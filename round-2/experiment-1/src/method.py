"""
method.py
=========
End-to-end runner for the CLUTRR label-free knockoff+ FDR calibration diagonal.

Our method   : decoy-competition knockoff+ gate (counterfactual decoys) -> realized FDR vs target alpha.
Baseline 1   : PLAIN confidence-threshold gate (decoy-free; raw LLM confidence = the standard foil).
Baseline 2   : SWAP-decoy knockoff gate (negative control; predicted anti-conservative).
Corroboration: deterministic entrapment FDP (r=1), 3-way agreement with gold & decoy estimates.

Stages: A = Phase-0 pilot (elicitation selection by tail-AUC, control behavior, populability,
power, alpha* pre-registration). B = confirmatory diagonal + pre-registered disconfirmation.
C = entrapment corroboration. CPU-only; OpenRouter openai/gpt-4.1-nano; cost-tracked, $10 hard cap.

Usage:  uv run method.py --scale {mini,pilot,full} [--concurrency N]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import math
import time
from pathlib import Path

import numpy as np

import fdr_core as fc
import pipeline as pl
from llm_client import LLM, CostTracker, LLMCache, HardStop

SEED = 20240617
MODEL = "openai/gpt-4.1-nano"
ALPHA_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]
TAU = 0.05
N_FALSE_MIN = 40
B_BOOT = 2000
WS = Path(__file__).resolve().parent


# ----------------------------------------------------------------------------
# Data loading + crisp gold
# ----------------------------------------------------------------------------
def load_docs(path, which="all"):
    with open(path) as f:
        data = json.load(f)
    examples = data["datasets"][0]["examples"]
    docs = []
    for ex in examples:
        inp = json.loads(ex["input"])
        out = json.loads(ex["output"])
        is_pilot = ex["metadata_is_pilot"]
        if which == "pilot" and not is_pilot:
            continue
        if which == "confirmatory" and is_pilot:
            continue
        gold_true = set()
        covered = set()
        atomic_pairs, bridge_pairs = set(), set()
        for fct in out["atomic_facts"]:
            gold_true.add((fct["head"], fct["relation"].lower(), fct["tail"]))
            covered.add((fct["head"], fct["tail"]))
            atomic_pairs.add((fct["head"], fct["tail"]))
        for fct in out["multi_hop_facts"]:
            gold_true.add((fct["head"], fct["relation"].lower(), fct["tail"]))
            covered.add((fct["head"], fct["tail"]))
            bridge_pairs.add((fct["head"], fct["tail"]))
        docs.append({
            "doc_id": inp["doc_id"], "document_text": inp["document_text"],
            "entities": inp["entities"], "k": ex["metadata_chain_length_k"],
            "is_pilot": is_pilot, "gold_true": gold_true, "covered": covered,
            "atomic_pairs": atomic_pairs, "bridge_pairs": bridge_pairs,
        })
    return docs


# ----------------------------------------------------------------------------
# Per-doc: build units (extraction -> label -> decoys/entrapment), then score
# ----------------------------------------------------------------------------
async def build_units(llm, doc, names_pool):
    cand = await pl.extract_candidates(llm, doc, n_samples=3, cap_per_family=20)
    units = {"atomic": [], "bridge": []}
    n_unjudge = 0
    for family in ("atomic", "bridge"):
        for tr in cand[family]:
            label = fc.gold_label((tr["head"], tr["relation"], tr["tail"]),
                                  doc["gold_true"], doc["covered"])
            if label == fc.UNJUDGEABLE:
                n_unjudge += 1
                continue
            cf_decoy, contaminated = await pl.make_counterfactual_decoy(llm, doc, tr)
            swap_decoy = pl.make_swap_decoy(doc, tr)
            ent, ent_mech = pl.make_entrapment(doc, tr, names_pool, doc["gold_true"],
                                               doc["covered"], idx=len(units[family]))
            units[family].append({
                "real": tr, "label": label, "cf_decoy": cf_decoy, "swap_decoy": swap_decoy,
                "entrapment": ent, "ent_mech": ent_mech, "contaminated": contaminated,
            })
    return {"doc_id": doc["doc_id"], "k": doc["k"], "is_pilot": doc["is_pilot"],
            "units": units, "discard": cand["discard"], "n_unjudge": n_unjudge}


async def score_units(llm, doc_text, doc_units, elicitation, score_decoys=True):
    """Score real (+ cf/swap/entrapment if score_decoys) for every unit, with `elicitation`."""
    fn = pl.ELICITATIONS[elicitation]

    async def score_unit(u):
        u["z_real"] = await fn(llm, doc_text, u["real"])
        if score_decoys:
            u["z_cf"] = await fn(llm, doc_text, u["cf_decoy"])
            u["z_swap"] = await fn(llm, doc_text, u["swap_decoy"])
            u["z_ent"] = await fn(llm, doc_text, u["entrapment"])
        return u

    for family in ("atomic", "bridge"):
        await asyncio.gather(*[score_unit(u) for u in doc_units["units"][family]])
    return doc_units


async def gather_bounded(coros, batch=24):
    """Run coroutines with at most `batch` documents in flight (HTTP further capped by the
    client semaphore). Preserves order."""
    results = [None] * len(coros)
    idx = 0
    pending = set()
    it = iter(enumerate(coros))
    for i, c in it:
        pending.add(asyncio.ensure_future(_idx_wrap(i, c)))
        if len(pending) >= batch:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            for d in done:
                j, r = d.result()
                results[j] = r
    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        for d in done:
            j, r = d.result()
            results[j] = r
    return results


async def _idx_wrap(i, coro):
    return i, await coro


# ----------------------------------------------------------------------------
# Gate statistics over scored doc-units
# ----------------------------------------------------------------------------
def _families(family):
    return ("atomic", "bridge") if family == "pooled" else (family,)


def family_arrays(scored_docs, family, decoy_key="z_cf"):
    """Flatten scored docs into arrays for a family ('atomic'/'bridge'/'pooled'). decoy_key
    selects which decoy's z to compete against ('z_cf' or 'z_swap')."""
    W, Z, lab, zdec = [], [], [], []
    for d in scored_docs:
        for fam in _families(family):
            for u in d["units"][fam]:
                if "z_real" not in u:
                    continue
                zr = u["z_real"]
                zd = u["z_cf"] if decoy_key == "z_cf" else u["z_swap"]
                W.append(fc.w_statistic(zr, zd))
                Z.append(zr)
                lab.append(u["label"])
                zdec.append(zd)
    return np.array(W), np.array(Z), np.array(lab, dtype=object), np.array(zdec)


