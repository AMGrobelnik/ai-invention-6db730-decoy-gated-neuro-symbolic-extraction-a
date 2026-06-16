"""
fdr_core.py
===========
Pure, API-free mathematical core for the label-free decoy-competition FDR gate.

Implements, with verbatim fidelity to SPEC1 (art_SLUbUUr6Ul98):
  * the CANONICAL knockoff competition statistic  W_i = sign(Z_i - Z~_i) * max(Z_i, Z~_i)
  * the knockoff+ data-dependent admission threshold (Barber-Candes eq. 1.9, with the +1)
  * the 1/k minimum-estimable-FDR floor  (need k >= ceil(1/alpha) admissions)
  * the four entrapment FDP estimators (Wen et al. 2025): lower / combined / paired / sample(invalid)
  * the document-block (cluster) bootstrap for FDP/FDR confidence intervals
  * crisp CLUTRR gold labelling (TRUE / FALSE / UNJUDGEABLE)
  * the PLAIN confidence-threshold baseline gate (the primary, decoy-free foil)
  * tail diagnostics (tail-conditioned win-rate, tail-restricted AUC, one-sided KS / Mann-Whitney)

Every function here is deterministic and unit-tested in tests.py with hand-computed answers.
No network, no I/O, no global state.
"""
from __future__ import annotations

import math
from typing import Callable, Sequence

import numpy as np

# ----------------------------------------------------------------------------
# Labels
# ----------------------------------------------------------------------------
TRUE = "TRUE"
FALSE = "FALSE"
UNJUDGEABLE = "UNJUDGEABLE"


# ============================================================================
# MODULE 5 -- the canonical competition statistic + knockoff+ gate (SPEC1 A)
# ============================================================================
def w_statistic(z_real: float, z_decoy: float) -> float:
    """CANONICAL signed magnitude-max competition statistic (SPEC1 A, SPEC2 Sec 0):

        W_i = sign(Z_i - Z~_i) * max(Z_i, Z~_i)

    A large positive W => the real candidate beat its matched decoy with a high score
    (evidence of a true signal). Ties (Z_i == Z~_i) give sign 0 -> W = 0 (no evidence;
    never admitted at a positive cutoff). This is the iter-1 fix: the per-pair difference
    d_i = Z_i - Z~_i is a TAIL DIAGNOSTIC only and is NEVER passed to the gate.
    """
    zr, zd = float(z_real), float(z_decoy)
    s = (zr > zd) - (zr < zd)  # sign in {-1,0,+1}
    return float(s) * max(zr, zd)


def knockoff_plus_threshold(W: Sequence[float], alpha: float):
    """knockoff+ admission threshold (Barber-Candes Definition 2, eq. 1.9; controls FDR exactly).

        T = min { t in {|W_i|} : (1 + #{i: W_i <= -t}) / (#{i: W_i >= t} v 1) <= alpha }
        admitted set  Shat = { i : W_i >= T }

    The +1 in the numerator is kept (Rajchert-Keich prove it is in general necessary).
    Scans candidate cutoffs over the ascending distinct POSITIVE |W| magnitudes and returns
    the smallest feasible t (the most permissive admission).

    Returns (T, admitted_indices(sorted list), fdr_hat). If no feasible cutoff: (inf, [], 1.0).
    """
    W = np.asarray(W, dtype=float)
    n = W.size
    if n == 0:
        return math.inf, [], 1.0
    cand = np.unique(np.abs(W))
    cand = cand[cand > 0.0]  # positive magnitudes only (|W|=0 candidates are never selected)
    if cand.size == 0:
        return math.inf, [], 1.0
    for t in cand:  # ascending => smallest feasible t first => most permissive
        pos = int(np.sum(W >= t))
        neg = int(np.sum(W <= -t))
        fdr_hat = (1 + neg) / max(1, pos)
        if fdr_hat <= alpha:
            admitted = sorted(int(i) for i in np.where(W >= t)[0])
            return float(t), admitted, float(fdr_hat)
    return math.inf, [], 1.0


def k_floor(alpha: float) -> int:
    """Minimum admissions needed to certify FDR<=alpha (the 1/k floor): k >= ceil(1/alpha)."""
    return int(math.ceil(1.0 / alpha))


def alpha_is_certifiable(n_max_admissible: int, alpha: float) -> bool:
    """An alpha is structurally demonstrable only if the maximum attainable #admissions
    can reach its k-floor ceil(1/alpha). Otherwise the alpha is precondition-unmet (NOT
    'confirmed by conservatism')."""
    return n_max_admissible >= k_floor(alpha)


