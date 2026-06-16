#!/usr/bin/env python3
"""Re-DocRED OPERATIONAL WEDGE (S4): does decoy-gating (knockoff+ competition statistic W_i)
beat a PLAIN confidence threshold (raw Z_i) at MATCHED RECALL on atomic-fact precision and
multi-hop hallucinated-conclusion rate? Compares 5 systems (METHOD, PLAIN foil, CoT, RAG,
labeled conformal) in one shared (title, P-code, head_id, tail_id) triple space, scored by
the official tuple-matching metric, with document-block-bootstrap CIs and an alignment-error
confound check. CPU-only. Soft cap ~$3, HARD STOP $10.

Usage:
  uv run method.py --stage all --split confirmatory --limit 152 --bootstrap-B 2000
  uv run method.py --stage all --data mini            # smoke test on 3 docs
"""
from __future__ import annotations

import argparse
import asyncio
import json
import math
import resource
from pathlib import Path

import numpy as np
from loguru import logger

import analyze as A
from common import (CONFIG, CKPT_DIR, FULL_DATA, MINI_DATA, RULES, BudgetExceeded, CostMeter,
                    Embedder, WORKSPACE, load_docs, load_relation_schema, setup_logging)
from extract import run_extraction


def set_mem_limit(gb: float = 25.0):
    # Cap RSS-equivalent generously: container limit is 29 GB; torch CPU reserves large
    # VIRTUAL space so we use RLIMIT_DATA (heap) rather than RLIMIT_AS to avoid false OOM.
    try:
        b = int(gb * 1024 ** 3)
        resource.setrlimit(resource.RLIMIT_DATA, (b, b))
        logger.info(f"RLIMIT_DATA set to {gb} GB (container limit 29 GB)")
    except Exception as e:
        logger.warning(f"could not set RLIMIT_DATA: {e}")


def load_checkpoints(split_tag: str, doc_ids: list[str]) -> list[dict]:
    out_dir = CKPT_DIR / split_tag
    recs = []
    for did in doc_ids:
        p = out_dir / f"{did}.json"
        if p.exists():
            try:
                recs.append(json.loads(p.read_text()))
            except Exception:
                logger.warning(f"bad checkpoint {p}")
    return recs


# ======================================================================================
# WEDGE COMPUTATION
# ======================================================================================
def compute_delta_at(method_items, plain_items, gold, gold_total, doc_list, r_star, counts,
                     pcodes=None, noise_p=0.0, noise_seed=0):
    """Materialize METHOD & PLAIN at matched recall r_star (each at its own threshold), return
    (delta_point, lo, hi, precM, precP). Optional shared P-code corruption for sensitivity."""
    mi, pi = method_items, plain_items
    if noise_p > 0 and pcodes:
        rng = np.random.default_rng(noise_seed)
        mi, pi = [], []
        for m, p in zip(method_items, plain_items):
            pc = m["pcode"]
            if rng.random() < noise_p:
                alt = [x for x in pcodes if x != pc]
                pc = alt[int(rng.integers(len(alt)))]
            mi.append({**m, "pcode": pc})
            pi.append({**p, "pcode": pc})
    recM = A.materialize(mi, gold)
    recP = A.materialize(pi, gold)
    thrM, precM = A.threshold_for_recall(recM, gold_total, r_star)
    thrP, precP = A.threshold_for_recall(recP, gold_total, r_star)
    subM, corM = A.per_doc_stats(recM, thrM, doc_list)
    subP, corP = A.per_doc_stats(recP, thrP, doc_list)
    dmean, lo, hi = A.diff_ci(counts, corM, subM, corP, subP)
    return dmean, lo, hi, precM, precP, thrM, thrP