def per_doc_family_records(scored_docs, family):
    """One record per doc: lists of (z_real, z_cf, z_swap, z_ent, label) for bootstrap."""
    recs = []
    for d in scored_docs:
        rows = []
        for fam in _families(family):
            for u in d["units"][fam]:
                if "z_real" not in u:
                    continue
                rows.append((u["z_real"], u["z_cf"], u["z_swap"], u.get("z_ent"), u["label"]))
        recs.append(rows)
    return recs


def realized_fdr_from_rows(rows_concat, alpha, which="knockoff"):
    """rows_concat: list of (z_real, z_cf, z_swap, z_ent, label). Returns realized FDR of the
    admitted set under the chosen gate."""
    if not rows_concat:
        return float("nan")
    zr = np.array([r[0] for r in rows_concat])
    zc = np.array([r[1] for r in rows_concat])
    zs = np.array([r[2] for r in rows_concat])
    lab = np.array([r[4] for r in rows_concat], dtype=object)
    if which == "knockoff":
        W = np.array([fc.w_statistic(a, b) for a, b in zip(zr, zc)])
        _, adm, _ = fc.knockoff_plus_threshold(W, alpha)
    elif which == "swap":
        W = np.array([fc.w_statistic(a, b) for a, b in zip(zr, zs)])
        _, adm, _ = fc.knockoff_plus_threshold(W, alpha)
    elif which == "plain":
        _, adm, _ = fc.plain_threshold_gate(zr, alpha)
    else:
        raise ValueError(which)
    if not adm:
        return float("nan")
    n_false = sum(1 for i in adm if lab[i] == fc.FALSE)
    return n_false / len(adm)


