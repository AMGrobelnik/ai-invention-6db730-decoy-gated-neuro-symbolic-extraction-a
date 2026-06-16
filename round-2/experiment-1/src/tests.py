"""
tests.py -- unit tests for fdr_core.py (NO API, run first; must pass before any LLM spend).
Hand-computed answers per the artifact testing_plan items 1-5.
Run: uv run tests.py
"""
from __future__ import annotations

import json
import math

import numpy as np

import fdr_core as fc


def approx(a, b, tol=1e-9):
    return abs(a - b) <= tol


def test_knockoff_plus_threshold():
    # (a) all-positive W, k below floor -> alpha unreachable -> admit nothing
    W = [0.9, 0.8, 0.7, 0.6, 0.5]  # 5 positive
    T, adm, fdr = fc.knockoff_plus_threshold(W, 0.05)  # k-floor=20 > 5
    assert math.isinf(T) and adm == [] and fdr == 1.0, (T, adm, fdr)

    # (b) all-positive W, alpha reachable -> admit all
    T, adm, fdr = fc.knockoff_plus_threshold(W, 0.20)  # k-floor=5; 1/5=0.2<=0.2
    assert adm == [0, 1, 2, 3, 4], adm
    assert approx(fdr, 1.0 / 5), fdr  # (1+0)/5 -- confirms the +1 (else 0)

    # (c) known mixed array, hand-computed: admit indices {0,1} at T=0.8, fdr=0.5
    W = [0.9, 0.8, -0.7, 0.6, -0.5]
    T, adm, fdr = fc.knockoff_plus_threshold(W, 0.5)
    assert approx(T, 0.8) and adm == [0, 1] and approx(fdr, 0.5), (T, adm, fdr)

    # (d) the +1 is present: two positives at alpha=0.5 -> fdr_hat = (1+0)/2 = 0.5, not 0
    T, adm, fdr = fc.knockoff_plus_threshold([0.8, 0.9], 0.5)
    assert adm == [0, 1] and approx(fdr, 0.5), (adm, fdr)
    # at alpha just below 0.5 -> infeasible
    T2, adm2, _ = fc.knockoff_plus_threshold([0.8, 0.9], 0.49)
    assert math.isinf(T2) and adm2 == []

    # (e) 1/k floor helper
    assert fc.k_floor(0.05) == 20 and fc.k_floor(0.10) == 10 and fc.k_floor(0.20) == 5
    assert fc.k_floor(0.30) == 4 and fc.k_floor(0.50) == 2
    assert not fc.alpha_is_certifiable(5, 0.05)  # 5 < 20
    assert fc.alpha_is_certifiable(5, 0.20)      # 5 >= 5
    print("  [ok] knockoff_plus_threshold (+1, 1/k floor, hand-computed mixed array)")


def test_entrapment_fdp():
    assert approx(fc.entrapment_fdp(10, 2, 1.0, "combined"), 4.0 / 12)
    assert approx(fc.entrapment_fdp(10, 2, 1.0, "lower"), 2.0 / 12)
    pc = {"E_ge_s_gt_T": 1, "E_gt_T_ge_s": 1}
    assert approx(fc.entrapment_fdp(10, 2, 1.0, "paired", pc), (2 + 1 + 2 * 1) / 12)
    # r=5 combined inflation (1+1/5)
    assert approx(fc.entrapment_fdp(10, 5, 5.0, "combined"), 5 * 1.2 / 15)
    # 'sample' must raise; paired requires r==1
    for bad in [("sample", None, 1.0), ("paired", None, 2.0)]:
        try:
            fc.entrapment_fdp(10, 2, bad[2], bad[0], bad[1])
            assert False, "should have raised"
        except ValueError:
            pass
    print("  [ok] entrapment_fdp (combined/lower/paired eqs; sample & r!=1 raise)")


def test_gold_label():
    # Build crisp gold from mini example 1 (convention: (h,r,t) = 'tail is head's relation')
    with open("data/mini_data_out.json") as f:
        mini = json.load(f)
    ex = mini["datasets"][0]["examples"][0]
    out = json.loads(ex["output"])
    gold_true = set()
    covered = set()
    for fct in out["atomic_facts"] + out["multi_hop_facts"]:
        gold_true.add((fct["head"], fct["relation"].lower(), fct["tail"]))
        covered.add((fct["head"], fct["tail"]))
    # every gold triple labels TRUE
    for fct in out["atomic_facts"] + out["multi_hop_facts"]:
        assert fc.gold_label((fct["head"], fct["relation"], fct["tail"]), gold_true, covered) == fc.TRUE
    # known: (Gabrielle, grandson, Dan) TRUE ; convention check
    assert fc.gold_label(("Gabrielle", "grandson", "Dan"), gold_true, covered) == fc.TRUE
    # wrong relation on a covered pair -> FALSE (genuine hallucination)
    assert fc.gold_label(("Gabrielle", "granddaughter", "Dan"), gold_true, covered) == fc.FALSE
    # reversed direction is an off-path pair -> UNJUDGEABLE
    assert fc.gold_label(("Dan", "brother", "Gabrielle"), gold_true, covered) == fc.UNJUDGEABLE
    print("  [ok] gold_label (TRUE/FALSE/UNJUDGEABLE; convention; direction-sensitive)")