def run_analysis(records, docs, cost_meter, bootstrap_B, out_path: Path,
                 logprobs_available, caching_ok, calib_records=None):
    logger.info(f"=== STAGE 2: analysis on {len(records)} docs, B={bootstrap_B} ===")
    rel_schema = load_relation_schema()
    embedder = Embedder()
    aligner = A.Aligner(embedder, rel_schema)
    pcodes = aligner.pcodes

    # --- resolve all unique relation phrases (incl. gold relation_names for the I1 probe) ---
    phrases = []
    for rec in list(records) + list(calib_records or []):
        for c in rec["candidates"]:
            phrases.append(c["relation"])
        for key in ("cot", "rag"):
            for tr in rec.get(key, []):
                phrases.append(tr["relation"])
        for g in rec["gold_triples"]:
            phrases.append(g.get("relation_name", ""))
    asyncio.run(aligner.resolve_phrases(phrases, cost_meter))

    # --- Phase E: align every system into the shared triple space (hybrid aligner) ---
    preds = A.align_records(records, aligner, embedder, mode="hybrid")
    gold, gold_by_doc = A.build_gold(records)
    gold_total = len(gold)
    doc_list = [r["title"] for r in records]
    logger.info(f"GOLD tuples: {gold_total}; predicted pool sizes: "
                + ", ".join(f"{s}={len(preds[s])}" for s in A.SYSTEMS))

    # --- Phase F: PR curves + per-system max recall ---
    mat = {s: A.materialize(preds[s], gold) for s in A.SYSTEMS}
    pr = {s: A.pr_curve(mat[s], gold_total) for s in A.SYSTEMS}
    max_recall = {s: (pr[s][-1][0] if pr[s] else 0.0) for s in A.SYSTEMS}
    max_common = min(max_recall.values()) if max_recall else 0.0
    logger.info("max recall per system: " + ", ".join(f"{s}={max_recall[s]:.3f}" for s in A.SYSTEMS))
    logger.info(f"max_common_recall = {max_common:.3f}")
    # FAIRNESS INVARIANT: METHOD & PLAIN consume an identical candidate+alignment pool ->
    # identical max recall. If this breaks, the wedge read-off is invalid.
    if abs(max_recall["METHOD"] - max_recall["PLAIN"]) > 1e-9:
        logger.warning(f"FAIRNESS INVARIANT VIOLATED: METHOD max_recall={max_recall['METHOD']:.4f} "
                       f"!= PLAIN max_recall={max_recall['PLAIN']:.4f}")
    else:
        logger.info("Fairness invariant OK: METHOD and PLAIN share identical max recall")

    counts = A.make_boot_counts(len(doc_list), bootstrap_B, CONFIG["seed"])

    # --- Phase G: matched-recall wedge. Headline grid spans the METHOD/PLAIN SHARED recall
    # range (they have identical pools); other systems report None where recall-capped. ---
    grid_max = max_recall["METHOD"] if max_recall["METHOD"] > 0 else max_common
    # P3 PHASE 4: relax the grid floor so recall-limited comparators (CoT/RAG) get >=1
    # evaluable matched-recall point instead of an all-None row. lo_r = lowest POSITIVE
    # max_recall across systems (clamped >=0.01) so even the weakest system is evaluable at
    # grid[0]. Systems still producing zero evaluable points are DROPPED (recorded below),
    # never listed as all-null "participants".
    positive_recalls = [max_recall[s] for s in A.SYSTEMS if max_recall[s] > 0]
    lo_r = max(0.01, min(positive_recalls)) if positive_recalls else 0.01
    if lo_r >= grid_max:  # degenerate (all systems share the same ceiling); keep a small spread
        lo_r = max(0.005, grid_max / 2)
    grid = list(np.linspace(lo_r, max(grid_max, lo_r + 1e-6), CONFIG["recall_grid_n"]))
    prec_by_sys = {s: [] for s in A.SYSTEMS}
    prec_ci_by_sys = {s: [] for s in A.SYSTEMS}
    delta_arr, delta_ci, delta_p = [], [], []
    for r_star in grid:
        for s in A.SYSTEMS:
            if r_star > max_recall[s] + 1e-9:  # system is recall-capped at this point
                prec_by_sys[s].append(None)
                prec_ci_by_sys[s].append([None, None])
                continue
            thr, prec = A.threshold_for_recall(mat[s], gold_total, r_star)
            sub, cor = A.per_doc_stats(mat[s], thr, doc_list)
            lo, hi = A.ratio_ci(counts, cor, sub)
            prec_by_sys[s].append(prec)
            prec_ci_by_sys[s].append([lo, hi])
        dmean, lo, hi, pm, pp, _, _ = compute_delta_at(
            preds["METHOD"], preds["PLAIN"], gold, gold_total, doc_list, r_star, counts)
        # one-sided bootstrap p: P(delta <= 0)
        recM = A.materialize(preds["METHOD"], gold)
        recP = A.materialize(preds["PLAIN"], gold)
        thrM, _ = A.threshold_for_recall(recM, gold_total, r_star)
        thrP, _ = A.threshold_for_recall(recP, gold_total, r_star)
        subM, corM = A.per_doc_stats(recM, thrM, doc_list)
        subP, corP = A.per_doc_stats(recP, thrP, doc_list)
        a = counts @ corM; da = counts @ subM
        b = counts @ corP; db = counts @ subP
        with np.errstate(divide="ignore", invalid="ignore"):
            dd = np.where(da > 0, a / da, np.nan) - np.where(db > 0, b / db, np.nan)
        dd = dd[~np.isnan(dd)]
        pval = float(np.mean(dd <= 0)) if len(dd) else 1.0
        delta_arr.append(dmean)
        delta_ci.append([lo, hi])
        delta_p.append(pval)

    # BH correction across grid points
    m = len(delta_p)
    order = np.argsort(delta_p)
    bh_sig = [False] * m
    for rank, idx in enumerate(order, start=1):
        if delta_p[idx] <= (rank / m) * 0.05:
            for j in range(rank):
                bh_sig[order[j]] = True
            break
    confirmed_points = [i for i in range(m)
                        if (delta_ci[i][0] is not None and delta_ci[i][0] > 0 and bh_sig[i])]
    wedge_confirmed = len(confirmed_points) > 0

    # P3 PHASE 4: complete-or-drop comparators. A system PARTICIPATES iff it produces >=1
    # evaluable (non-None) matched-recall precision point; otherwise it is DROPPED (recorded
    # with reason + ceiling) and EXCLUDED from the wedge arrays + the verdict's cited systems.
    grid0 = grid[0]
    participating_systems, dropped_comparators = [], {}
    for s in A.SYSTEMS:
        n_eval = sum(1 for x in prec_by_sys[s] if x is not None)
        if n_eval >= 1:
            participating_systems.append(s)
        else:
            dropped_comparators[s] = {
                "reason": (f"recall ceiling {max_recall[s]:.4f} below evaluable grid start "
                           f"{grid0:.4f} — produced NO comparable matched-recall point"),
                "max_recall": round(max_recall[s], 5),
                "grid_start": round(grid0, 5)}
    logger.info(f"PHASE4 participating_systems={participating_systems} "
                f"dropped={list(dropped_comparators)} (grid[0]={grid0:.4f})")

    # --- METHOD knockoff+ operating points ---
    knock_ops = {}
    method_items = preds["METHOD"]
    W_list = [it["score"] for it in method_items if it["score"] is not None]
    for alpha in CONFIG["alpha_grid"]:
        T = A.knockoff_plus_threshold(W_list, alpha)
        if T is None:
            knock_ops[str(alpha)] = {"recall": None, "precision": None, "n_admit": 0,
                                     "T": None, "k_floor": CONFIG["W_floor_k"][alpha],
                                     "k_floor_met": False}
            continue
        adm = A.materialize([it for it in method_items if it["score"] >= T], gold)
        n_adm = len(adm)
        cor = sum(1 for r in adm if r["correct"])
        knock_ops[str(alpha)] = {
            "recall": cor / max(1, gold_total), "precision": cor / max(1, n_adm),
            "n_admit": n_adm, "T": float(T), "k_floor": CONFIG["W_floor_k"][alpha],
            "k_floor_met": n_adm >= CONFIG["W_floor_k"][alpha]}

    # --- CONF conformal (Mohri-Hashimoto) operating points, calibrated on the labeled pilot ---
    conformal_ops = {}
    n_calib_labels = 0
    if calib_records:
        calib_preds = A.align_records(calib_records, aligner, embedder, mode="hybrid")
        calib_gold, _ = A.build_gold(calib_records)
        calib_conf = A.materialize(calib_preds["CONF"], calib_gold)
        calib_by_doc = {}
        for r in calib_conf:
            calib_by_doc.setdefault(r["doc"], []).append((r["score"], r["correct"]))
        test_conf = [(r["score"], r["correct"]) for r in mat["CONF"]]
        conformal_ops = A.conformal_operating_points(calib_by_doc, test_conf, gold_total,
                                                     CONFIG["alpha_grid"])
        n_calib_labels = sum(len(r["gold_triples"]) for r in calib_records)
        logger.info(f"Conformal calibrated on {len(calib_records)} pilot docs "
                    f"({n_calib_labels} labels); operating points: {list(conformal_ops.keys())}")

    # --- Phase G2: multi-hop hallucinated-conclusion rate. Read at PARTIAL admission: at
    # max recall METHOD & PLAIN admit the identical shared pool so any delta vanishes; the
    # wedge lives where the W vs Z ranking selects DIFFERENT subsets. Compute across the grid
    # (figure-ready) + a headline at ~70% of max recall. ---
    rep_idx = max(1, min(len(grid) - 2, int(round(0.7 * (len(grid) - 1)))))
    r_rep = grid[rep_idx]

    def hallu_at(r_star):
        nds, nhs, pts = {}, {}, {}
        for s in A.SYSTEMS:
            if r_star > max_recall[s] + 1e-9:
                nds[s] = np.zeros(len(doc_list)); nhs[s] = np.zeros(len(doc_list)); pts[s] = None
                continue
            thr, _ = A.threshold_for_recall(mat[s], gold_total, r_star)
            adm = A.admitted_by_doc(mat[s], thr)
            nd, nh = A.hallu_per_doc(adm, gold_by_doc, doc_list)
            nds[s], nhs[s] = nd, nh
            pts[s] = float(nh.sum() / nd.sum()) if nd.sum() > 0 else None
        return nds, nhs, pts

    # grid arrays
    hallu_grid = {s: [] for s in A.SYSTEMS}
    hallu_delta_grid, hallu_delta_ci_grid = [], []
    for r_star in grid:
        nds, nhs, pts = hallu_at(r_star)
        for s in A.SYSTEMS:
            hallu_grid[s].append(pts[s])
        dm, lo, hi = A.diff_ci(counts, nhs["METHOD"], nds["METHOD"], nhs["PLAIN"], nds["PLAIN"])
        hallu_delta_grid.append(dm)
        hallu_delta_ci_grid.append([lo, hi])
    # headline at r_rep
    hallu_nd, hallu_nh, hallu_pts = hallu_at(r_rep)
    hallu = {}
    for s in A.SYSTEMS:
        lo, hi = A.ratio_ci(counts, hallu_nh[s], hallu_nd[s])
        hallu[s] = {"point": hallu_pts[s], "ci_lo": lo, "ci_hi": hi,
                    "n_derived": int(hallu_nd[s].sum()), "n_hallucinated": int(hallu_nh[s].sum())}
    hd_mean, hd_lo, hd_hi = A.diff_ci(counts, hallu_nh["METHOD"], hallu_nd["METHOD"],
                                      hallu_nh["PLAIN"], hallu_nd["PLAIN"])

    # P3 PHASE 5: power assessment. The comparison is UNDERPOWERED if either system derives
    # < power_target conclusions OR the METHOD-PLAIN delta CI is wider than 0.5. When
    # underpowered we flag it explicitly with exact per-system counts rather than presenting
    # the bars as a confirmed comparison.
    POWER_TARGET = CONFIG["power_target"]
    nd_method = int(hallu_nd["METHOD"].sum())
    nd_plain = int(hallu_nd["PLAIN"].sum())
    _w = (hd_hi - hd_lo) if (hd_hi is not None and hd_lo is not None
                             and hd_hi == hd_hi and hd_lo == hd_lo) else float("inf")
    hallu_ci_width = _w
    hallu_underpowered = (min(nd_method, nd_plain) < POWER_TARGET) or (_w > 0.5)
    n_derived_by_system = {s: int(hallu_nd[s].sum()) for s in A.SYSTEMS}
    logger.info(f"PHASE5 multi-hop power: n_derived METHOD={nd_method} PLAIN={nd_plain} "
                f"(target {POWER_TARGET}); delta CI width={_w if _w!=float('inf') else 'inf'} "
                f"-> underpowered={hallu_underpowered}")

    # P3 PHASE 6: LABEL-FREE REGIME-DIAGNOSTIC (gold-free, ZERO API). Predicts the wedge sign
    # from cached Z/Zt/W/self-consistency, then validates against the realized delta CIs.
    import regime as REG
    recP_rep = A.materialize(preds["PLAIN"], gold)
    T_op_rep, _ = A.threshold_for_recall(recP_rep, gold_total, r_rep)
    regime_diag = REG.compute_regime_diagnostic(
        records, realized_delta_ci=delta_ci, realized_grid=grid,
        bootstrap_B=bootstrap_B, seed=CONFIG["seed"], T_op=float(T_op_rep))
    regime_rows = REG.gather_rows(records)  # reused for per-doc audit fields below

    # P3: human-auditable multi-hop PROOF TRACES (rule + premises -> conclusion) over METHOD's
    # admitted atomic facts at the representative recall. Names resolved for readability.
    reasoning_traces = []
    matM_rep = A.materialize(preds["METHOD"], gold)
    thrM_rep, _ = A.threshold_for_recall(matM_rep, gold_total, r_rep)
    admM_rep = A.admitted_by_doc(matM_rep, thrM_rep)
    ent_name_by_doc = {rec["title"]: {e["entity_id"]: (e.get("canonical_name")
                       or (e.get("aliases") or [""])[0]) for e in rec["entities"]}
                       for rec in records}
    for d, tuples in admM_rep.items():
        if len(reasoning_traces) >= 8:
            break
        facts = {(pc, h, t) for (_, pc, h, t) in tuples}
        traces = A.forward_chain_traced(facts)
        if not traces:
            continue
        nm = ent_name_by_doc.get(d, {})
        def _rd(tr):
            pc, h, t = tr
            return {"relation": pc, "relation_name": aligner.pmap.get(pc, {}).get("relation_name", pc),
                    "head": nm.get(h, str(h)), "tail": nm.get(t, str(t))}
        tr0 = traces[0]
        concl = tuple(tr0["conclusion"])
        reasoning_traces.append({
            "doc": d, "rule": tr0["rule"],
            "premises": [_rd(tuple(p)) for p in tr0["premises"]],
            "conclusion": _rd(concl),
            "conclusion_in_gold": bool((d, concl[0], concl[1], concl[2]) in gold),
            "note": ("conclusion_in_gold=false may be a Re-DocRED residual false negative rather "
                     "than a true hallucination (relative interpretation only).")})
    logger.info(f"Exported {len(reasoning_traces)} human-auditable multi-hop proof traces")

    # --- Phase I1: aligner self-error probe (align gold surface forms) ---
    rel_ok = el_ok = rel_tot = el_tot = 0
    for rec in records:
        eidx = A.build_doc_entity_index(embedder, rec["entities"])
        for g in rec["gold_triples"]:
            pc = aligner.relation_pcode(g.get("relation_name", ""), mode="hybrid")
            rel_tot += 1
            if pc == g["relation_pid"]:
                rel_ok += 1
            hid = A.link_entity(g.get("head_name", ""), eidx, embedder, CONFIG["el_embed_floor"])
            tid = A.link_entity(g.get("tail_name", ""), eidx, embedder, CONFIG["el_embed_floor"])
            el_tot += 1
            if hid == g["head_id"] and tid == g["tail_id"]:
                el_ok += 1
    aligner_rel_acc = rel_ok / max(1, rel_tot)
    aligner_el_acc = el_ok / max(1, el_tot)
    logger.info(f"Aligner self-error probe: relation_acc={aligner_rel_acc:.3f} "
                f"entitylink_acc={aligner_el_acc:.3f}")

    # --- Phase I2: alignment perturbation sensitivity (delta sign must persist) ---
    sensitivity = {}
    d0, lo0, hi0, _, _, _, _ = compute_delta_at(preds["METHOD"], preds["PLAIN"], gold,
                                                gold_total, doc_list, r_rep, counts)
    sensitivity["baseline"] = {"r_star": r_rep, "delta": d0, "ci": [lo0, hi0]}
    for p in CONFIG["noise_levels"]:
        dm, lo, hi, _, _, _, _ = compute_delta_at(
            preds["METHOD"], preds["PLAIN"], gold, gold_total, doc_list, r_rep, counts,
            pcodes=pcodes, noise_p=p, noise_seed=CONFIG["seed"] + int(p * 100))
        sensitivity[f"noise_{int(p*100)}pct"] = {"delta": dm, "ci": [lo, hi]}
    # embedding-only aligner
    preds_eo = A.align_records(records, aligner, embedder, mode="embed_only")
    dm, lo, hi, _, _, _, _ = compute_delta_at(preds_eo["METHOD"], preds_eo["PLAIN"], gold,
                                              gold_total, doc_list, r_rep, counts)
    sensitivity["embed_only_aligner"] = {"delta": dm, "ci": [lo, hi]}
    # strict EL floor 0.7
    preds_strict = A.align_records(records, aligner, embedder, mode="hybrid",
                                   el_floor=CONFIG["el_strict_floor"])
    gold_s, _ = gold, None
    dm, lo, hi, _, _, _, _ = compute_delta_at(preds_strict["METHOD"], preds_strict["PLAIN"],
                                              gold, gold_total, doc_list, r_rep, counts)
    sensitivity["strict_el_floor_0.7"] = {"delta": dm, "ci": [lo, hi]}

    # --- contamination rate (decoys) ---
    n_gen = sum(r["contamination"]["n_generated"] for r in records)
    n_ent = sum(r["contamination"]["n_entailed"] for r in records)
    contamination_rate = n_ent / max(1, n_gen)

    # --- P3 PHASE 3: scope honesty. State the TRUE n and the achievable recall ceiling AT the
    # claim. n_docs_used is the ACTUAL scored count (never the requested 152 if fewer landed). ---
    n_docs_used = len(records)
    n_docs_requested = len(docs)
    recall_ceiling = float(max_recall["METHOD"])
    scope = {
        "n_docs_used": n_docs_used,
        "n_docs_requested": n_docs_requested,
        "recall_ceiling": round(recall_ceiling, 5),
        "recall_ceiling_definition": "max recall of METHOD/PLAIN's shared candidate+alignment pool",
        "bootstrap_B": bootstrap_B,
        "grid_start": round(grid[0], 5),
    }

    # --- verdict ---
    disconfirmed = not wedge_confirmed
    notes = ("RELATIVE comparison only: Re-DocRED residual false negatives depress recall for "
             "ALL systems equally and inflate hallucinated-conclusion counts for ALL systems "
             "equally; no absolute realized-FDR diagonal is asserted (that belongs to CLUTRR). "
             "METHOD and PLAIN consume an IDENTICAL candidate+alignment pool (same max recall); "
             "the only difference is the gate (W_i competition vs raw Z_i threshold).")
    if wedge_confirmed:
        verdict_msg = ("WEDGE CONFIRMED: decoy-gating (W_i) yields higher atomic-fact precision "
                       "than the plain Z_i threshold at matched recall (delta CI>0, BH-significant) "
                       f"at {len(confirmed_points)}/{m} recall points (recall <= "
                       f"{recall_ceiling:.3f} on {n_docs_used} docs).")
    else:
        verdict_msg = (f"OPERATIONAL DISCONFIRMATION at recall <= {recall_ceiling:.3f} on "
                       f"{n_docs_used} docs (pre-registered): the wedge collapses to "
                       "'thresholding-is-enough' — no recall point shows a precision advantage of "
                       "decoy-gating over the plain confidence threshold with CI entirely > 0.")
    operational_verdict = (
        f"{'confirmed' if wedge_confirmed else 'disconfirmed'} at recall <= {recall_ceiling:.3f} "
        f"on {n_docs_used} docs; reframed as a label-free regime-diagnostic — the Re-DocRED scorer "
        f"sits in the {regime_diag['predicted_regime']} regime (predicted gold-free as "
        f"'{regime_diag['predicted_wedge_sign']}'; prediction_correct="
        f"{regime_diag['prediction_vs_realized']['prediction_correct']} vs the realized wedge).")
    logger.info(verdict_msg)
    logger.info(f"OPERATIONAL VERDICT: {operational_verdict}")

    # --------------------------- ASSEMBLE method_out.json -----------------------------
    def downsample(pts, k=60):
        if len(pts) <= k:
            return [[round(a, 5), round(b, 5), round(c, 5)] for a, b, c in pts]
        step = len(pts) / k
        return [[round(pts[int(i * step)][0], 5), round(pts[int(i * step)][1], 5),
                 round(pts[int(i * step)][2], 5)] for i in range(k)]

    # per-doc gold-free regime fields (self-consistency f histogram + winrate) for auditability
    regime_rows_by_doc = {}
    for row in regime_rows:
        regime_rows_by_doc.setdefault(row["doc"], []).append(row)

    input_by_id = {d["doc_id"]: d for d in docs}
    examples = []
    for rec in records:
        did = rec["doc_id"]
        src = input_by_id.get(did, {})
        per_sys_pred = {}
        for s in A.SYSTEMS:
            items = [it for it in preds[s] if it["doc"] == rec["title"]]
            per_sys_pred[s] = [[it["pcode"], it["h_id"], it["t_id"], round(float(it["score"]), 4)]
                               for it in items if it["score"] is not None]
        # gold-free per-doc regime audit fields (winrate of decoys, self-consistency hist)
        rrows = regime_rows_by_doc.get(rec["title"], [])
        n_decoy_win = sum(1 for r in rrows if r["Zt"] >= r["Z"])
        f_hist = [0, 0, 0]  # f<=0.4, 0.4<f<0.8, f>=0.8
        for r in rrows:
            f_hist[0 if r["f"] <= 0.4 else (2 if r["f"] >= 0.8 else 1)] += 1
        ex = {
            "input": src.get("input", "")[:3000],
            "output": json.dumps([[g["relation_pid"], g["head_id"], g["tail_id"]]
                                  for g in rec["gold_triples"]]),
            "metadata_doc_id": did,
            "metadata_title": rec["title"],
            "metadata_fold": rec["fold"],
            "metadata_n_candidates": len(rec["candidates"]),
            "metadata_n_gold": len(rec["gold_triples"]),
            "metadata_decoy_winrate": (round(n_decoy_win / len(rrows), 4) if rrows else None),
            "metadata_self_consistency_f_hist": f_hist,
        }
        for s in participating_systems:
            ex[f"predict_{s}"] = json.dumps(per_sys_pred[s])
        examples.append(ex)

    metadata = {
        "method_name": "Decoy-gating (knockoff+ W_i) vs plain confidence threshold (Z_i)",
        "description": ("Operational wedge on Re-DocRED at matched recall: atomic-fact precision, "
                        "multi-hop hallucinated-conclusion rate, knockoff+ operating points."),
        "n_docs_used": len(records),
        "split_role": records[0]["split_role"] if records else None,
        "model": CONFIG["model_primary"],
        "elicitation": CONFIG["elicitation"],
        "logprobs_available": logprobs_available,
        "caching_ok": caching_ok,
        "cost_usd": round(cost_meter.total, 5),
        "n_api_calls": cost_meter.n_calls,
        "n_calibration_labels_conformal": n_calib_labels,
        "seed": CONFIG["seed"],
        "bootstrap_B": bootstrap_B,
        "systems": A.SYSTEMS,
        "participating_systems": participating_systems,
        "dropped_comparators": dropped_comparators,
        "scope": scope,
        "rules_list": [r["name"] for r in RULES],
        "config": {k: CONFIG[k] for k in ("cand_cap", "n_overgen", "n_conf_samples",
                                          "alpha_grid", "W_floor_k", "align_shortlist_k",
                                          "el_embed_floor", "decoy_max_regen")},
        "max_recall_per_system": {s: round(max_recall[s], 5) for s in A.SYSTEMS},
        "max_common_recall": round(max_common, 5),
        "pr_curves": {s: downsample(pr[s]) for s in A.SYSTEMS},
        "matched_recall": {
            "recall_grid": [round(x, 5) for x in grid],
            "participating_systems": participating_systems,
            "precision": {s: [None if x is None else round(x, 5) for x in prec_by_sys[s]]
                          for s in participating_systems},
            "precision_ci": {s: [[None if a is None or a != a else round(a, 5),
                                  None if b is None or b != b else round(b, 5)]
                                 for a, b in prec_ci_by_sys[s]] for s in participating_systems},
            "delta_method_minus_plain": [round(x, 5) for x in delta_arr],
            "delta_ci": [[round(a, 5) if a is not None and a == a else None,
                          round(b, 5) if b is not None and b == b else None]
                         for a, b in delta_ci],
            "delta_bootstrap_p_value": [round(x, 5) for x in delta_p],
            "bh_significant": bh_sig,
            "confirmed_recall_points": [round(grid[i], 5) for i in confirmed_points],
        },
        "knockoff_operating_points": knock_ops,
        "conformal_operating_points": {
            "calibrated_on": "pilot" if calib_records else None,
            "n_calibration_labels": n_calib_labels,
            "by_alpha": conformal_ops,
            "note": ("CONF is the LABELED reference (Mohri-Hashimoto conformal back-off): q-hat "
                     "calibrated on the pilot split; the label-free decoy gate (METHOD) uses 0 "
                     "labels. In the matched-recall grid CONF is swept by its label-free combined "
                     "frequency+confidence score."),
        },
        "hallucinated_conclusion_rate": {
            "representative_recall": round(r_rep, 5),
            "by_system": hallu,
            "delta_method_minus_plain": {"point": hd_mean, "ci_lo": hd_lo, "ci_hi": hd_hi},
            "underpowered": bool(hallu_underpowered),
            "power_target": POWER_TARGET,
            "n_derived_by_system": n_derived_by_system,
            "delta_ci_width": (None if hallu_ci_width == float("inf") else round(hallu_ci_width, 5)),
            "power_note": (f"UNDERPOWERED: min per-system derived conclusions "
                           f"({min(nd_method, nd_plain)}) < power_target ({POWER_TARGET}) and/or "
                           f"delta CI width > 0.5 — the METHOD-vs-PLAIN hallucination bars are NOT "
                           f"a confirmed comparison." if hallu_underpowered else
                           f"POWERED: both systems derive >= power_target ({POWER_TARGET}) "
                           f"conclusions with delta CI width <= 0.5."),
            "recall_grid": [round(x, 5) for x in grid],
            "rate_by_system_grid": {s: [None if v is None else round(v, 5) for v in hallu_grid[s]]
                                    for s in A.SYSTEMS},
            "delta_grid": [None if v is None or v != v else round(v, 5) for v in hallu_delta_grid],
            "delta_ci_grid": [[None if a is None or a != a else round(a, 5),
                               None if b is None or b != b else round(b, 5)]
                              for a, b in hallu_delta_ci_grid],
            "note": ("Read the METHOD-vs-PLAIN hallucination wedge at PARTIAL admission "
                     "(representative_recall, ~70% of max): at max recall both admit the "
                     "identical shared candidate pool so the delta is structurally 0. Absolute "
                     "rates are inflated for ALL systems by Re-DocRED residual false negatives "
                     "(a derived true fact absent from gold counts as 'hallucinated'); only the "
                     "RELATIVE METHOD-vs-PLAIN difference is interpreted."),
        },
        "alignment_check": {
            "aligner_relation_accuracy": round(aligner_rel_acc, 5),
            "aligner_entitylink_accuracy": round(aligner_el_acc, 5),
            "sensitivity": sensitivity,
        },
        "contamination_rate_decoys": round(contamination_rate, 5),
        "reasoning_traces": reasoning_traces,
        "regime_diagnostic": regime_diag,
        "verdict": {
            "wedge_confirmed": wedge_confirmed,
            "disconfirmed": disconfirmed,
            "n_confirmed_points": len(confirmed_points),
            "scope": scope,
            "recall_ceiling": round(recall_ceiling, 5),
            "n_docs_used": n_docs_used,
            "message": verdict_msg,
            "operational_verdict": operational_verdict,
            "predicted_regime": regime_diag["predicted_regime"],
            "predicted_wedge_sign": regime_diag["predicted_wedge_sign"],
            "prediction_correct": regime_diag["prediction_vs_realized"]["prediction_correct"],
            "notes": notes,
        },
        "cost_log_summary": {"total_usd": round(cost_meter.total, 5),
                             "n_calls": cost_meter.n_calls,
                             "soft_cap": CONFIG["soft_cap_usd"],
                             "hard_stop": CONFIG["hard_stop_usd"]},
    }
    def sanitize(o):
        if isinstance(o, dict):
            return {k: sanitize(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [sanitize(v) for v in o]
        if isinstance(o, float) and not math.isfinite(o):
            return None
        if isinstance(o, (np.floating,)):
            v = float(o)
            return v if math.isfinite(v) else None
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.bool_,)):
            return bool(o)
        return o

    out = {"metadata": sanitize(metadata),
           "datasets": [{"dataset": "Re-DocRED", "examples": sanitize(examples)}]}
    out_path.write_text(json.dumps(out, indent=2, allow_nan=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1024:.1f} KB)")
    return out