def diagonal_for_family(scored_docs, family):
    """Compute the full diagonal (knockoff / swap / plain) with bootstrap CIs for one family."""
    W, Z, lab, _ = family_arrays(scored_docs, family, "z_cf")
    n_pos = int(np.sum(W > 0))
    per_doc = per_doc_family_records(scored_docs, family)
    flat = [r for doc in per_doc for r in doc]
    rows = []
    for alpha in ALPHA_GRID:
        T, adm, decoy_fdr_hat = fc.knockoff_plus_threshold(W, alpha)
        realized = realized_fdr_from_rows(flat, alpha, "knockoff")
        n_adm = len(adm)
        n_false = sum(1 for i in adm if lab[i] == fc.FALSE)
        pt, lo, hi = fc.doc_block_bootstrap(
            per_doc, lambda recs: realized_fdr_from_rows([r for doc in recs for r in doc], alpha, "knockoff"),
            B=B_BOOT, seed=SEED)
        # swap control + plain baseline at matched alpha
        realized_swap = realized_fdr_from_rows(flat, alpha, "swap")
        realized_plain = realized_fdr_from_rows(flat, alpha, "plain")
        _, adm_swap, _ = fc.knockoff_plus_threshold(
            family_arrays(scored_docs, family, "z_swap")[0], alpha)
        _, adm_plain, est_plain = fc.plain_threshold_gate(Z, alpha)
        rows.append({
            "target_alpha": alpha, "realized_fdr": _nan(realized),
            "ci_low": _nan(lo), "ci_high": _nan(hi),
            "n_admitted": n_adm, "n_false": n_false,
            "decoy_fdr_hat": _nan(decoy_fdr_hat) if not math.isinf(decoy_fdr_hat) else None,
            "k_floor": fc.k_floor(alpha),
            "certified": bool(fc.alpha_is_certifiable(n_pos, alpha)),
            "swap_realized_fdr": _nan(realized_swap), "swap_n_admitted": len(adm_swap),
            "plain_realized_fdr": _nan(realized_plain), "plain_n_admitted": len(adm_plain),
            "plain_est_fdr": _nan(est_plain),
        })
    return {"rows": rows, "n_pos": n_pos, "n_total": int(W.size),
            "n_true": int(np.sum(lab == fc.TRUE)), "n_false_total": int(np.sum(lab == fc.FALSE))}


def _nan(x):
    return None if (x is None or (isinstance(x, float) and math.isnan(x))) else round(float(x), 6)


# ----------------------------------------------------------------------------
# Tail diagnostics + control behavior
# ----------------------------------------------------------------------------
def control_behavior(scored_docs, family, alpha=0.30):
    W, Z, lab, zcf = family_arrays(scored_docs, family, "z_cf")
    _, _, _, zswap = family_arrays(scored_docs, family, "z_swap")
    T, adm, _ = fc.knockoff_plus_threshold(W, alpha)
    cut = T if not math.isinf(T) else float(np.percentile(np.maximum(Z, zcf), 50)) if Z.size else 0.5
    wr_cf = fc.tail_win_rate(Z, zcf, cut)
    wr_swap = fc.tail_win_rate(Z, zswap, cut)
    # tail KS / Mann-Whitney: real-FALSE vs decoy scores in the admission tail
    false_scores = Z[(lab == fc.FALSE) & (Z >= cut)]
    cf_tail = zcf[zcf >= cut]
    ks_p = mw_p = None
    try:
        from scipy import stats
        if false_scores.size > 1 and cf_tail.size > 1:
            ks_p = float(stats.ks_2samp(cf_tail, false_scores, alternative="greater").pvalue)
            mw_p = float(stats.mannwhitneyu(cf_tail, false_scores, alternative="less").pvalue)
    except Exception:
        pass
    return {"alpha_used": alpha, "cut": _nan(cut),
            "counterfactual_tail_win_rate": _nan(wr_cf),
            "swap_tail_win_rate": _nan(wr_swap),
            "ks_pvalue_cf_vs_realfalse": ks_p, "mannwhitney_pvalue": mw_p}


def elicitation_tail_aucs(pilot_scores_by_elic):
    out = {}
    for elic, (scores, labels) in pilot_scores_by_elic.items():
        full = fc.auc([s for s, l in zip(scores, labels) if l == fc.TRUE],
                      [s for s, l in zip(scores, labels) if l == fc.FALSE])
        tail = fc.tail_auc(scores, labels, tail_frac=0.5)
        # bootstrap CI for tail-AUC
        rng = np.random.default_rng(SEED)
        boots = []
        s_arr, l_arr = np.array(scores), np.array(labels, dtype=object)
        n = len(scores)
        if n >= 4:
            for _ in range(500):
                idx = rng.integers(0, n, size=n)
                boots.append(fc.tail_auc(s_arr[idx], l_arr[idx], 0.5))
            boots = [b for b in boots if not math.isnan(b)]
        ci = [_nan(np.percentile(boots, 2.5)), _nan(np.percentile(boots, 97.5))] if boots else [None, None]
        out[elic] = {"full_auc": _nan(full), "tail_auc": _nan(tail), "tail_auc_ci": ci,
                     "n_true": int(np.sum(l_arr == fc.TRUE)), "n_false": int(np.sum(l_arr == fc.FALSE))}
    return out