def test_doc_block_bootstrap():
    # per-doc records: each doc carries a list of 0/1 (false-admission indicators)
    rng = np.random.default_rng(0)
    per_doc = [list(rng.integers(0, 2, size=5)) for _ in range(30)]

    def stat(records):
        flat = [x for doc in records for x in doc]
        return float(np.mean(flat)) if flat else float("nan")

    p1, lo1, hi1 = fc.doc_block_bootstrap(per_doc, stat, B=500, seed=42)
    p2, lo2, hi2 = fc.doc_block_bootstrap(per_doc, stat, B=500, seed=42)
    assert (p1, lo1, hi1) == (p2, lo2, hi2), "same seed must reproduce"
    assert lo1 <= p1 <= hi1, "CI must bracket the point estimate"
    # different seed -> (generally) different CI but same point
    p3, lo3, hi3 = fc.doc_block_bootstrap(per_doc, stat, B=500, seed=7)
    assert approx(p3, p1), "point estimate is seed-independent"
    print("  [ok] doc_block_bootstrap (reproducible, brackets point, doc-level resample)")


def test_w_statistic():
    assert approx(fc.w_statistic(0.9, 0.3), 0.9)   # real wins -> +max
    assert approx(fc.w_statistic(0.3, 0.9), -0.9)  # decoy wins -> -max
    assert approx(fc.w_statistic(0.5, 0.5), 0.0)   # tie -> 0
    # canonical formula identity on a grid
    for zr in np.linspace(0, 1, 11):
        for zd in np.linspace(0, 1, 11):
            zr_f, zd_f = float(zr), float(zd)
            s = (zr_f > zd_f) - (zr_f < zd_f)
            assert approx(fc.w_statistic(zr_f, zd_f), s * max(zr_f, zd_f))
    print("  [ok] w_statistic (canonical sign*max; d_i never used as gate input)")


def test_plain_threshold_gate():
    Z = [0.95, 0.9, 0.6, 0.5]
    thr, adm, est = fc.plain_threshold_gate(Z, 0.10)
    # top-1: 0.05<=0.1; top-2: 0.075<=0.1; top-3: 0.1833>0.1 -> best_k=2
    assert adm == [0, 1] and approx(est, 1 - (0.95 + 0.9) / 2), (adm, est)
    # nothing admissible if top score below 1-alpha
    thr0, adm0, _ = fc.plain_threshold_gate([0.5, 0.4], 0.10)
    assert math.isinf(thr0) and adm0 == []
    print("  [ok] plain_threshold_gate (decoy-free confidence baseline)")


def test_auc_and_tail():
    # perfectly separable
    assert approx(fc.auc([0.9, 0.8], [0.1, 0.2]), 1.0)
    assert approx(fc.auc([0.1, 0.2], [0.9, 0.8]), 0.0)
    assert approx(fc.auc([0.5, 0.5], [0.5, 0.5]), 0.5)  # all ties
    scores = [0.9, 0.85, 0.4, 0.3, 0.8, 0.2]
    labels = [fc.TRUE, fc.FALSE, fc.TRUE, fc.FALSE, fc.TRUE, fc.FALSE]
    ta = fc.tail_auc(scores, labels, tail_frac=0.5)  # tail = top3: 0.9(T),0.85(F),0.8(T)
    # pos={0.9,0.8}, neg={0.85}; P(pos>neg) = ((0.9>0.85)+(0.8>0.85))/2 = (1+0)/2 = 0.5
    assert approx(ta, 0.5), ta
    wr = fc.tail_win_rate([0.9, 0.2], [0.3, 0.95], cut=0.5)  # pairs with max>=0.5: both; decoy wins pair2
    assert approx(wr, 0.5), wr
    print("  [ok] auc / tail_auc / tail_win_rate")


def main():
    print("Running fdr_core unit tests (no API)...")
    test_knockoff_plus_threshold()
    test_entrapment_fdp()
    test_gold_label()
    test_doc_block_bootstrap()
    test_w_statistic()
    test_plain_threshold_gate()
    test_auc_and_tail()
    print("ALL UNIT TESTS PASSED")


if __name__ == "__main__":
    main()
