#!/usr/bin/env python3
"""
fdr_stats.py — Offline statistical primitives for the decoy-competition FDR gate.

All functions are pure (no I/O, no API) so they can be unit-tested with `--selftest`
in method.py. Implements:
  * canonical knockoff statistic W_i (signed-max)           [Barber-Candes]
  * knockoff+ operative threshold T(alpha) (eq 1.9)
  * k-floor / certifiable-alpha logic (FDR floor 1/k)
  * tail-conditioned decoy win-rate
  * one-sided two-sample tests (KS, Mann-Whitney, Anderson-Darling, permutation)
  * tail effect sizes (Wasserstein, Cliff's delta, KS-sup, mean-diff)
  * document-block (cluster) bootstrap CIs (B>=2000)
  * Benjamini-Hochberg multiplicity correction
  * within-document rank-normalisation
  * empirical-CDF export for figure-ready overlays
  * realized-FDR calibration for the decoy gate and the raw-confidence baseline
"""
from __future__ import annotations

import hashlib
import math
from typing import Callable, Sequence

import numpy as np
from scipy import stats


# ---------------------------------------------------------------------------
# Rank-normalisation (per document, cancels per-doc scoring-scale differences)
# ---------------------------------------------------------------------------
def _jitter(cand_id: str, seed: int) -> float:
    """Tiny deterministic jitter in [0, 1e-6) to break exact ties before ranking."""
    h = hashlib.sha256(f"{cand_id}|{seed}".encode()).hexdigest()
    return (int(h[:12], 16) / float(16**12)) * 1e-6


def rank_normalize(scores: dict[str, float], seed: int) -> dict[str, float]:
    """Map a pool of candidate scores to [0,1] ranks. cand_id->normalized rank.

    A single-element pool maps to 0.5 (no information). Ties broken by deterministic
    jitter keyed on the candidate id so the mapping is reproducible.
    """
    ids = list(scores.keys())
    n = len(ids)
    if n == 0:
        return {}
    if n == 1:
        return {ids[0]: 0.5}
    jittered = np.array([scores[i] + _jitter(i, seed) for i in ids])
    order = np.argsort(jittered, kind="mergesort")
    ranks = np.empty(n, dtype=float)
    ranks[order] = np.arange(n, dtype=float)
    norm = ranks / (n - 1)  # 0 .. 1
    return {ids[i]: float(norm[i]) for i in range(n)}


# ---------------------------------------------------------------------------
# Canonical knockoff statistic and knockoff+ threshold
# ---------------------------------------------------------------------------
def W_signed_max(z_real: float, z_decoy: float) -> float:
    """Signed-max statistic: magnitude = max(|real|,|decoy|) in score space,
    sign positive iff the real beats its decoy (Barber-Candes antisymmetry).

    Scores are in [0,1] (rank-normalized), so max(z_real,z_decoy) is the magnitude
    and sign(z_real - z_decoy) is the orientation. Antisymmetric under real<->decoy
    swap (sign flips, magnitude unchanged).
    """
    mag = max(z_real, z_decoy)
    s = z_real - z_decoy
    sign = 0.0 if s == 0 else math.copysign(1.0, s)
    return mag * sign


def knockoff_plus_threshold(W: Sequence[float], alpha: float) -> tuple[float, int, float]:
    """knockoff+ operative cutoff T(alpha) (Barber-Candes 2015, eq 1.9):

        T = min{ t in |W| : (1 + #{W_i <= -t}) / max(1, #{W_i >= t}) <= alpha }

    The '+1' in the numerator (Rajchert-Keich: generally necessary) controls *exact*
    FDR (their Thm 2). Returns (T, n_admitted, realized_ratio). If no feasible cutoff
    exists, returns (inf, 0, 1.0) — admit nothing.
    """
    Wa = np.asarray([w for w in W], dtype=float)
    if Wa.size == 0:
        return math.inf, 0, 1.0
    cands = sorted({abs(w) for w in Wa if w != 0.0})
    best = (math.inf, 0, 1.0)
    for t in cands:
        if t <= 0:
            continue
        pos = int(np.sum(Wa >= t))
        neg = int(np.sum(Wa <= -t))
        ratio = (1 + neg) / max(1, pos)
        if ratio <= alpha:
            return float(t), pos, float(ratio)
    return best


def k_floor(alpha: float) -> int:
    """Minimum admissions needed to certify FDR<=alpha (FDR floor 1/k => k>=ceil(1/alpha))."""
    return int(math.ceil(1.0 / alpha))


# ---------------------------------------------------------------------------
# Tail-conditioned decoy win-rate
# ---------------------------------------------------------------------------
def tail_win_rate(pairs: Sequence[tuple[float, float]], threshold: float) -> tuple[float, int]:
    """Among pairs (z_real, z_decoy) in the admission region {max(z_real,z_decoy) >= T},
    fraction where the decoy beats the real. Target ~0.5 under exchangeability.
    Returns (win_rate, n_tail). NaN win_rate if the tail is empty.
    """
    tail = [(zr, zd) for (zr, zd) in pairs if max(zr, zd) >= threshold]
    if not tail:
        return float("nan"), 0
    wins = sum(1 for (zr, zd) in tail if zd > zr)
    return wins / len(tail), len(tail)