# ----------------------------------------------------------------------------
# Entrapment corroboration (Stage C)
# ----------------------------------------------------------------------------
def entrapment_analysis(scored_docs, family, alpha):
    """At the operative cutoff for `alpha`, compute combined & paired entrapment FDP with
    doc-block CI, vs realized & decoy estimates."""
    W, Z, lab, zcf = family_arrays(scored_docs, family, "z_cf")
    T, adm, decoy_fdr_hat = fc.knockoff_plus_threshold(W, alpha)
    adm_set = set(adm)
    # entrapment items scored; "discovered" if their score would pass the same operative cutoff.
    # Use the knockoff competition for entrapment too: an entrapment is "admitted" if it beats
    # its paired real's decoy structure -> approximate by score >= cut on Z-scale.
    zent, zreal_paired, real_adm_mask, ent_adm_mask = [], [], [], []
    cut = T if not math.isinf(T) else float("inf")
    i = 0
    for d in scored_docs:
        for u in d["units"][family]:
            if "z_real" not in u or "z_ent" not in u:
                continue
            zent.append(u["z_ent"]); zreal_paired.append(u["z_real"])
            real_adm_mask.append(i in adm_set)
            ent_adm_mask.append(u["z_ent"] >= cut if not math.isinf(cut) else False)
            i += 1
    N_T = len(adm)
    N_E = int(np.sum(ent_adm_mask))
    combined = fc.entrapment_fdp(N_T, N_E, r=1.0, estimator="combined")
    pc = fc.paired_entrapment_counts(zreal_paired, zent, real_adm_mask, ent_adm_mask, cut)
    paired = fc.entrapment_fdp(N_T, N_E, r=1.0, estimator="paired", paired_counts=pc)

    # doc-block bootstrap CI for the combined FDP: resample docs, re-run gate+entrapment.
    per_doc = []
    for d in scored_docs:
        rows = [(u["z_real"], u["z_cf"], u.get("z_ent")) for fam in _families(family)
                for u in d["units"][fam] if "z_real" in u]
        per_doc.append(rows)

    def comb_stat(recs):
        flat = [r for doc in recs for r in doc]
        if not flat:
            return float("nan")
        zr = np.array([r[0] for r in flat]); zc = np.array([r[1] for r in flat])
        ze = np.array([(r[2] if r[2] is not None else 0.0) for r in flat])
        Wb = np.array([fc.w_statistic(a, b) for a, b in zip(zr, zc)])
        Tb, admb, _ = fc.knockoff_plus_threshold(Wb, alpha)
        if math.isinf(Tb):
            return float("nan")
        nt = len(admb)
        ne = int(np.sum(ze >= Tb))
        return fc.entrapment_fdp(nt, ne, r=1.0, estimator="combined")

    _, lo, hi = fc.doc_block_bootstrap(per_doc, comb_stat, B=1000, seed=SEED)
    flat_rows = [(u["z_real"], u["z_cf"], u["z_swap"], u.get("z_ent"), u["label"])
                 for d in scored_docs for fam in _families(family) for u in d["units"][fam] if "z_real" in u]
    realized = realized_fdr_from_rows(flat_rows, alpha, "knockoff")
    return {"alpha": alpha, "N_T": N_T, "N_E": N_E, "r": 1,
            "fdp_combined": _nan(combined), "fdp_combined_ci": [_nan(lo), _nan(hi)],
            "fdp_paired": _nan(paired),
            "decoy_fdr_hat": _nan(decoy_fdr_hat) if not math.isinf(decoy_fdr_hat) else None,
            "realized_fdr_gold": _nan(realized),
            "agree_realized": _agree(combined, realized), "agree_decoy": _agree(combined, decoy_fdr_hat),
            "tail_difficulty_ent_median": _nan(float(np.median(zent)) if zent else float("nan")),
            "tail_difficulty_real_median": _nan(float(np.median(zreal_paired)) if zreal_paired else float("nan"))}


def _agree(a, b, tol=0.10):
    if a is None or b is None or (isinstance(a, float) and math.isnan(a)) \
            or (isinstance(b, float) and (math.isnan(b) or math.isinf(b))):
        return None
    return bool(abs(float(a) - float(b)) <= tol)


# ----------------------------------------------------------------------------
# Power analysis + alpha* pre-registration (from pilot)
# ----------------------------------------------------------------------------
def power_table(pilot_scored, family, n_pilot_docs, n_confirm_docs):
    per_doc = per_doc_family_records(pilot_scored, family)
    flat = [r for doc in per_doc for r in doc]
    scale = (n_confirm_docs / max(1, n_pilot_docs))
    W, Z, lab, _ = family_arrays(pilot_scored, family, "z_cf")
    table = []
    for alpha in ALPHA_GRID:
        _, adm, _ = fc.knockoff_plus_threshold(W, alpha)
        n_adm_pilot = len(adm)
        n_false_pilot = sum(1 for i in adm if lab[i] == fc.FALSE)
        proj_adm = int(round(n_adm_pilot * scale))
        proj_false = int(round(n_false_pilot * scale))
        _, lo, hi = fc.doc_block_bootstrap(
            per_doc, lambda recs: realized_fdr_from_rows([r for doc in recs for r in doc], alpha, "knockoff"),
            B=1000, seed=SEED)
        half = (hi - lo) / 2 if not (math.isnan(lo) or math.isnan(hi)) else float("nan")
        table.append({"alpha": alpha, "k_floor": fc.k_floor(alpha),
                      "pilot_admissions": n_adm_pilot, "projected_admissions": proj_adm,
                      "projected_false": proj_false,
                      "clears_floor": proj_adm >= fc.k_floor(alpha),
                      "ci_half_width": _nan(half)})
    # alpha* = most stringent alpha whose floor is projected reachable on the populable family
    reachable = [row["alpha"] for row in table if row["clears_floor"]]
    alpha_star = min(reachable) if reachable else max(ALPHA_GRID)
    return table, alpha_star