# ============================================================================
# PLAIN confidence-threshold baseline gate (decoy-free primary foil; SPEC2 Block E)
# ============================================================================
def plain_threshold_gate(Z: Sequence[float], alpha: float):
    """Decoy-free label-free baseline: admit the most-confident candidates until the
    *self-estimated* FDR of the admitted set (1 - mean admitted confidence) would exceed
    alpha. This is the standard 'raw LLM confidence' gate the decoy method is compared
    against -- it has NO null calibration, so its self-estimate is expected to be
    anti-conservative (overconfident) relative to the realized FDR against gold.

    Returns (threshold, admitted_indices, est_fdr_of_admitted).
    """
    Z = np.asarray(Z, dtype=float)
    n = Z.size
    if n == 0:
        return math.inf, [], 1.0
    order = np.argsort(-Z, kind="stable")  # descending confidence
    zsorted = Z[order]
    cumsum = np.cumsum(zsorted)
    best_k = 0
    best_est = 1.0
    for k in range(1, n + 1):
        est_fdr = 1.0 - cumsum[k - 1] / k  # 1 - mean confidence of the top-k admitted
        if est_fdr <= alpha:
            best_k = k
            best_est = est_fdr
    if best_k == 0:
        return math.inf, [], 1.0
    threshold = float(zsorted[best_k - 1])
    admitted = sorted(int(i) for i in order[:best_k])
    return threshold, admitted, float(best_est)


# ============================================================================
# MODULE 6 -- entrapment FDP estimators (Wen et al. 2025; SPEC1 B)
# ============================================================================
def entrapment_fdp(N_T: int, N_E: int, r: float, estimator: str = "combined",
                   paired_counts: dict | None = None) -> float:
    """Entrapment-based FDP estimators (verbatim eq. numbers from SPEC1 B):

        lower    (eq.2)  = N_E / (N_T + N_E)                          # failure-only lower bound
        combined (eq.1)  = N_E * (1 + 1/r) / (N_T + N_E)             # DEFAULT upper bound
        paired   (eq.4)  = (N_E + N_{E>=s>T} + 2 N_{E>T>=s}) / (N_T + N_E)   # tighter, requires r==1
        sample   (eq.3)  = INVALID (biased) -> raises

    paired_counts (for 'paired'): {'E_ge_s_gt_T': int, 'E_gt_T_ge_s': int}.
    """
    denom = max(1, N_T + N_E)
    if estimator == "lower":
        return N_E / denom
    if estimator == "combined":
        return N_E * (1.0 + 1.0 / r) / denom
    if estimator == "sample":
        raise ValueError("entrapment 'sample' estimator (eq.3) is INVALID/biased -- never use it")
    if estimator == "paired":
        if abs(r - 1.0) > 1e-9:
            raise ValueError("paired entrapment estimator requires r == 1")
        if paired_counts is None:
            raise ValueError("paired estimator requires paired_counts")
        n_egt = int(paired_counts.get("E_ge_s_gt_T", 0))
        n_egtt = int(paired_counts.get("E_gt_T_ge_s", 0))
        return (N_E + n_egt + 2 * n_egtt) / denom
    raise ValueError(f"unknown estimator: {estimator}")


def paired_entrapment_counts(real_scores, entrapment_scores, admitted_mask_real,
                             admitted_mask_ent, s_cut: float):
    """Compute the paired-estimator auxiliary counts (eq.4) for one-to-one (r=1) pairing.

    For each (real_i, entrapment_i) pair, with operative discovery cutoff score s:
      N_E            = # entrapment items discovered (admitted)
      N_{E>=s>T}     = # discovered entrapment whose PAIRED real scored < s (real not discovered)
      N_{E>T>=s}     = # discovered entrapment whose paired real scored LOWER but is ALSO discovered
    Here 'score' is the per-item scalar Z and s_cut is the score threshold that defines discovery.
    """
    real_scores = np.asarray(real_scores, float)
    ent_scores = np.asarray(ent := entrapment_scores, float)
    am_real = np.asarray(admitted_mask_real, bool)
    am_ent = np.asarray(admitted_mask_ent, bool)
    N_E = int(np.sum(am_ent))
    n_egt = 0
    n_egtt = 0
    for i in range(len(ent_scores)):
        if not am_ent[i]:
            continue
        if not am_real[i]:
            # paired real NOT discovered (real score < s)
            n_egt += 1
        else:
            # paired real discovered too; "scored lower but still discovered"
            if ent_scores[i] > real_scores[i]:
                n_egtt += 1
    return {"E_ge_s_gt_T": n_egt, "E_gt_T_ge_s": n_egtt, "N_E": N_E}


# ============================================================================
# Crisp CLUTRR gold labelling (MODULE 0)
# ============================================================================
def gold_label(candidate: tuple, gold_true: set, covered_pairs: set) -> str:
    """Crisp gold label for an extracted candidate (h, r, t):

        TRUE         if (h,r,t) is a directly-stated atomic OR proof-path-derived bridge fact
        FALSE        if (h,t) is a COVERED pair (appears in gold) but the relation is wrong
                     (a genuine hallucination -- wrong relation on a known pair)
        UNJUDGEABLE  if (h,t) is not on any proof path -> excluded from the FDR pool (logged)

    Relations are compared lowercased; names exactly. This preserves CLUTRR crispness with
    NO homegrown rule reimplementation.
    """
    h, r, t = candidate
    key = (h, r.lower(), t)
    if key in gold_true:
        return TRUE
    if (h, t) in covered_pairs:
        return FALSE
    return UNJUDGEABLE