# ---------------------------------------------------------------------------
# One-sided two-sample tests + supplements
# ---------------------------------------------------------------------------
def ks_two_sample(decoy: Sequence[float], real: Sequence[float], alternative: str = "two-sided"):
    """KS two-sample. alternative per scipy: 'two-sided','less','greater'.
    Returns (stat, p). Empty input -> (nan, 1.0)."""
    d = np.asarray(decoy, float)
    r = np.asarray(real, float)
    if d.size == 0 or r.size == 0:
        return float("nan"), 1.0
    try:
        res = stats.ks_2samp(d, r, alternative=alternative, method="auto")
        return float(res.statistic), float(res.pvalue)
    except Exception:
        return float("nan"), 1.0


def mannwhitney(decoy: Sequence[float], real: Sequence[float], alternative: str = "two-sided"):
    """Mann-Whitney U (one- or two-sided). Returns (stat, p)."""
    d = np.asarray(decoy, float)
    r = np.asarray(real, float)
    if d.size == 0 or r.size == 0:
        return float("nan"), 1.0
    try:
        res = stats.mannwhitneyu(d, r, alternative=alternative)
        return float(res.statistic), float(res.pvalue)
    except ValueError:
        return float("nan"), 1.0


def anderson_darling_2samp(a: Sequence[float], b: Sequence[float]):
    """Anderson-Darling k-sample (more tail-sensitive than KS). Returns (stat, p).
    p is clipped to scipy's reported floor/cap (0.001 .. 0.25)."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.size < 2 or b.size < 2:
        return float("nan"), 1.0
    try:
        res = stats.anderson_ksamp([a, b])
        return float(res.statistic), float(res.significance_level)
    except Exception:
        return float("nan"), 1.0


def permutation_two_sample(a: Sequence[float], b: Sequence[float], n_perm: int = 5000,
                           seed: int = 0, alternative: str = "two-sided"):
    """Permutation test on the difference of means (robust for small tails).
    Returns (observed_mean_diff a-b, p)."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.size == 0 or b.size == 0:
        return float("nan"), 1.0
    rng = np.random.default_rng(seed)
    obs = a.mean() - b.mean()
    pooled = np.concatenate([a, b])
    na = a.size
    diffs = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(pooled)
        diffs[i] = pooled[:na].mean() - pooled[na:].mean()
    if alternative == "two-sided":
        p = (np.sum(np.abs(diffs) >= abs(obs)) + 1) / (n_perm + 1)
    elif alternative == "greater":
        p = (np.sum(diffs >= obs) + 1) / (n_perm + 1)
    else:  # less
        p = (np.sum(diffs <= obs) + 1) / (n_perm + 1)
    return float(obs), float(p)