# ----------------------------------------------------------------------------
# Output assembly (schema-conformant: examples + rich metadata)
# ----------------------------------------------------------------------------
def build_examples(scored_docs):
    examples = []
    for d in scored_docs:
        for family in ("atomic", "bridge"):
            for u in d["units"][family]:
                if "z_real" not in u:
                    continue
                W = fc.w_statistic(u["z_real"], u["z_cf"])
                inp = json.dumps({"doc_id": d["doc_id"], "family": family,
                                  "fact": pl.fact_nl(**pl._hrt(u["real"]))})
                pred_our = json.dumps({"W": round(W, 4), "z_real": round(u["z_real"], 4),
                                       "z_cf_decoy": round(u["z_cf"], 4)})
                pred_base = json.dumps({"z_real": round(u["z_real"], 4),
                                        "plain_admit_if_conf_ge": "1-alpha"})
                examples.append({
                    "input": inp, "output": u["label"],
                    "predict_our_method": pred_our, "predict_baseline": pred_base,
                    "metadata_doc_id": d["doc_id"], "metadata_family": family,
                    "metadata_k": d["k"], "metadata_is_pilot": d["is_pilot"],
                    "metadata_label": u["label"], "metadata_W": round(W, 4),
                    "metadata_z_real": round(u["z_real"], 4),
                    "metadata_z_cf_decoy": round(u["z_cf"], 4),
                    "metadata_z_swap_decoy": round(u["z_swap"], 4),
                    "metadata_z_entrapment": round(u.get("z_ent", float("nan")), 4)
                        if u.get("z_ent") is not None else None,
                    "metadata_ent_mechanism": u["ent_mech"],
                    "metadata_contaminated_decoy": u["contaminated"],
                })
    return examples