# ======================================================================================
async def probe_model(cost_meter) -> tuple[bool, bool]:
    from llm import LLM
    logprobs_available = caching_ok = False
    long_prefix = "DOCUMENT:\n" + ("Background context. " * 120) + "\n\n"
    async with LLM(cost_meter) as llm:
        c, lp = await llm.chat([{"role": "user", "content": long_prefix + "Reply OK."}],
                               max_tokens=16, want_logprobs=True, tag="probe1")
        logprobs_available = lp is not None
        c2, _ = await llm.chat([{"role": "user", "content": long_prefix + "Reply YES."}],
                               max_tokens=16, tag="probe2")
    logger.info(f"PROBE: logprobs_available={logprobs_available}")
    return logprobs_available, caching_ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["all", "extract", "analyze"], default="all")
    ap.add_argument("--split", default="confirmatory")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--data", choices=["full", "mini"], default="full")
    ap.add_argument("--bootstrap-B", type=int, default=CONFIG["bootstrap_B"])
    ap.add_argument("--cand-cap", type=int, default=None)
    ap.add_argument("--n-overgen", type=int, default=None)
    ap.add_argument("--out", default=str(WORKSPACE / "method_out.json"))
    ap.add_argument("--tag", default=None)
    ap.add_argument("--calib-split", default="pilot")
    ap.add_argument("--calib-limit", type=int, default=None)
    ap.add_argument("--no-calib", action="store_true")
    args = ap.parse_args()

    setup_logging("run")
    set_mem_limit(25.0)
    if args.cand_cap:
        CONFIG["cand_cap"] = args.cand_cap
    if args.n_overgen:
        CONFIG["n_overgen"] = args.n_overgen

    data_path = MINI_DATA if args.data == "mini" else FULL_DATA
    split = None if args.data == "mini" else args.split
    docs = load_docs(data_path, split, args.limit)
    if not docs:
        logger.error("No docs loaded; aborting")
        return
    split_tag = args.tag or (f"mini" if args.data == "mini" else args.split)

    use_calib = (not args.no_calib) and args.data == "full"
    calib_docs = load_docs(data_path, args.calib_split, args.calib_limit) if use_calib else []

    cost_meter = CostMeter(CONFIG["hard_stop_usd"], CONFIG["soft_cap_usd"])
    logprobs_available = caching_ok = False

    if args.stage in ("all", "extract"):
        try:
            logprobs_available, caching_ok = asyncio.run(probe_model(cost_meter))
        except BudgetExceeded as e:
            logger.error(str(e))
            return
        try:
            asyncio.run(run_extraction(docs, cost_meter, split_tag))
            if calib_docs and not cost_meter.over_soft():
                logger.info(f"Extracting {len(calib_docs)} {args.calib_split} docs for conformal calibration")
                asyncio.run(run_extraction(calib_docs, cost_meter, args.calib_split))
        except BudgetExceeded as e:
            logger.error(f"Budget exceeded during extraction: {e}")

    if args.stage in ("all", "analyze"):
        records = load_checkpoints(split_tag, [d["doc_id"] for d in docs])
        if not records:
            logger.error("No checkpoints to analyze")
            return
        calib_records = (load_checkpoints(args.calib_split, [d["doc_id"] for d in calib_docs])
                         if calib_docs else None)
        try:
            run_analysis(records, docs, cost_meter, args.bootstrap_B, Path(args.out),
                         logprobs_available, caching_ok, calib_records=calib_records)
        except BudgetExceeded as e:
            logger.error(f"Budget exceeded during analysis: {e}")

    logger.info(f"DONE. Total cost ${cost_meter.total:.4f} over {cost_meter.n_calls} calls")


if __name__ == "__main__":
    main()
