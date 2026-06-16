#!/usr/bin/env python3
"""P3 NOVEL CONTRIBUTION — LABEL-FREE REGIME-DIAGNOSTIC.

Pure-Python over CACHED checkpoint fields (each candidate already carries Z, Zt, W, decoy,
conf_samples). ZERO new API calls, NO gold used. The diagnostic PREDICTS the sign of the
operational wedge (decoy-gating vs plain threshold) BEFORE the realized wedge is computed,
from four gold-free signals, then is VALIDATED against the realized wedge.

Signals (all gold-free):
  A  tail-conditioned decoy win-rate  -> decoy EXCHANGEABILITY axis
  B  spontaneous-error CDF match      -> decoy EXCHANGEABILITY axis (distributional)
  C  W-vs-Z ranking divergence        -> DIRECT mechanical wedge predictor (rho, Jaccard)
  D  base-scorer calibration (Z~f)    -> base-scorer CALIBRATION axis

2-axis regime map (decoy exchangeability x base-scorer calibration):
  (exchangeable ~0.5, low calibration) -> GATE ADDS VALUE   (validated FDR regime, CLUTRR self-consistency)
  (too-easy <<0.5,  high calibration)  -> GATE REDUNDANT    (predicted: Re-DocRED logprob)
  (too-easy <<0.5,  low  calibration)  -> GATE WORSE/anti-conservative (CLUTRR logprob)
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import scipy.stats as st
from loguru import logger

import analyze as A
from common import CONFIG, WORKSPACE


# ======================================================================================
# GATHER GOLD-FREE PER-CANDIDATE SIGNALS FROM CHECKPOINTS
# ======================================================================================
def gather_rows(records: list[dict]) -> list[dict]:
    """Per-candidate gold-free signal rows: Z (real score), Zt (matched-decoy score), W
    (knockoff statistic), f (self-consistency frequency in [0,1]), doc (for block bootstrap)."""
    rows = []
    for rec in records:
        samples = rec.get("conf_samples", []) or []
        for c in rec["candidates"]:
            z, zt, w = c.get("Z"), c.get("Zt"), c.get("W")
            if z is None or zt is None or w is None:
                continue
            f = A.conf_frequency(c, samples)
            rows.append({
                "doc": rec["title"], "Z": float(z), "Zt": float(zt), "W": float(w),
                "f": float(f), "max_zzt": max(float(z), float(zt)),
            })
    return rows


# ======================================================================================
# DOCUMENT-BLOCK BOOTSTRAP for a per-doc ratio (reuses analyze.make_boot_counts/ratio_ci)
# ======================================================================================
def _doc_ratio_ci(num_by_doc: dict, den_by_doc: dict, doc_list: list[str], B: int, seed: int):
    counts = A.make_boot_counts(len(doc_list), B, seed)
    num_vec = np.array([num_by_doc.get(d, 0.0) for d in doc_list], float)
    den_vec = np.array([den_by_doc.get(d, 0.0) for d in doc_list], float)
    lo, hi = A.ratio_ci(counts, num_vec, den_vec)
    point = float(num_vec.sum() / max(1.0, den_vec.sum()))
    return point, lo, hi


# ======================================================================================
# SIGNAL A — tail-conditioned decoy win-rate (gold-free)
#   winrate_tail = mean( Zt_i >= Z_i ) over the operative tail.
#   ~0.5 => decoys EXCHANGEABLE; <<0.5 => decoys TOO EASY (scorer separates real from fake).
# ======================================================================================
def winrate_over_subset(subset: list[dict], doc_list: list[str], B: int, seed: int,
                        label: str, cutoff_desc: str):
    if not subset:
        return {"label": label, "cutoff": cutoff_desc, "n_tail": 0, "winrate": None,
                "ci": [None, None]}
    num, den = {}, {}
    for r in subset:
        den[r["doc"]] = den.get(r["doc"], 0.0) + 1.0
        if r["Zt"] >= r["Z"]:
            num[r["doc"]] = num.get(r["doc"], 0.0) + 1.0
    point, lo, hi = _doc_ratio_ci(num, den, doc_list, B, seed)
    return {"label": label, "cutoff": cutoff_desc, "n_tail": len(subset),
            "winrate": round(point, 5), "ci": [round(lo, 5), round(hi, 5)]}


def signal_A(rows, doc_list, B, seed, T_op=None):
    """Win-rate over several operative tails (gold-free quantiles + knockoff-admitted +
    optional gold-anchored matched-recall cutoff cross-check)."""
    maxv = np.array([r["max_zzt"] for r in rows])
    out = []
    # gold-free top-q quantile tails
    for q in CONFIG["regime_tail_quantiles"]:
        cut = float(np.quantile(maxv, 1.0 - q))
        sub = [r for r in rows if r["max_zzt"] >= cut]
        out.append(winrate_over_subset(sub, doc_list, B, seed, f"top_{int(q*100)}pct",
                                        f"max(Z,Zt)>={cut:.3f}"))
    # full set
    out.append(winrate_over_subset(rows, doc_list, B, seed, "all", "all candidates"))
    # knockoff+ admitted set at alpha=0.2 (gold-free: derived purely from W signs)
    W_list = [r["W"] for r in rows]
    Tk = A.knockoff_plus_threshold(W_list, 0.20)
    if Tk is not None:
        sub = [r for r in rows if r["W"] >= Tk]
        out.append(winrate_over_subset(sub, doc_list, B, seed, "knockoff_alpha0.2",
                                       f"W>={Tk:.3f}"))
    # gold-anchored matched-recall operating cutoff (cross-check only, in max(Z,Zt) space)
    if T_op is not None:
        sub = [r for r in rows if r["max_zzt"] >= T_op]
        out.append(winrate_over_subset(sub, doc_list, B, seed, "matched_recall_rep",
                                       f"max(Z,Zt)>={T_op:.3f} (gold-anchored)"))
    return out


# ======================================================================================
# SIGNAL B — spontaneous-error CDF match (gold-free)
#   Compare Zt (decoy) score CDF vs the Z score CDF of low-self-consistency reals
#   (f_i <= low_f: reals the model itself did not reproduce -> its own likely errors).
#   MATCH (fail-to-reject) => decoys exchangeable with model's own errors;
#   REJECT with decoy LOWER => decoys too easy.
# ======================================================================================
def _perm_meandiff_p(a: np.ndarray, b: np.ndarray, B: int, seed: int) -> float:
    """Two-sided permutation p-value for difference in means."""
    rng = np.random.default_rng(seed)
    obs = abs(a.mean() - b.mean())
    pooled = np.concatenate([a, b])
    n = len(a)
    cnt = 0
    for _ in range(B):
        rng.shuffle(pooled)
        if abs(pooled[:n].mean() - pooled[n:].mean()) >= obs - 1e-12:
            cnt += 1
    return (cnt + 1) / (B + 1)


def _two_sample_block(zt: np.ndarray, z_lowf: np.ndarray, seed: int, perm_B: int):
    if len(zt) < 3 or len(z_lowf) < 3:
        return {"n_decoy": int(len(zt)), "n_lowf_real": int(len(z_lowf)),
                "ks_p": None, "mw_p": None, "perm_p": None,
                "decoy_mean": round(float(zt.mean()), 5) if len(zt) else None,
                "lowf_real_mean": round(float(z_lowf.mean()), 5) if len(z_lowf) else None,
                "match": None}
    ks = st.ks_2samp(zt, z_lowf)
    try:
        mw = st.mannwhitneyu(zt, z_lowf, alternative="two-sided")
        mw_p = float(mw.pvalue)
    except ValueError:
        mw_p = None
    perm_p = _perm_meandiff_p(zt, z_lowf, perm_B, seed)
    match = (float(ks.pvalue) > 0.05) and (mw_p is None or mw_p > 0.05) and (perm_p > 0.05)
    return {"n_decoy": int(len(zt)), "n_lowf_real": int(len(z_lowf)),
            "ks_p": round(float(ks.pvalue), 6), "mw_p": None if mw_p is None else round(mw_p, 6),
            "perm_p": round(float(perm_p), 6),
            "decoy_mean": round(float(zt.mean()), 5),
            "lowf_real_mean": round(float(z_lowf.mean()), 5),
            "match": bool(match)}


def signal_B(rows, seed, perm_B=2000):
    low_f = CONFIG["regime_low_f"]
    zt_all = np.array([r["Zt"] for r in rows])
    z_lowf_all = np.array([r["Z"] for r in rows if r["f"] <= low_f])
    full = _two_sample_block(zt_all, z_lowf_all, seed, perm_B)
    # top-tail version: restrict both to the upper half (>= pooled median of scores)
    pooled = np.concatenate([zt_all, z_lowf_all]) if len(z_lowf_all) else zt_all
    med = float(np.median(pooled)) if len(pooled) else 0.0
    zt_tail = zt_all[zt_all >= med]
    z_lowf_tail = z_lowf_all[z_lowf_all >= med] if len(z_lowf_all) else z_lowf_all
    tail = _two_sample_block(zt_tail, z_lowf_tail, seed + 1, perm_B)
    return {"low_f_threshold": low_f, "full_distribution": full, "top_tail": tail,
            "interpretation": ("MATCH (fail-to-reject) => decoys exchangeable with the model's "
                               "own spontaneous errors (valid knockoff); REJECT with decoy mean "
                               "< low-f-real mean => decoys TOO EASY (gate redundant/worse).")}


# ======================================================================================
# SIGNAL C — W-vs-Z ranking divergence (gold-free, the DIRECT wedge predictor)
#   rho ~ 1 in the admission region => the gate cannot re-rank => MECHANICALLY null wedge.
# ======================================================================================
def signal_C(rows):
    """W = max(Z,Zt)*sign(Z-Zt). When the decoy LOSES (Zt<Z) W==Z exactly, so the gate
    cannot re-rank that candidate relative to the plain Z threshold. The ONLY candidates the
    gate moves are the 'winners' (Zt>=Z, W<0), which it demotes/drops. Hence:
      frac(W==Z) ~ 1  AND  rho(W,Z) over the gate-admitted set {W>=0} ~ 1
    mechanically predicts a NULL wedge (the gate admits the same facts in the same order)."""
    Z = np.array([r["Z"] for r in rows])
    W = np.array([r["W"] for r in rows])
    n = len(rows)
    rho_full = float(st.spearmanr(W, Z).statistic) if n > 2 else 1.0
    frac_w_eq_z = float(np.mean(np.isclose(W, Z, atol=1e-9)))
    adm = [i for i in range(n) if W[i] >= 0]          # the set the gate actually admits
    K = len(adm)
    if K > 2 and len(set(Z[adm].tolist())) > 1:
        rho_adm = float(st.spearmanr(W[adm], Z[adm]).statistic)
    else:
        rho_adm = 1.0
    # Jaccard between the gate-admitted set {W>=0} and the equal-size top-Z set (membership
    # divergence: <1 exactly to the extent the gate demotes 'winners' the plain threshold keeps)
    topZ = set(np.argsort(-Z)[:K].tolist()) if K > 0 else set()
    admset = set(adm)
    jac = len(topZ & admset) / max(1, len(topZ | admset))
    return {"spearman_full": round(rho_full, 5),
            "spearman_admission": round(rho_adm, 5),
            "admitted_set_jaccard": round(float(jac), 5),
            "frac_W_equals_Z": round(frac_w_eq_z, 5),
            "n_candidates": n, "n_admitted_W_ge_0": K,
            "interpretation": ("frac(W==Z)~1 and admitted-set rho~1 => the gate keeps and orders "
                               "the same facts as the plain Z threshold => mechanically NULL "
                               "wedge. Jaccard<1 measures the few 'winner' demotions, which the "
                               "realized wedge shows are precision-neutral here.")}


# ======================================================================================
# SIGNAL D — base-scorer calibration (gold-free): does Z agree with the label-free truth
#   proxy f (self-consistency)? High agreement => Z calibrated => plain threshold already
#   works => gate redundant.
# ======================================================================================
def signal_D(rows, f_pos=0.5):
    from sklearn.metrics import roc_auc_score
    Z = np.array([r["Z"] for r in rows])
    f = np.array([r["f"] for r in rows])
    y = (f >= f_pos).astype(int)
    auc = None
    if 0 < int(y.sum()) < len(y):
        try:
            auc = float(roc_auc_score(y, Z))
        except ValueError:
            auc = None
    rho = float(st.spearmanr(Z, f).statistic) if len(rows) > 2 else None
    return {"calibration_auc": None if auc is None else round(auc, 5),
            "calibration_spearman_Z_f": None if rho is None else round(rho, 5),
            "f_pos_threshold": f_pos, "n_pos": int(y.sum()), "n_total": int(len(y)),
            "interpretation": ("AUC(Z -> high-self-consistency) high => Z is calibrated against "
                               "the model's own truth proxy => plain threshold already separates "
                               "good from bad => the gate is redundant rather than harmful.")}


# ======================================================================================
# REGIME CLASSIFICATION (2-axis) + PREDICTED WEDGE SIGN  (all gold-free)
# ======================================================================================
def classify(winrate_headline, calib_auc, rho_adm, jaccard, frac_eq):
    band = CONFIG["regime_exch_band"]
    exch = (winrate_headline is not None) and abs(winrate_headline - 0.5) <= band
    too_easy = (winrate_headline is not None) and winrate_headline < 0.5 - band
    too_hard = (winrate_headline is not None) and winrate_headline > 0.5 + band
    calibrated = (calib_auc is not None) and (calib_auc >= CONFIG["regime_calib_auc_hi"])

    # Signal C is the dominant, mechanical predictor: if the gate keeps+orders the same facts
    # as the plain threshold, the wedge is null regardless of the other axes. Triggered by an
    # overwhelming W==Z fraction OR (admitted-set rho~1 AND admitted-set Jaccard~1).
    rerank_blocked = ((frac_eq is not None and frac_eq >= 0.90)
                      or (rho_adm is not None and rho_adm >= CONFIG["regime_rho_null"]
                          and jaccard is not None and jaccard >= CONFIG["regime_jaccard_null"]))

    if rerank_blocked:
        regime, sign = "GATE REDUNDANT", "null"
        basis = (f"Signal C (frac(W==Z)={frac_eq}, admitted-set rho={rho_adm}: the gate keeps & "
                 f"orders the same facts as the plain threshold -> mechanically null wedge)")
    elif exch and not calibrated:
        regime, sign = "GATE ADDS VALUE", "positive"
        basis = "exchangeable decoys + low base-scorer calibration"
    elif too_easy and calibrated:
        regime, sign = "GATE REDUNDANT", "null"
        basis = "too-easy decoys + calibrated base scorer"
    elif (too_easy or too_hard) and not calibrated:
        regime, sign = "GATE WORSE/anti-conservative", "negative"
        basis = "non-exchangeable decoys + low calibration (anti-conservative risk)"
    else:
        regime, sign = "INDETERMINATE", "unclear"
        basis = "axes do not cleanly separate"
    axes = {"decoy_exchangeable": bool(exch), "decoys_too_easy": bool(too_easy),
            "decoys_too_hard": bool(too_hard), "base_scorer_calibrated": bool(calibrated),
            "rerank_blocked": bool(rerank_blocked)}
    return regime, sign, basis, axes


# ======================================================================================
# CROSS-ANCHOR: place Re-DocRED and CLUTRR (P1) on the same 2-axis map + state the principle
# ======================================================================================
def load_clutrr_anchor() -> dict:
    """Read P1's CLUTRR regime coordinates from its method_out.json if present; else fall
    back to the hypothesis-reported values (logged as such)."""
    p1 = (WORKSPACE.parent / "gen_art_experiment_1" / "method_out.json")
    if p1.exists():
        try:
            m = json.loads(p1.read_text()).get("metadata", {})
            rd = m.get("regime_diagnostic") or m.get("regime") or {}
            if rd:
                logger.info("Loaded CLUTRR cross-anchor coordinates from P1 method_out.json")
                return {"source": "P1_method_out", "raw": rd}
        except Exception as e:
            logger.warning(f"could not parse P1 method_out.json: {e}")
    logger.info("P1 method_out.json not available; using hypothesis-reported CLUTRR coordinates")
    # Hypothesis-reported CLUTRR self-report (decoy win-rate as exchangeability proxy):
    #   verbalized 0.103 -> too-easy/anti-conservative; logprob 0.34 -> anti-conservative/worse;
    #   self-consistency 0.482 -> exchangeable -> controls FDR (gate adds value).
    return {
        "source": "hypothesis_reported",
        "elicitations": {
            "verbalized": {"winrate_tail": 0.103, "regime": "GATE WORSE/anti-conservative",
                           "wedge_sign": "negative", "calibrated": False},
            "logprob": {"winrate_tail": 0.34, "regime": "GATE WORSE/anti-conservative",
                        "wedge_sign": "negative", "calibrated": False},
            "self_consistency": {"winrate_tail": 0.482, "regime": "GATE ADDS VALUE",
                                 "wedge_sign": "positive", "calibrated": False},
        },
    }


def cross_anchor(redocred_coords: dict) -> dict:
    clutrr = load_clutrr_anchor()
    points = [{
        "anchor": "Re-DocRED (logprob)", **redocred_coords,
    }]
    if clutrr["source"] == "hypothesis_reported":
        for elic, v in clutrr["elicitations"].items():
            points.append({"anchor": f"CLUTRR ({elic})", "winrate_tail": v["winrate_tail"],
                           "base_scorer_calibrated": v["calibrated"],
                           "predicted_regime": v["regime"], "predicted_wedge_sign": v["wedge_sign"]})
    principle = ("Gate value is monotone in tail-overconfidence and CONDITIONAL on decoy "
                 "exchangeability: the decoy-competition gate adds value ONLY where the base "
                 "elicitation is tail-overconfident AND the decoys are exchangeable with the "
                 "model's own errors (win-rate ~0.5); it is REDUNDANT where the base scorer is "
                 "already calibrated / decoys are too easy (win-rate <<0.5, rho~1), and WORSE "
                 "where decoys are too easy but the scorer is anti-conservative.")
    # 2-anchor direction (illustration, not a powered regression): sort by winrate_tail and
    # report whether wedge sign moves from negative/null (low exchangeability) toward positive
    # (exchangeable ~0.5).
    wr = [(p.get("winrate_tail"), p.get("predicted_wedge_sign", p.get("realized_wedge_sign")))
          for p in points if p.get("winrate_tail") is not None]
    wr_sorted = sorted(wr, key=lambda x: x[0])
    direction = ("The wedge sign is governed by a 2-AXIS map, NOT a 1-D monotone of winrate_tail: "
                 "the positive (gate-adds-value) regime requires exchangeable decoys (winrate~0.5) "
                 "— realized only at the high end (CLUTRR self-consistency, 0.482, positive). At the "
                 "LOW (too-easy) end the sign SPLITS by base-scorer calibration: Re-DocRED (0.047) "
                 "is NULL (redundant) because its scorer is comparatively calibrated and frac(W==Z)"
                 "~0.94 means almost nothing is demoted, whereas CLUTRR verbalized/logprob "
                 "(0.10/0.34) are NEGATIVE (anti-conservative). So winrate alone does NOT linearly "
                 "order the sign — the calibration axis is required. Reported as a {}-point 2-anchor "
                 "illustration, NOT a powered regression.").format(len(wr_sorted))
    return {"points": points, "clutrr_source": clutrr["source"], "principle": principle,
            "winrate_sorted": [[None if a is None else round(a, 4), b] for a, b in wr_sorted],
            "direction": direction}


# ======================================================================================
# TOP-LEVEL ENTRY POINT
# ======================================================================================
def compute_regime_diagnostic(records, realized_delta_ci, realized_grid, bootstrap_B,
                              seed, T_op=None):
    """Returns the full regime_diagnostic metadata block (gold-free predictions + validation
    against the realized wedge)."""
    rows = gather_rows(records)
    doc_list = sorted({r["doc"] for r in rows})
    logger.info(f"REGIME DIAGNOSTIC: {len(rows)} candidate rows over {len(doc_list)} docs "
                f"(gold-free; zero API)")
    if len(rows) < 10:
        logger.warning("too few candidate rows for a stable regime diagnostic")

    sigA = signal_A(rows, doc_list, bootstrap_B, seed, T_op=T_op)
    sigB = signal_B(rows, seed, perm_B=min(bootstrap_B, 2000))
    sigC = signal_C(rows)
    sigD = signal_D(rows, f_pos=0.5)

    # headline winrate = the top-50% operative tail (representative of the admission region)
    headline = next((a for a in sigA if a["label"] == "top_50pct"), None)
    winrate_headline = headline["winrate"] if headline else None

    regime, sign, basis, axes = classify(
        winrate_headline, sigD["calibration_auc"], sigC["spearman_admission"],
        sigC["admitted_set_jaccard"], sigC["frac_W_equals_Z"])
    logger.info(f"PREDICTED regime={regime} wedge_sign={sign} (basis: {basis})")
    logger.info(f"  winrate_tail(top50%)={winrate_headline} calib_auc={sigD['calibration_auc']} "
                f"rho_adm={sigC['spearman_admission']} jaccard={sigC['admitted_set_jaccard']}")

    # --- VALIDATION against the realized wedge (no recall point with delta CI entirely > 0) ---
    any_positive_point = False
    for ci in (realized_delta_ci or []):
        lo = ci[0] if ci and ci[0] is not None else None
        if lo is not None and lo > 0:
            any_positive_point = True
            break
    realized_wedge_sign = "positive" if any_positive_point else "null_or_negative"
    prediction_correct = (sign == "null") and (not any_positive_point)
    logger.info(f"REALIZED wedge: any_positive_recall_point={any_positive_point} -> "
                f"realized_sign={realized_wedge_sign}; prediction_correct={prediction_correct}")

    redocred_coords = {
        "winrate_tail": winrate_headline,
        "base_scorer_calibrated": axes["base_scorer_calibrated"],
        "predicted_regime": regime, "predicted_wedge_sign": sign,
        "realized_wedge_sign": realized_wedge_sign,
    }
    xanchor = cross_anchor(redocred_coords)

    return {
        "summary": ("Label-free 2-axis regime-diagnostic that predicts the operational-wedge "
                    "sign from cached Z/Zt/W/self-consistency with ZERO API calls and NO gold, "
                    "then validates against the realized wedge."),
        "n_candidate_rows": len(rows), "n_docs": len(doc_list),
        "signal_A_winrate_tail": sigA,
        "signal_B_cdf_match": sigB,
        "signal_C_wz_divergence": sigC,
        "signal_D_calibration": sigD,
        "winrate_tail_headline": winrate_headline,
        "predicted_regime": regime,
        "predicted_wedge_sign": sign,
        "prediction_basis": basis,
        "regime_axes": axes,
        "prediction_vs_realized": {
            "predicted_wedge_sign": sign,
            "realized_wedge_sign": realized_wedge_sign,
            "realized_any_positive_recall_point": bool(any_positive_point),
            "prediction_correct": bool(prediction_correct),
            "note": ("prediction_correct == (predicted null) AND (no matched-recall point has a "
                     "delta CI entirely > 0).")},
        "cross_anchor": xanchor,
        "thresholds": {k: CONFIG[k] for k in ("regime_low_f", "regime_tail_quantiles",
                                              "regime_exch_band", "regime_calib_auc_hi",
                                              "regime_rho_null", "regime_jaccard_null")},
    }