# ----------------------------------------------------------------------------
# Main orchestration
# ----------------------------------------------------------------------------
async def run(scale, concurrency):
    t0 = time.time()
    data_path = WS / "data" / ("mini_data_out.json" if scale == "mini" else "full_data_out.json")
    cost = CostTracker(str(WS / "logs" / "cost_log.jsonl"), soft_cap=3.0, hard_cap=10.0)
    cache = LLMCache(str(WS / "logs" / "llm_cache.jsonl"))

    if scale == "mini":
        pilot_docs = load_docs(data_path, "all")[:3]
        confirm_docs = pilot_docs
    elif scale == "pilot":
        pilot_docs = load_docs(data_path, "pilot")
        confirm_docs = []
    else:  # full
        pilot_docs = load_docs(data_path, "pilot")
        confirm_docs = load_docs(data_path, "confirmatory")
    names_pool = [e["name"] for d in (pilot_docs + confirm_docs) for e in d["entities"]]
    names_pool = list(dict.fromkeys(names_pool))[:200]

    out = {"meta": {"model": MODEL, "seed": SEED, "scale": scale, "alpha_grid": ALPHA_GRID,
                    "tau": TAU, "N_false_min": N_FALSE_MIN, "r": 1, "B": B_BOOT,
                    "n_docs_pilot": len(pilot_docs), "n_docs_confirmatory": len(confirm_docs)}}

    async with LLM(MODEL, cost, cache, concurrency=concurrency) as llm:
        # ---------- runtime probes ----------
        out["meta"]["probes"] = await run_probes(llm)

        # ================= STAGE A : PILOT =================
        # Resumable: load prebuilt units from checkpoint when valid (also avoids Python
        # hash() nondeterminism rebuilding different swap/entrapment triples than the ones
        # the prior LLM scoring calls were cached against).
        pilot_units = load_units_ckpt("pilot_units", len(pilot_docs))
        if pilot_units is None:
            print(f"[STAGE A] building units for {len(pilot_docs)} pilot docs ...")
            pilot_units = await gather_bounded([build_units(llm, d, names_pool) for d in pilot_docs])
            save_ckpt("pilot_units", pilot_units)
        else:
            print(f"[STAGE A] loaded {len(pilot_units)} pilot units from checkpoint")

        # A1 elicitation selection: score pilot REALS with every elicitation -> tail-AUC
        elics = ["logprob_yesno", "verbalized", "self_consistency", "dinco"] \
            if scale != "mini" else ["logprob_yesno", "verbalized"]
        print(f"[STAGE A1] elicitation comparison over {elics} ...")
        pilot_scores_by_elic = await compare_elicitations(llm, pilot_docs, pilot_units, elics)
        tail_aucs = elicitation_tail_aucs(pilot_scores_by_elic)
        selected = select_elicitation(tail_aucs)
        out["meta"]["selected_elicitation"] = selected
        print(f"[STAGE A1] selected elicitation = {selected}; tail-AUCs = "
              f"{ {k: v['tail_auc'] for k, v in tail_aucs.items()} }")

        # A2-A4 full pilot scoring with the selected elicitation (reals + decoys + entrapment)
        print(f"[STAGE A2] scoring pilot units with '{selected}' (reals+decoys+entrapment) ...")
        doc_text = {d["doc_id"]: d["document_text"] for d in pilot_docs}
        pilot_scored = await gather_bounded(
            [score_units(llm, doc_text[u["doc_id"]], u, selected) for u in pilot_units])
        save_ckpt("pilot_scored", pilot_scored)

        primary_family = "bridge"
        power_tbl, alpha_star = power_table(pilot_scored, primary_family,
                                            len(pilot_docs), max(1, len(confirm_docs)))
        ctrl = control_behavior(pilot_scored, primary_family, alpha=0.30)
        pilot_pop = populability(pilot_scored, alpha_star)
        contamination = contamination_rate(pilot_scored)
        out["pilot"] = {
            "elicitation_tail_auc": tail_aucs, "isolated_scoring": "default (provenance-blinded)",
            "control_behavior": ctrl, "populability_pilot": pilot_pop,
            "contamination_rate": contamination, "discard_rate": discard_rate(pilot_units),
            "alpha_star": alpha_star, "populable_family": primary_family,
        }
        out["power_analysis"] = power_tbl
        out["alpha_star"] = alpha_star
        print(f"[STAGE A] alpha* = {alpha_star}; pilot populability = {pilot_pop}")

        # ================= STAGE B : CONFIRMATORY =================
        scored_for_output = pilot_scored
        if confirm_docs:
            confirm_units = load_units_ckpt("confirm_units", len(confirm_docs))
            if confirm_units is None:
                print(f"[STAGE B] building units for {len(confirm_docs)} confirmatory docs ...")
                confirm_units = await gather_bounded([build_units(llm, d, names_pool) for d in confirm_docs])
                save_ckpt("confirm_units", confirm_units)
            else:
                print(f"[STAGE B] loaded {len(confirm_units)} confirmatory units from checkpoint")
            print(f"[STAGE B] scoring confirmatory units with '{selected}' ...")
            ctext = {d["doc_id"]: d["document_text"] for d in confirm_docs}
            confirm_scored = await gather_bounded(
                [score_units(llm, ctext[u["doc_id"]], u, selected) for u in confirm_units])
            save_ckpt("confirm_scored", confirm_scored)
            scored_for_output = confirm_scored
        else:
            confirm_scored = pilot_scored  # pilot/mini: reuse for diagonal demo

        # diagonal for each family
        out["diagonal"] = {fam: diagonal_for_family(confirm_scored, fam)
                           for fam in ("bridge", "atomic", "pooled")}
        out["decoy_control"] = {fam: control_behavior(confirm_scored, fam, alpha=0.30)
                                for fam in ("bridge", "atomic")}
        out["confirmatory_populability"] = populability(confirm_scored, alpha_star)

        # ================= STAGE C : ENTRAPMENT =================
        out["entrapment"] = {str(a): entrapment_analysis(confirm_scored, primary_family, a)
                             for a in [alpha_star, 0.30, 0.50]}

        # ---------- pre-registered disconfirmation ----------
        out["disconfirmation"] = disconfirmation(confirm_scored, primary_family, alpha_star,
                                                  out["confirmatory_populability"])
        out["calibration_verdict"] = calibration_verdict(out["diagonal"]["bridge"],
                                                          out["disconfirmation"])

    out["meta"]["cumulative_cost_usd_this_run"] = round(cost.cumulative, 6)
    out["meta"]["cumulative_cost_usd"] = round(total_spend_from_log(), 6)  # honest grand total (all runs)
    out["meta"]["n_llm_calls_this_run"] = cost.n_calls
    out["meta"]["n_cache_hits_this_run"] = cost.n_cache_hits
    out["meta"]["wall_time_sec"] = round(time.time() - t0, 1)

    # assemble schema-conformant file
    examples = build_examples(scored_for_output)
    result = {"metadata": out,
              "datasets": [{"dataset": "CLUTRR-v1-CrispGold-CalibrationAnchor", "examples": examples}]}
    (WS / "method_out.json").write_text(json.dumps(result, indent=2))
    print(f"[DONE] cost=${cost.cumulative:.4f} calls={cost.n_calls} "
          f"verdict={out['calibration_verdict']} -> method_out.json")
    return result