# ============================================================================
# MODULE 7 -- document-block (cluster) bootstrap (SPEC1 C)
# ============================================================================
def doc_block_bootstrap(per_doc_records: list, statistic_fn: Callable, B: int = 2000,
                        seed: int = 20240617, lo_pct: float = 2.5, hi_pct: float = 97.5):
    """Resample WHOLE documents with replacement (preserving within-doc dependence),
    re-run the statistic on each resample, return (point, lo, hi) percentile CI.

    per_doc_records : list (one element per document; any structure statistic_fn understands)
    statistic_fn    : maps a list-of-doc-records -> float (re-runs the WHOLE gate+stat)
    """
    rng = np.random.default_rng(seed)
    D = len(per_doc_records)
    point = float(statistic_fn(per_doc_records))
    if D == 0:
        return point, float("nan"), float("nan")
    stats = np.empty(B, dtype=float)
    for b in range(B):
        idx = rng.integers(0, D, size=D)
        boot = [per_doc_records[i] for i in idx]
        stats[b] = statistic_fn(boot)
    stats = stats[~np.isnan(stats)]
    if stats.size == 0:
        return point, float("nan"), float("nan")
    lo = float(np.percentile(stats, lo_pct))
    hi = float(np.percentile(stats, hi_pct))
    return point, lo, hi


# ============================================================================
# MODULE 4/D.4 -- tail diagnostics (measurement only; NEVER consumed by the gate)
# ============================================================================
def auc(scores_pos: Sequence[float], scores_neg: Sequence[float]) -> float:
    """AUC = P(score_pos > score_neg) via the Mann-Whitney U statistic (ties -> 0.5).
    Returns NaN if either class is empty."""
    p = np.asarray(scores_pos, float)
    n = np.asarray(scores_neg, float)
    if p.size == 0 or n.size == 0:
        return float("nan")
    # rank-based U; equivalent to mean over all pairs of [pos>neg] + 0.5[pos==neg]
    allv = np.concatenate([p, n])
    order = np.argsort(allv, kind="stable")
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, allv.size + 1)
    # average ranks for ties
    _assign_tie_ranks(allv, ranks)
    r_pos = ranks[: p.size].sum()
    u_pos = r_pos - p.size * (p.size + 1) / 2.0
    return float(u_pos / (p.size * n.size))


def _assign_tie_ranks(values: np.ndarray, ranks: np.ndarray) -> None:
    """In-place average-rank assignment for ties."""
    order = np.argsort(values, kind="stable")
    sv = values[order]
    i = 0
    n = sv.size
    while i < n:
        j = i
        while j + 1 < n and sv[j + 1] == sv[i]:
            j += 1
        if j > i:
            avg = (i + 1 + j + 1) / 2.0  # average of 1-based ranks
            for k in range(i, j + 1):
                ranks[order[k]] = avg
        else:
            ranks[order[i]] = i + 1
        i = j + 1


def tail_auc(scores: Sequence[float], labels: Sequence[str], tail_frac: float = 0.5) -> float:
    """AUC of TRUE vs FALSE restricted to the upper (admission) tail = the top `tail_frac`
    of items by score. Requires both classes present in the tail; else NaN."""
    s = np.asarray(scores, float)
    lab = np.asarray(labels, dtype=object)
    if s.size == 0:
        return float("nan")
    k = max(1, int(math.ceil(tail_frac * s.size)))
    tail_idx = np.argsort(-s, kind="stable")[:k]
    s_t = s[tail_idx]
    lab_t = lab[tail_idx]
    pos = s_t[lab_t == TRUE]
    neg = s_t[lab_t == FALSE]
    return auc(pos, neg)


def tail_win_rate(z_real: Sequence[float], z_decoy: Sequence[float], cut: float) -> float:
    """Tail-conditioned win-rate of the DECOY over its matched real, among pairs whose
    max(Z_real, Z_decoy) >= cut. For counterfactual decoys this should be ~0.5 (fair coin);
    for too-easy swap decoys it should be measurably < 0.5. Returns NaN if tail empty."""
    zr = np.asarray(z_real, float)
    zd = np.asarray(z_decoy, float)
    m = np.maximum(zr, zd)
    sel = m >= cut
    if not np.any(sel):
        return float("nan")
    zr_s, zd_s = zr[sel], zd[sel]
    wins = np.sum(zd_s > zr_s) + 0.5 * np.sum(zd_s == zr_s)
    return float(wins / sel.sum())