# ---------------------------------------------------------------------------
# Tail effect sizes
# ---------------------------------------------------------------------------
def cliffs_delta(a: Sequence[float], b: Sequence[float]) -> float:
    """Cliff's delta in [-1,1]: P(a>b)-P(a<b). Sign(+) => a stochastically larger."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.size == 0 or b.size == 0:
        return float("nan")
    # vectorised count via sorting b
    b_sorted = np.sort(b)
    gt = np.searchsorted(b_sorted, a, side="left").sum()        # #(b < a_i)
    lt = (b.size - np.searchsorted(b_sorted, a, side="right")).sum()  # #(b > a_i)
    return float((gt - lt) / (a.size * b.size))


def tail_gap(decoy: Sequence[float], spont: Sequence[float]) -> dict:
    """Bundle of gap metrics comparing decoy vs spontaneous-error tails.
    Signed mean_diff/cliffs: + => decoys score HIGHER than genuine errors (harder to reject
    => gate over-counts false discoveries => CONSERVATIVE); - => decoys score LOWER (false
    reals beat their decoys => under-count => ANTI-CONSERVATIVE)."""
    d = np.asarray(decoy, float)
    s = np.asarray(spont, float)
    ks_sup, _ = ks_two_sample(d, s, "two-sided")
    w1 = float(stats.wasserstein_distance(d, s)) if d.size and s.size else float("nan")
    md = float(d.mean() - s.mean()) if d.size and s.size else float("nan")
    return {
        "ks_sup": ks_sup,
        "wasserstein": w1,
        "mean_diff": md,
        "cliffs_delta": cliffs_delta(d, s),
        "n_decoy": int(d.size),
        "n_other": int(s.size),
    }


# ---------------------------------------------------------------------------
# Document-block (cluster) bootstrap
# ---------------------------------------------------------------------------
def doc_block_bootstrap(doc_units: list, stat_fn: Callable[[list], float],
                        B: int = 2000, seed: int = 0, ci: float = 0.95) -> dict:
    """Resample whole documents with replacement B times; recompute stat_fn on the
    pooled resample. Returns point estimate, percentile CI, and bootstrap SE.

    doc_units : list of per-document objects (any payload stat_fn understands).
    stat_fn   : maps a list of doc_units -> scalar statistic.
    """
    n = len(doc_units)
    point = stat_fn(doc_units)
    if n == 0:
        return {"point": float("nan"), "ci_low": float("nan"), "ci_high": float("nan"),
                "se": float("nan"), "B": B, "n_docs": 0}
    rng = np.random.default_rng(seed)
    reps = np.empty(B)
    idx_all = np.arange(n)
    for b in range(B):
        idx = rng.choice(idx_all, size=n, replace=True)
        resample = [doc_units[i] for i in idx]
        reps[b] = stat_fn(resample)
    reps = reps[~np.isnan(reps)]
    if reps.size == 0:
        return {"point": float(point) if point == point else float("nan"),
                "ci_low": float("nan"), "ci_high": float("nan"),
                "se": float("nan"), "B": B, "n_docs": n}
    lo = float(np.percentile(reps, 100 * (1 - ci) / 2))
    hi = float(np.percentile(reps, 100 * (1 - (1 - ci) / 2)))
    return {"point": float(point) if point == point else float(np.mean(reps)),
            "ci_low": lo, "ci_high": hi, "se": float(np.std(reps, ddof=1)),
            "B": int(reps.size), "n_docs": n}


# ---------------------------------------------------------------------------
# Benjamini-Hochberg
# ---------------------------------------------------------------------------
def benjamini_hochberg(pvals: Sequence[float], q: float = 0.05) -> list[dict]:
    """BH step-up. Returns list aligned to input order with adjusted p and reject flag."""
    p = np.asarray(pvals, float)
    m = p.size
    if m == 0:
        return []
    order = np.argsort(p, kind="mergesort")
    ranked = p[order]
    adj = np.empty(m)
    prev = 1.0
    for i in range(m - 1, -1, -1):
        val = ranked[i] * m / (i + 1)
        prev = min(prev, val)
        adj[i] = min(prev, 1.0)
    adj_orig = np.empty(m)
    adj_orig[order] = adj
    # reject if BH-adjusted p <= q
    return [{"raw_p": float(p[i]), "bh_adj_p": float(adj_orig[i]),
             "reject": bool(adj_orig[i] <= q)} for i in range(m)]


# ---------------------------------------------------------------------------
# Empirical CDF export (figure-ready)
# ---------------------------------------------------------------------------
def empirical_cdf(values: Sequence[float], grid: Sequence[float]) -> list[float]:
    """Empirical CDF of `values` evaluated on a common `grid`."""
    v = np.sort(np.asarray(values, float))
    g = np.asarray(grid, float)
    if v.size == 0:
        return [float("nan")] * len(g)
    cdf = np.searchsorted(v, g, side="right") / v.size
    return [float(x) for x in cdf]


# ---------------------------------------------------------------------------
# Realized-FDR calibration: decoy gate vs raw-confidence baseline
# ---------------------------------------------------------------------------
def decoy_gate_fdr(reals: list[dict], alpha: float) -> dict:
    """Decoy-competition (knockoff+) gate evaluated against crisp gold.

    reals: list of {'w': W_i, 'is_false': bool} for labelable reals (TRUE/FALSE).
    Admit reals with W_i >= T(alpha). Realized FDR = #(admitted & FALSE)/#admitted.
    """
    W = [r["w"] for r in reals]
    T, n_adm, ratio = knockoff_plus_threshold(W, alpha)
    admitted = [r for r in reals if r["w"] >= T]
    n = len(admitted)
    n_false = sum(1 for r in admitted if r["is_false"])
    realized = (n_false / n) if n else 0.0
    floor = k_floor(alpha)
    return {
        "alpha": alpha, "threshold": (None if math.isinf(T) else T),
        "n_admitted": n, "n_false_admitted": n_false,
        "realized_fdr": realized, "estimated_ratio": ratio,
        "k_floor": floor, "certified": n >= floor,
    }


def baseline_confidence_gate_fdr(reals: list[dict], alpha: float) -> dict:
    """Raw-confidence (purely neural) baseline gate evaluated against crisp gold.

    reals: list of {'z': raw confidence in [0,1] that the real is TRUE, 'is_false': bool}.
    Greedily admit reals in descending confidence while the *self-estimated* FDP
    (mean of (1-confidence) over admitted) stays <= alpha — i.e. trust the model's
    own confidence as a calibrated probability (no labels, no decoys). Realized FDR
    is then measured against crisp gold. This is the standard 'threshold the model's
    confidence' approach the decoy gate is compared against.
    """
    srt = sorted(reals, key=lambda r: r["z"], reverse=True)
    admitted: list[dict] = []
    run_false_mass = 0.0
    for r in srt:
        new_mass = run_false_mass + (1.0 - r["z"])
        n_new = len(admitted) + 1
        if (new_mass / n_new) <= alpha:
            admitted.append(r)
            run_false_mass = new_mass
        else:
            break
    n = len(admitted)
    n_false = sum(1 for r in admitted if r["is_false"])
    realized = (n_false / n) if n else 0.0
    est = (run_false_mass / n) if n else 0.0
    return {
        "alpha": alpha, "n_admitted": n, "n_false_admitted": n_false,
        "realized_fdr": realized, "self_estimated_fdp": est,
    }