async def run_probes(llm):
    # logprob probe
    r = await llm.chat([{"role": "system", "content": pl.SCORE_YESNO},
                        {"role": "user", "content": "STORY:\nAna is Bob's mother.\n\nSTATEMENT: Bob is Ana's son\nAnswer Yes or No:"}],
                       kind="probe_logprob", temperature=0.0, max_tokens=16, logprobs=True, top_logprobs=5)
    logprob_ok = len(r["first_token_top_logprobs"]) > 0
    # cache probe (same call twice)
    _ = await llm.chat([{"role": "user", "content": "probe cache: say hi"}], kind="probe_cache",
                       temperature=0.0, max_tokens=16)
    r2 = await llm.chat([{"role": "user", "content": "probe cache: say hi"}], kind="probe_cache",
                        temperature=0.0, max_tokens=16)
    cached = (r2["usage"].get("prompt_tokens_details") or {}).get("cached_tokens", 0)
    return {"logprobs_available": bool(logprob_ok), "cache_hit_tokens": int(cached or 0),
            "logprob_example": r["first_token_top_logprobs"][:3]}


async def compare_elicitations(llm, docs, units, elics):
    """Score the labeled pilot REAL candidates with each elicitation; return
    {elic: (scores[], labels[])} for tail-AUC selection."""
    doc_text = {d["doc_id"]: d["document_text"] for d in docs}
    out = {}
    for elic in elics:
        fn = pl.ELICITATIONS[elic]
        scores, labels = [], []

        async def sc(u_doc, u):
            return await fn(llm, doc_text[u_doc["doc_id"]], u["real"]), u["label"]

        tasks = []
        for u_doc in units:
            for fam in ("atomic", "bridge"):
                for u in u_doc["units"][fam]:
                    tasks.append(sc(u_doc, u))
        res = await gather_bounded([t for t in tasks], batch=concurrency_for(elic))
        for z, lab in res:
            scores.append(z); labels.append(lab)
        out[elic] = (scores, labels)
    return out


def concurrency_for(elic):
    return 24


def select_elicitation(tail_aucs):
    """Pick the best tail-AUC with CI excluding 0.5; prefer a 1-call elicitation unless a
    multi-call one's tail-AUC clearly justifies its cost."""
    one_call = {"logprob_yesno", "verbalized"}
    valid = {}
    for e, v in tail_aucs.items():
        ta = v["tail_auc"]; ci = v["tail_auc_ci"]
        if ta is None:
            continue
        excludes_half = ci[0] is not None and ci[0] > 0.5
        valid[e] = (ta, excludes_half, e in one_call)
    if not valid:
        return "logprob_yesno"
    # best 1-call that excludes 0.5
    best_one = max([e for e in valid if valid[e][2]], key=lambda e: valid[e][0], default=None)
    best_any = max(valid, key=lambda e: valid[e][0])
    if best_one is not None:
        # accept a multi-call winner only if it beats the best 1-call by > 0.05 tail-AUC
        if valid[best_any][0] - valid[best_one][0] > 0.05:
            return best_any
        return best_one
    return best_any


def populability(scored_docs, alpha_star):
    out = {}
    for fam in ("atomic", "bridge"):
        W, Z, lab, _ = family_arrays(scored_docs, fam, "z_cf")
        _, adm, _ = fc.knockoff_plus_threshold(W, alpha_star)
        n_false = sum(1 for i in adm if lab[i] == fc.FALSE)
        # also count at loosest alpha for total available
        _, adm_loose, _ = fc.knockoff_plus_threshold(W, 0.50)
        n_false_loose = sum(1 for i in adm_loose if lab[i] == fc.FALSE)
        out[fam] = {"n_admitted_at_alpha_star": len(adm), "n_false_at_alpha_star": n_false,
                    "n_false_total_in_family": int(np.sum(lab == fc.FALSE)),
                    "n_false_admitted_loosest": n_false_loose}
    pooled_false = out["atomic"]["n_false_total_in_family"] + out["bridge"]["n_false_total_in_family"]
    out["pooled"] = {"n_false_total": pooled_false}
    return out


def contamination_rate(scored_docs):
    n_cont = n_tot = 0
    for d in scored_docs:
        for fam in ("atomic", "bridge"):
            for u in d["units"][fam]:
                n_tot += 1
                n_cont += u.get("contaminated", 0)
    return round(n_cont / n_tot, 4) if n_tot else 0.0


def discard_rate(units):
    seen = disc = 0
    for u in units:
        d = u["discard"]
        seen += d["atomic_seen"] + d["bridge_seen"]
        disc += d["atomic_disc"] + d["bridge_disc"]
    return round(disc / seen, 4) if seen else 0.0


def disconfirmation(scored_docs, family, alpha_star, pop):
    """Single pre-registered disconfirmation at alpha* on the populable family."""
    W, Z, lab, _ = family_arrays(scored_docs, family, "z_cf")
    per_doc = per_doc_family_records(scored_docs, family)
    flat = [r for doc in per_doc for r in doc]
    realized = realized_fdr_from_rows(flat, alpha_star, "knockoff")
    pt, lo, hi = fc.doc_block_bootstrap(
        per_doc, lambda recs: realized_fdr_from_rows([r for doc in recs for r in doc], alpha_star, "knockoff"),
        B=B_BOOT, seed=SEED)
    n_false_total = pop[family]["n_false_total_in_family"]
    if n_false_total < N_FALSE_MIN:
        verdict = "UNTESTABLE"
        reason = (f"populable family '{family}' has only {n_false_total} genuine FALSE candidates "
                  f"(< N_false_min={N_FALSE_MIN}); diagonal precondition unmet (NOT 'confirmed by conservatism').")
    elif realized is not None and not math.isnan(realized) and realized > alpha_star + TAU \
            and lo is not None and not math.isnan(lo) and lo > alpha_star:
        verdict = "DISCONFIRMED"
        reason = (f"realized FDR {realized:.3f} > alpha*+tau ({alpha_star}+{TAU}) AND doc-block "
                  f"CI [{lo:.3f},{hi:.3f}] lies entirely above alpha*={alpha_star}.")
    else:
        verdict = "NOT_DISCONFIRMED"
        reason = (f"realized FDR {realized} with CI [{lo},{hi}] does not exceed alpha*+tau with "
                  f"CI entirely above alpha*={alpha_star}.")
    return {"alpha_star": alpha_star, "family": family, "realized_fdr": _nan(realized),
            "ci": [_nan(lo), _nan(hi)], "tau": TAU, "verdict": verdict, "reason": reason,
            "n_false_total_in_family": n_false_total}


def calibration_verdict(bridge_diag, disconf):
    if disconf["verdict"] == "UNTESTABLE":
        return "UNTESTABLE"
    if disconf["verdict"] == "DISCONFIRMED":
        return "DISCONFIRMED"
    # CONFIRMED iff diagonal tracks within tau above the 1/k floor across certified alphas
    ok = True
    any_cert = False
    for row in bridge_diag["rows"]:
        if not row["certified"]:
            continue
        any_cert = True
        rf = row["realized_fdr"]
        if rf is None:
            continue
        if rf > row["target_alpha"] + TAU:
            ok = False
    return "CONFIRMED" if (any_cert and ok) else "INCONCLUSIVE"


def save_ckpt(name, obj):
    (WS / "checkpoints").mkdir(exist_ok=True)
    (WS / "checkpoints" / f"{name}.json").write_text(json.dumps(obj, default=str))


def load_units_ckpt(name, n_docs):
    """Load a prebuilt *units* checkpoint iff it is structurally complete for this scale
    (a list with exactly n_docs doc-records, each carrying a 'units' block). Returns the
    list or None. Loading (vs rebuilding) guarantees the exact swap/entrapment triples that
    prior scoring calls were cached against are reused -> deterministic, crash-resumable."""
    p = WS / "checkpoints" / f"{name}.json"
    if not p.exists():
        return None
    try:
        obj = json.load(open(p))
    except Exception:
        return None
    if (isinstance(obj, list) and len(obj) == n_docs and n_docs > 0
            and all(isinstance(d, dict) and "units" in d for d in obj)):
        return obj
    return None


def total_spend_from_log():
    """True cumulative LLM spend across ALL runs (sum of non-cache-hit call_cost in the
    persistent cost log). The per-run CostTracker resets to 0 each process; this gives the
    honest grand total since the cache means cached replays are free."""
    p = WS / "logs" / "cost_log.jsonl"
    tot = 0.0
    if not p.exists():
        return 0.0
    with open(p) as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            if not r.get("cache_hit"):
                tot += float(r.get("call_cost", 0.0) or 0.0)
    return tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scale", choices=["mini", "pilot", "full"], default="mini")
    ap.add_argument("--concurrency", type=int, default=12)
    args = ap.parse_args()
    try:
        asyncio.run(run(args.scale, args.concurrency))
    except HardStop as e:
        print(f"[HARDSTOP] {e}")


if __name__ == "__main__":
    main()
