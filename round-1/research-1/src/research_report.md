# Spec Sheet: Label-Free FDR Gate at the LLM Text-to-Logic Admission Boundary

## Summary

Consolidated, source-traceable implementation spec for the label-free decoy-competition FDR gate that admits LLM-extracted facts/bridges into a Prolog/symbolic layer. Provides, for each component, a verbatim formula (with equation number and source), a symbol glossary, a language-agnostic pseudo-procedure, and a recommended default. KEY RESULTS: (A) knockoff+ admission threshold T=min{t: (1+#{W_i<=-t})/(#{W_i>=t} v 1)<=alpha} (Barber-Candes eq 1.9, exact FDR via Thm 2; plain knockoff eq 1.8 controls only modified FDR Thm 1); the minimum-estimable-FDR floor is 1/k, so certifying FDR<=alpha needs k>=ceil(1/alpha) admissions -> demonstrable alpha grid {0.05,0.1,0.2,0.3,0.5} maps to k-floors {20,10,5,4,2}. Rajchert-Keich prove the '+1' is generally necessary (t=1 optimal), so keep it; TDC-SB/TDC-UB (bandsfdp) are an optional tighter FDX bound. (B) Entrapment estimators verbatim from Wen et al. 2025: combined FDP=N_E(1+1/r)/(N_T+N_E) (upper bound, DEFAULT), paired (eq4, requires r=1, tighter), lower bound N_E/(N_T+N_E) (failure-only), and 'sample' N_E(1/r)/N_T which is INVALID (biased). r=#entrapment/#target; default r=1 paired. (C) Document-block (cluster) bootstrap B>=2000 for all FDP/FDR CIs (resample whole documents; Cameron-Gelbach-Miller anchor) — the CI used by the primary disconfirmation. (D) Sole validity condition = Barber-Candes Lemma 1 (null W signs are i.i.d. fair coins) = TDC equal-chance; two anti-conservative failure modes (within-doc correlation -> bootstrap; batched contrast effect -> isolated provenance-blinded order-randomized scoring) and the isolated-vs-batched discriminator. (E) Property-matched document-conditioned COUNTERFACTUAL decoys + non-entailment verification (DeepCoy principle; DOE 0.166->0.032/0.109->0.038); random type-matched swaps kept as the anti-conservative negative control. (F) Ranked label-free upper-tail elicitation shortlist: DINCO (primary, overconfidence-corrected), FactSelfCheck (fact-level), self-consistency/SelfCheckGPT, logprob/yes-no-token (if exposed), verbalized (overconfident floor); Phase-0 selects on tail-AUC>0.5 with CI + isolated~batched agreement. (G) Recommended model openai/gpt-4.1-nano ($0.10/$0.40 per M, logprobs+auto-caching, <$0.30 input); fallbacks gpt-4o-mini then a logprob-free cheap caching model; projected cost ~$1-3 << $10 cap. (H) Novelty confirmed: no prior work applies knockoff/target-decoy/entrapment FDR at a label-free LLM text->logic admission boundary (conformal factuality/selection are labeled and certify outputs). Includes a final Parameter Defaults table and runtime follow-ups (probe logprobs non-null; confirm cached_tokens>0).

## Research Findings

# Implementation-Ready Spec — Label-Free FDR Gate at the Text-to-Logic Admission Boundary

> **Scope.** This is a copy-pasteable specification sheet for every scalar input and procedure of the
> decoy-competition FDR gate used to admit LLM-extracted facts/bridges into the symbolic (Prolog) layer.
> Every equation is quoted verbatim from a primary source with its equation number, every symbol is
> glossed, and each component is reduced to a language-agnostic pseudo-procedure with a recommended default.
> A method-executor reading **only this file** can code Phase-0 + the CLUTRR calibration diagonal with no
> further literature lookup. Citations `[n]` index the Sources section at the end.
>
> **Conventions used throughout.** `a ∨ b = max(a,b)`. "Admission" = a candidate (extracted atomic fact or
> multi-hop bridge) is accepted into the symbolic layer. `W_i` is the per-candidate **competition statistic**
> (real-candidate score minus its matched decoy score, sign-antisymmetric). `t` is the operative admission
> cutoff on `W`. `α` is the target FDR. The gate decides admission **by decoy competition (knockoff+)**, and
> uses **entrapment** as an *independent* corroborating upper bound.

---

## A. knockoff+/TDC thresholding and the `+1` / `1/k` minimum-estimable-FDR floor

### A.1 The competition statistic and its required properties (verbatim)

Barber & Candès define the statistic `W_j` and require two properties [1]:

- **Antisymmetry property (Definition 4)** [1]: *"The statistic W is said to obey the antisymmetry
  property if swapping X_j and X̃_j has the effect of switching the sign of W_j."* Formally, for any
  `S ⊆ {1,…,p}`, `W_j([X X̃]_swap(S), y) = W_j([X X̃], y) · (+1 if j∉S, −1 if j∈S)`.
- **Sufficiency property (Definition 3)** [1]: `W` depends on the data only through `[X X̃]ᵀ[X X̃]` and `[X X̃]ᵀy`.

A large **positive** `W_j` is evidence the candidate is a true signal; the sign of `W_j` is the "win/lose"
of real vs. decoy.

### A.2 The two thresholds (verbatim)

- **knockoff (Definition 1, eq. 1.8)** [1] — controls the *modified* FDR:
  ```
  T = min { t ∈ W : #{j : W_j ≤ −t} / (#{j : W_j ≥ t} ∨ 1) ≤ q }
  ```
- **knockoff+ (Definition 2, eq. 1.9)** [1] — controls the FDR **exactly**:
  ```
  T = min { t ∈ W : ( 1 + #{j : W_j ≤ −t} ) / (#{j : W_j ≥ t} ∨ 1) ≤ q }
  ```
  Selected/admitted set: `Ŝ = { j : W_j ≥ T }` (Definition 1) [1].

**Which controls what (verbatim theorems)** [1]:
- **Theorem 1 (knockoff → modified FDR):** `E[ #{j: β_j=0 and j∈Ŝ} / (#{j: j∈Ŝ} + q⁻¹) ] ≤ q`. The
  `q⁻¹` in the denominator makes this "very close to the FDR when a high number of variables are selected,
  but may be quite different when a small number of variables is selected" [1].
- **Theorem 2 (knockoff+ → FDR):** `FDR = E[ #{j: β_j=0 and j∈Ŝ} / (#{j: j∈Ŝ} ∨ 1) ] ≤ q`.

> **Gate mapping (use knockoff+).** estimated FDR at cutoff `t`:
> `FDR_hat(t) = (1 + #{i : W_i ≤ −t}) / (#{i : W_i ≥ t} ∨ 1)`; admit `{i : W_i ≥ t}` at the **smallest** `t`
> (most permissive) with `FDR_hat(t) ≤ α`. This is exactly eq. 1.9 with `q := α`.

### A.3 Minimum-estimable-FDR floor (`1/k`) — DERIVED, with the demonstrable-α grid

The numerator of eq. 1.9 is `1 + #{W_i ≤ −t} ≥ 1`; the denominator is at most `k = #admitted`. Hence the
**smallest attainable estimate with k admissions is `(1+0)/k = 1/k`** (achieved when zero decoy wins lie above
`t`). To certify `FDR_hat ≤ α` you therefore need `1/k ≤ α`, i.e. **`k ≥ ⌈1/α⌉`**. This is a hard structural
floor and dictates how many admissions each anchor/relation must yield before an α is even demonstrable:

| α | k-floor = ⌈1/α⌉ | interpretation |
|------|-----------------|-----------------------------------------------|
| 0.05 | **20** | need ≥20 admitted candidates to certify FDR≤5% |
| 0.10 | **10** | ≥10 admissions |
| 0.20 | **5**  | ≥5 admissions |
| 0.30 | **4**  | (1/0.3=3.33 → 4) |
| 0.50 | **2**  | ≥2 admissions |

**Recommended demonstrable-α grid:** `{0.05, 0.10, 0.20, 0.30, 0.50}` — each grid point tied to its k-floor
above. Phase-0/CLUTRR must guarantee per-(facts | bridges)-per-anchor admission counts ≥ the k-floor of the
smallest α you intend to demonstrate, else that α is structurally unreachable regardless of model quality.

### A.4 Is the `+1` droppable? (Rajchert & Keich, verbatim findings)

Rajchert & Keich study the general additive constant `t` in `SSSt+` (eq. 2–3 of [2], the sequential/TDC form
of the `+1`) and answer **the `+1` is, in general, necessary** [2]:

- **Theorem 1 + Corollary 1** [2]: writing `((1−c)/c)·α = a/b` with `a,b` coprime, for any `t ∈ (1 − 1/b, 1]`
  the threshold is **unchanged** (`K_t = K_1`). So you *can* shrink the constant below 1 in some cases, **but
  it makes no difference to the discovery list** — no power is gained.
- **Theorem 2 + Corollary 2** [2]: for the `a=1` case (i.e. `α = 1/b` form, `c=1/2`), **`t = 1` is optimal**:
  any `t<1` either gives `K_t = K_1` or **fails to control the FDR** (they construct an explicit counterexample
  where `FDR(SSSt+) > α`, confirmed to bite even for moderate `n`, their Fig. 1). The result "applies to TDC".

> **Spec consequence.** Do **not** drop or relax the `+1` for the headline certificate — keep eq. 1.9 as
> written. The conservativeness the `+1` induces is exactly the `1/k` floor of A.3; it is large only at small
> `k`. Any "leftover-budget +1-floor relaxation" experiment is **exploratory** and must be validated
> empirically (it has no finite-sample guarantee per Theorem 2 of [2]).

### A.5 Leftover-budget tightening: TDC-SB / TDC-UB (Ebadi et al.) — NOT the headline

Ebadi et al. give **upper prediction bounds on the FDP** (not just its average) for competition-based FDR
control: **TDC-SB** (standardized band) and **TDC-UB** (uniform band) [3]. They bound the decoy-win counting
process `U_d` whose marginal is **negative-binomial `NB(d, R)`**, and require a horizon parameter `d_max` [3].
Both are **"significantly tighter than ones obtained using … Katsevich and Ramdas"** (TDC-KR) [3]. Reported
median bounds (m=2000, π₀=0.5, ρ=3) [3]:

| confidence γ | TDC-UB | TDC-SB | TDC-KR (Katsevich–Ramdas) |
|--------------|--------|--------|---------------------------|
| 0.01 | **0.087** | 0.094 | 0.243 |
| 0.05 | **0.079** | 0.083 | 0.189 |

TDC-UB is generally the tightest. **Reference implementation:** R package `bandsfdp`; the function
`tdc_ub(thresholds, labels, alpha, gamma, c=0.5, lambda=0.5, n=length(labels), interpolate=TRUE)` "computes an
upper prediction bound, derived from the uniform band, on the FDP in TDC's list of discoveries"; `gamma` is the
confidence parameter (typical `0.05` or `0.01`), `c=0.5` sets winning target ranks for single-decoy TDC [4].
The method-executor can port `bandsfdp` (tdc_ub/tdc_sb) to Python. **Mark as leftover-budget FDX tightening,
not the primary certificate.**

### A.6 Pseudo-procedure — `knockoff_plus_threshold`

```
function knockoff_plus_threshold(W[], alpha):           # W = competition statistics (signed), one per candidate
    cand_cutoffs = sort( unique( |W_i| for all i ) )     # scan candidate t over distinct |W| magnitudes, ascending
    best = (t=+inf, admitted={}, fdr=1.0)
    for t in cand_cutoffs:                                # ascending t = most→least permissive as t grows
        pos = count(i : W_i >=  t)                        # real wins at/above t  (= #admitted at this t)
        neg = count(i : W_i <= -t)                        # decoy wins at/below -t
        fdr_hat = (1 + neg) / max(1, pos)                 # eq. 1.9
        if fdr_hat <= alpha:                              # feasible cutoff
            return (t, {i : W_i >= t}, fdr_hat)           # smallest such t = most permissive admission
    return (+inf, {}, 1.0)                                # no feasible cutoff: admit nothing
# Floor check: if max attainable #admitted < ceil(1/alpha), this alpha is structurally undemonstrable (A.3).
```

---

## B. Valid entrapment combined/paired estimator and the ratio `r`

**Role in the gate.** Decoy competition (Sub-task A) decides **admission**. Entrapment provides an
**independent, construction-distinct upper bound** on the realized FDP, compared against gold on a labeled
slice. Use the **combined** estimator as the default certificate and **paired** (r=1) as the tighter
certificate; **never** use *sample*; use *lower bound* only to demonstrate *failure*.

Symbols (verbatim from [5]): `N_T`, `N_E` = number of original-**target** and **entrapment** discoveries at
the operative cutoff; `r` = **effective ratio of the entrapment to original target database size**
(`r = #entrapment / #target`, the *database-size* ratio — distinct from the discovery counts `N_T, N_E`) [5,6].

### B.1 The four estimators (verbatim, with equation numbers from the Nature Methods paper)

- **Lower bound (eq. 2)** [5]: `FDP̂_{T∪E} = N_E / (N_T + N_E)`.
  *"without the 1/r term and assuming that any entrapment discovery is indeed false, equation (2) represents a
  lower bound on the FDP. As such, this method can only be used to indicate that a tool **fails** to control
  the FDR … rather than as evidence of FDR control."* [5]
- **Combined (eq. 1) — DEFAULT certificate** [5]:
  ```
  FDP̂_{T∪E} = N_E · (1 + 1/r) / (N_T + N_E)
  ```
  Grouping is **`(1 + 1/r)`** (verified verbatim) [5]. *"under an assumption analogous to the equal-chance
  assumption that TDC relies on, equation (1) provides an estimated **upper bound**, that is, on average it
  overestimates the true FDP."* With `r = 1` it reduces to Elias & Gygi's concatenated target+decoy FDR
  estimate [5].
- **Sample (eq. 3) — INVALID, do not use** [5]:
  ```
  FDP̂_T = N_E · (1/r) / N_T          # estimates FDP only among the original-target (T) discoveries
  ```
  *"the sample-entrapment method is inherently flawed because, while **typically underestimating** the FDP, it
  can also **overestimate** it in some unusual cases … cannot be used to provide empirical evidence that a tool
  controls the FDR nor that the tool fails to control the FDR."* [5]
- **Paired (eq. 4) — TIGHTER certificate, requires `r = 1`** [5]:
  ```
  FDP̂*_{T∪E} = ( N_E + N_{E≥s>T} + 2·N_{E>T≥s} ) / (N_T + N_E)
  ```
  where `s` = discovery cutoff score; `N_{E≥s>T}` = # discovered entrapment items (score ≥ s) whose **paired**
  target scores `< s`; `N_{E>T≥s}` = # discovered entrapment items whose paired target scored lower **but was
  still also discovered** [5]. Requires each target paired with a **unique** entrapment (so `r = 1`); a
  `k`-matched generalization uses `r = k`. Both are valid upper bounds "in the same averaged sense" as combined [5].
  *Tightest case is `r = 1` paired.* (OmniNovo applies exactly this `r=1` one-to-one paired entrapment "following
  the framework proposed by Wen et al." [7].)

### B.2 Why "sample" is biased (the paper's exact argument)

The sample method estimates the FDP **only among the original-target list `T`** (denominator `N_T`, eq. 3),
i.e. it targets the wrong discovery list and ignores that the relevant search space is the **augmented** T∪E
list. The paper proves (Supplementary Note 3) it is **inherently flawed**: it **typically underestimates** FDP
(so it would falsely "pass" a leaky pipeline) but can also **overestimate** in unusual cases — therefore it can
be used as evidence **neither** of control **nor** of failure [5].

### B.3 How `r` propagates (point estimate, variance, achievable-α floor)

1. **Point estimate:** `r` enters combined via the multiplicative `(1 + 1/r)` inflation. As `r → ∞`,
   `(1+1/r) → 1` and combined → lower bound (the difference is exactly `1/r`; the paper notes at `r = 5` the
   gap is `1/r = 20%`) [5]. Smaller `r` ⇒ larger inflation ⇒ more conservative upper bound.
2. **Variance:** smaller `r` ⇒ fewer entrapment items ⇒ smaller-count `N_E` ⇒ **higher relative variance** of
   `N_E` ⇒ **wider** FDP CI. Larger `r` shrinks variance but moves you away from the actual application (you are
   searching a much larger DB than intended) [5].
3. **Achievable-α floor:** an entrapment certificate cannot certify FDP below roughly its own counting
   granularity (≈ `1/(N_T+N_E)`); with few entrapment discoveries the smallest *credibly distinguishable* FDP
   is coarse. (This parallels the `1/k` floor of A.3.)

> **Recommended default: `r = 1`, paired estimator** (tightest valid certificate; matches the hypothesis's
> "entrapment-at-one-item"). Trade-off of `r > 1`: lower variance but a looser, less application-faithful bound
> and `k`-matched bookkeeping. Use **combined** when pairing is unavailable.

### B.4 Pseudo-procedure — `entrapment_fdp`

```
function entrapment_fdp(N_T, N_E, r, estimator, paired_counts=None):
    if estimator == "lower":     return N_E / max(1, N_T + N_E)                      # eq.2  (lower bound)
    if estimator == "combined":  return N_E * (1 + 1.0/r) / max(1, N_T + N_E)        # eq.1  (default upper bound)
    if estimator == "sample":    raise Error("invalid — do not use (eq.3 is biased)")
    if estimator == "paired":    # requires r==1 and per-target paired entrapment scores; s = operative cutoff
        N_Egt = paired_counts.E_ge_s_gt_T      # entrapment >= s whose paired target < s
        N_Egtt = paired_counts.E_gt_T_ge_s     # entrapment whose paired target scored lower but is also discovered
        return (N_E + N_Egt + 2*N_Egtt) / max(1, N_T + N_E)                          # eq.4  (tighter upper bound)
# Construction-independence: build entrapment by a mechanism DISTINCT from the admission decoys, so the two
# FDR signals (knockoff+ admission vs. entrapment bound) are independent corroborations against gold.
```

---

## C. Document-block (cluster) bootstrap for all FDP/FDR confidence intervals

### C.1 Threat addressed

LLM scoring noise is **correlated within a document** (shared context, entities, genre). Treating per-candidate
`W` signs as i.i.d. across the pooled corpus **understates variance** and the floor — i.e. it is
**anti-conservative**. The fix is to resample **whole documents** (clusters/blocks), preserving within-document
dependence. This is the standard cluster/block-bootstrap remedy for within-group dependence: the **pairs
cluster bootstrap** and **wild cluster bootstrap** of Cameron, Gelbach & Miller (RESTAT 2008, 90(3):414–427),
which correct over-rejection when errors are clustered [8]; lineage also includes the moving/block bootstrap
for dependent data (Künsch 1989). Resample at the **document** level, not the candidate level.

### C.2 Procedure (concrete)

```
for b in 1..B:
    docs_b   = sample WITH REPLACEMENT from {documents}      # block = whole document, preserves within-doc dependence
    corpus_b = concat(all candidate records of docs in docs_b)
    t_b, S_b, fdr_b = knockoff_plus_threshold(W of corpus_b, alpha)   # re-run the WHOLE gate on the resample
    ent_b   = entrapment_fdp(N_T(corpus_b), N_E(corpus_b), r, estimator)   # and the entrapment bound
    stat_b  = realized_FDP_statistic(corpus_b)               # whatever statistic the disconfirmation tests
collect {stat_b}; report percentile CI (2.5%, 97.5%).
# Primary disconfirmation: does the CI lie ENTIRELY on the anti-conservative (above-alpha) side?
```

- **Recommended `B ≥ 2000`** (percentile-CI tail stability; `B=2000` gives stable 2.5/97.5 quantiles).
- **Statistic of interest** = realized FDP vs. the operative `α`; the CI used by the **primary
  disconfirmation** is this document-block percentile CI.

### C.3 Two granularities — do not conflate

- **FDP bootstrap** (above): resample **documents with replacement**, recompute the gate, get an FDP/FDR CI.
- **Cross-validation for S5** (leave-one-cluster-out / leave-one-document-out): a **separate** generalization
  check — partition documents, hold one out, evaluate. It is **not** the FDP CI and must not be mixed into the
  bootstrap loop.

### C.4 Pseudo-procedure — `doc_block_bootstrap`

```
function doc_block_bootstrap(per_doc_records, statistic_fn, B=2000):
    stats = []
    D = number of documents
    for b in 1..B:
        idx   = sample D document-indices WITH replacement
        boot  = concat(per_doc_records[i] for i in idx)
        stats.append( statistic_fn(boot) )
    point = statistic_fn(per_doc_records)                    # plug-in point estimate on full data
    return (point, percentile(stats, 2.5), percentile(stats, 97.5))
```

---

## D. Null sign-flip property + two LLM failure modes + isolated-vs-batched discriminator

### D.1 The sole validity condition (verbatim)

Barber & Candès, **Lemma 1 (i.i.d. signs for the nulls)** [1]:
> *"Let ε ∈ {±1}ᵖ be a sign sequence independent of W, with ε_j = +1 for all nonnull j and ε_j ~iid {±1} for
> null j. Then (W₁,…,W_p) =d (W₁·ε₁,…,W_p·ε_p)."*

i.e. **for genuinely-false (null) candidates the sign of `W_i` is an independent fair coin (P=0.5), independent
of `|W_i|` and of the signs of the true candidates** [1]. Consequence (eq. 1.10) [1]:
`#{j: β_j=0 and W_j ≥ t} =d #{j: β_j=0 and W_j ≤ −t}`, which is what makes `#{W_i ≤ −t}` a valid estimate of the
false admissions above `t`. The **TDC "equal-chance" assumption** [5] is the same statement in competition
language: *a false real candidate and its matched decoy are exchangeable in the high-score tail* (each equally
likely to win).

> **Honesty caveat (state in the paper).** For LLM decoys there is **no construction-level proof** of Lemma 1
> (unlike Gaussian knockoffs). The gate is therefore an **empirically-validated calibration**, not a theorem;
> D.4 diagnostics must show the fair-coin property *holds in the tail* on labeled data.

### D.2 Two anti-conservative failure channels (reproduce this table)

| # | Failure channel | Mechanism | Effect on FDP | Mitigation |
|---|-----------------|-----------|---------------|------------|
| 1 | **Within-document score correlation** | Null `W` signs dependent within a document → variance/floor understated | Floor/CI too tight (anti-conservative) | **Document-block bootstrap** (Sub-task C) |
| 2 | **Batched-scoring contrast effects** | Model implicitly detects the fabricated/odd item among co-presented candidates and depresses decoy scores → decoys lose "too often" | FDP **optimistically** low (anti-conservative) | **ISOLATED, provenance-blinded, order-randomized** scoring as default |

### D.3 Isolated-vs-batched discriminator (pre-registered test)

```
Run a LABELED slice under BOTH scoring regimes:
  - ISOLATED : each candidate scored in its own call, provenance hidden, order randomized
  - BATCHED  : candidates co-presented in one call
Decision:
  if ISOLATED restores the FDR-vs-alpha diagonal (calibrated) but BATCHED is anti-conservative
        -> the anti-conservatism was a SCORING ARTIFACT (contrast effect); isolated scoring fixes it.
  if anti-conservatism PERSISTS under ISOLATED
        -> genuine decoy NON-exchangeability (decoys are "too easy"); fix the decoy family (Sub-task E).
```
**Default = isolated scoring for 100% of the confirmatory set.** Headroom is bought by **prompt caching of the
document prefix**, *not* by batching (batching reintroduces channel #2).

### D.4 Tail diagnostics (measurement only — NEVER consumed by the gate)

1. **Tail-conditioned win-rate** of matched (real-false, decoy) pairs **above the admission cutoff `t`** should
   be ≈ 0.5 (the fair-coin check of D.1).
2. **Upper-tail two-sample CDF test** on real-false vs. decoy scores restricted to the admission region
   (`scores ≥ t`): recommended **one-sided two-sample Kolmogorov–Smirnov** (or a tail-restricted Mann–Whitney
   U) testing whether decoy scores are stochastically *smaller* than real-false scores in the tail (which would
   signal non-exchangeability). "Tail" is delimited by `scores ≥ operative knockoff+ cutoff t`.

---

## E. Plausibility / property-matched decoy generation

### E.1 The load-bearing principle (DeepCoy, verbatim cautionary evidence)

DeepCoy [9] generates **property-matched** decoys: decoys must **reproduce the property/score distribution of
the true positives** and must **not be "too easy."** Too-easy/biased decoys let the scorer separate on
artifacts and make the estimated FDR **optimistic**. Quantified by **DOE (Deviation from Optimal Embedding):**
DeepCoy improves DOE by an average of **81% (0.166 → 0.032 on DUD-E)** and **66% (0.109 → 0.038 on DEKOIS
2.0)** while "introducing no discernible additional risk of false negatives" [9].

> **Text translation.** An LLM decoy must reproduce the **score distribution of genuine plausible
> hallucinations** — same entity types, surface form, specificity — so the *only* feature distinguishing it
> from a real-but-false fact is document non-entailment.

### E.2 Primary decoy family — document-conditioned counterfactuals (+ negative control)

- **PRIMARY: document-conditioned counterfactual decoys** — maximally-plausible, document-**non-entailed**
  facts/bridges drawn from the model's own prior **conditioned on the document**. Generation recipe (prompt
  sketch): *"Given DOCUMENT and the relation/entity-type schema R(·,·), produce a fact `R(a,b)` that is
  plausible for this genre and these entities but **is NOT stated or entailed by the document**; match the
  surface form and specificity of the document's real facts."* Predicted tail-win-rate ≈ 0.5.
- **NEGATIVE CONTROL (keep, expect anti-conservative): random type-matched swaps** — replace an argument with a
  random type-matched entity. Deliberately retained as the baseline that *should* read anti-conservative
  (decoys too easy → optimistic FDR), validating the diagnostic.

### E.3 Non-entailment verification gate (every decoy must pass)

An **accidentally-entailed** decoy is actually true → would bias the FDR **conservatively**. So every decoy
passes an **independent entailment check** against the document: NLI-style, or a **separate isolated LLM call**
asking *"Is this statement entailed by the text? yes/no."* Reject (regenerate) if entailed. **Report the
contamination rate** and run a **contamination sensitivity analysis** (sweep the rejection threshold).
*"Plausibility-matched"* is defined as: decoy and real share entity types / surface form / specificity, so the
only difference is entailment.

### E.4 Pseudo-procedures

```
function generate_decoy(document, candidate_real):
    schema = relation_and_type_schema(candidate_real)
    decoy  = LLM("plausible, type/surface/specificity-matched fact under {schema} "
                 "that is NOT entailed by:\n{document}")
    return decoy

function verify_non_entailment(document, decoy):           # independent, isolated call (or NLI model)
    return LLM_isolated("Is '{decoy}' entailed by the text? Answer yes/no.\n{document}") == "no"
# Accept decoy only if verify_non_entailment is True; log contamination_rate = #entailed / #generated.
```

---

## F. Upper-tail label-free score elicitation — ranked shortlist

Goal: a per-candidate score whose **upper tail** discriminates true from false (the admission region). Tail
calibration matters far more than average calibration here.

### F.1 Candidates with reported tail behavior

1. **Verbalized confidence** (model states 0–100/0–1). **Overconfident in the upper tail**: Xiong et al.
   (ICLR 2024) find LLMs are *overconfident* when verbalizing, "potentially imitating human patterns";
   calibration improves with scale but remains far from ideal; human-inspired prompting mitigates with
   diminishing returns in advanced models [10]. → use as a **floor baseline**.
2. **Token-logprob-derived score** (sequence/avg token logprob, or yes/no-token probability of an
   entailment-framed prompt). Better calibrated than verbalized for **base** models, but **degrades under
   RLHF**: Tian et al. (EMNLP 2023) find for RLHF LMs (ChatGPT/GPT-4/Claude) the **verbalized** confidence is
   *typically better calibrated than the model's conditional (log)probabilities* on TriviaQA/SciQ/TruthfulQA
   [11]. **Requires a model exposing logprobs** (ties to Sub-task G). DINCO confirms logit access still helps
   calibration when available [12].
3. **Self-consistency / SelfCheckGPT** (Manakul et al. 2023): sample `N` completions, score by agreement;
   **zero-resource, black-box, no logprobs needed**, but `N×` cost [13]. The consistency-across-generations
   signal is correlated with correctness [12].
4. **DINCO — Distractor-Normalized Coherence** (2509.25532, ICLR 2026) — **overconfidence-corrected primary
   candidate** [12]. Verbalize confidence independently across self-generated **distractors** (alternative
   claims) and **normalize by the total verbalized confidence**; an off-the-shelf NLI model down-weights
   distractors that don't contradict the main claim; then integrate **self-consistency** via
   generator–validator disagreement. Exact normalization (eq. 2) [12]:
   ```
   β(C) ≈ Σ_{c∈C} f_VC(c) ;   f_NVC(c) = f_VC(c) / β(C) ≈ f_lat(c) ;   in practice β(C) ← max(1, β(C))
   ```
   where `C` = main claim + distractors, `f_VC` = raw verbalized confidence, `f_NVC` = normalized.
   Reported gains: **ECE improved over the best baseline by 0.077 (TriviaQA), 0.092 (SimpleQA), 0.055
   (FactScore)**; correlation with passage-level FactScore +0.072 (Pearson)/+0.074 (Spearman); **DINCO at 10
   inference calls outperforms self-consistency at 100**; relieves confidence saturation [12].
5. **FactSelfCheck** (2503.17229) — **fact-level black-box** [14]. Represents output as a knowledge graph of
   **triples `(h, r, t)`**; computes a per-fact hallucination score `H_fact` from **factual consistency across
   `N` stochastic samples** (KG or text variant); zero-resource, no logprobs. **Native fact-level granularity
   matches the gate's per-candidate unit.** Improves hallucination *correction* by **35.5%** vs SelfCheckGPT's
   **10.6%** [14].

### F.2 Ranking (by: upper-tail discrimination, zero-label feasibility, cost/logprob need, isolated-scoring fit)

| Rank | Elicitation | Upper-tail behavior | Labels | logprobs? | Cost | Phase-0 role |
|------|-------------|---------------------|--------|-----------|------|--------------|
| 1 | **DINCO** | overconfidence-**corrected**, less saturated | none | optional (helps) | ~10 calls | **primary candidate** |
| 2 | **FactSelfCheck** | fact-level consistency, matches unit | none | no | `N×` | sampling option, per-fact |
| 3 | **Self-consistency / SelfCheckGPT** | decent, saturates | none | no | `N×` | sampling baseline |
| 4 | **Token-logprob / yes-no-token** | good for base, RLHF-degraded | none | **yes** | 1 call | logprob variant **iff** model exposes logprobs |
| 5 | **Verbalized confidence** | **overconfident** | none | no | 1 call | floor baseline |

**Recommended Phase-0 shortlist (pilot 3–4):** verbalized (floor) + **DINCO (primary)** + a **logprob/yes-no
token** variant *iff* the chosen model exposes logprobs + a sampling option (**self-consistency or
FactSelfCheck-style**). **Phase-0 selection metric: tail-AUC > 0.5 with CI** on a labeled slice (AUC of
true-vs-false restricted to the admission tail), **plus isolated≈batched agreement** (D.3).

### F.3 Coupling to Sub-task G (contingency)

If no affordable model exposes usable logprobs, **drop the logprob elicitation**; **DINCO + verbalized +
self-consistency/FactSelfCheck** carry Phase-0 (all logprob-free). The pilot is thus codeable regardless of
logprob availability.

---

## G. OpenRouter model: logprobs + prompt caching + sub-$0.30/M pricing

### G.1 The central tension

Cheap auto-caching models (DeepSeek, Gemini Flash tier) cache the document prefix well but expose token
`logprobs` unevenly through OpenRouter; the **OpenAI GPT-4.1 family** reliably exposes `logprobs`/`top_logprobs`
*and* auto-caches — and the **nano** tier is under the $0.30/M input cap. OpenRouter supports `logprobs` +
`top_logprobs` (an integer 0–20 most-likely tokens per position; `logprobs` must be `true`), available for **all
xAI models, the OpenAI GPT-4.1 series, and several open-weight models (5–20 logprobs)** [18].

### G.2 Concrete model table (current OpenRouter pricing)

| model id | input $/M | output $/M | cache-read mult. | caching | logprobs? | notes |
|----------|-----------|------------|------------------|---------|-----------|-------|
| **openai/gpt-4.1-nano** | **$0.10** [16] | $0.40 [16] | 0.25–0.5× (writes free) [15] | auto (implicit) | **yes** (GPT-4.1 series) [18] | **PRIMARY** — cheapest with logprobs+caching |
| openai/gpt-4o-mini | $0.15 [17] | $0.60 [17] | 0.5× (writes free) [15] | auto | **yes** [18] | fallback 1 (more capable) |
| openai/gpt-4.1-mini | $0.40 [17] | $1.60 [17] | 0.25–0.5× | auto | yes [18] | **EXCEEDS $0.30 input cap** — excluded |
| deepseek (V3 tier) | sub-$0.30 (verify) | — | implicit/auto [15] | auto | **uneven via OR** | fallback 2 (**logprob-free** path) |
| google/gemini-flash-lite tier | sub-$0.30 (verify) | — | implicit caching [15] | auto | uneven | logprob-free path |

`[15]` = OpenRouter prompt-caching doc. Cache-read multipliers per provider [15]: **OpenAI** writes free /
reads **0.25× or 0.5×**; **Grok (xAI)** reads 0.25×; **Moonshot** reads 0.25×; **Groq** reads 0.5×; **Alibaba
Qwen** writes **1.25×** / reads **0.1×** (needs explicit `cache_control:{"type":"ephemeral"}`, 5-min TTL);
**Anthropic** needs explicit `cache_control` breakpoints, negative discount on writes (≈1.25×) / positive on
reads (≈0.1×); **DeepSeek & Gemini 2.5** = implicit/automatic. Cache hits are verifiable via
`usage.prompt_tokens_details.cached_tokens` (and `cache_write_tokens`) on every response [15].

### G.3 Budget arithmetic (validated against the hard cap)

Workload ≈ **14.4K isolated scoring calls + ~0.7K generation calls + pilot ≈ 15.1K calls**, ~**450 input +
~30 output tokens/call** ⇒ ~**6.8M input + ~0.45M output** (≈7M; upper-bound design ~15M).

- **gpt-4.1-nano** (no caching): `6.8M×$0.10/M + 0.45M×$0.40/M = $0.68 + $0.18 = $0.86`. With document-prefix
  caching (≈400 of 450 input tokens cached at 0.25–0.5×): input → ~$0.30–0.45 ⇒ **≈ $0.5–0.7**.
- **gpt-4.1-nano** (15M upper-bound, ~14M in/1M out): `$1.40 + $0.40 = $1.80` uncached → **≈ $1.0–1.5** cached.
- **gpt-4o-mini** (15M): `14M×$0.15 + 1M×$0.60 = $2.10 + $0.60 = $2.70` uncached → **≈ $1.5–2.5** cached.

All land in the **~$1–3 zone, well under the $10 hard cap** [15,16,17].

### G.4 Recommendation

- **PRIMARY: `openai/gpt-4.1-nano`** ($0.10/$0.40, logprobs ✓, auto-cache) — enables **all** Sub-task F
  elicitations including the **logprob/yes-no-token** variant.
- **FALLBACK 1: `openai/gpt-4o-mini`** ($0.15/$0.60, logprobs ✓) — same capabilities, more headroom/quality.
- **FALLBACK 2 (logprob-free): a cheap auto-caching model (DeepSeek V3 / Gemini Flash-Lite tier)** — run
  **DINCO + verbalized + self-consistency/FactSelfCheck** (F.3) so the pipeline is never blocked if logprobs are
  unavailable.
- **Runtime gate (follow-up):** the method-executor must **probe logprobs return non-null on a 1-call test**
  and **confirm `cached_tokens > 0`** before committing the budget. If the probe fails on nano, fall to the
  logprob-free path on Fallback 2.

---

## H. Novelty-positioning note

A targeted sweep finds **no prior work that applies knockoff / target-decoy / entrapment competition FDR control
at an LLM neuro-symbolic (text-to-logic) admission boundary, label-free.** The nearest families all (a) require
**labeled** calibration data and/or (b) certify the **output**, not the **admission** of intermediate
facts/bridges into a symbolic layer:

- **Conformal factuality** (Mohri & Hashimoto, ICML 2024, arXiv 2402.10978): splits LLM output into atomic
  sub-claims and filters those below a conformal factuality threshold for a marginal correctness guarantee —
  but the threshold is set on a **labeled calibration set** and it certifies the **emitted answer** [19].
- **Coherent factuality** (arXiv 2505.17126) extends this to reasoning chains — still conformal/labeled [21].
- **Conformal selection / Selection by Prediction with Conformal p-values** (Jin & Candès, JMLR 2023, arXiv
  2210.01408): wraps any predictor to select candidates while controlling FDR — but needs **labeled
  calibration outcomes** [20].
- Conformal-Labeling / risk-controlling extraction for clinical entities (e.g. arXiv 2603.00924): FDR/RCPS
  guarantees, again **conformal (labeled)**.
- LINC / Logic-LM and ontology-constraint filtering (ODKE+/SHACL): symbolic-side filtering, not a statistical
  FDR knob and not decoy-based.

**Near-miss to report (not a pre-emption):** *"Neuro-Symbolic Verification for Preventing LLM Hallucinations in
Process Control"* (MDPI Processes 2024) uses **Abductive Logic Programming coherence + counter-abduction** to
score LLM explanations [22] — same neuro-symbolic-anti-hallucination *spirit* but a **logic-coherence** method,
**not** decoy-competition FDR and **not** an admission-boundary FDR knob.

**Differentiator (one line for the paper):** *ours is the first to convert the proteomics target-decoy/knockoff
competition machinery into a **label-free**, finite-sample FDR knob that gates the **text→logic admission
boundary**, using **counterfactual decoys** as the negative control in place of a labeled calibration set.*
Confirmatory searches ("knockoff filter LLM hallucination", "target-decoy competition language model fact
extraction", "FDR control neuro-symbolic admission") surfaced only proteomics TDC/knockoff work and conformal
(labeled) LLM methods — **no 2025–2026 preprint pre-empts the claim.**

---

## Parameter Defaults table (recommended values + justification)

| Parameter | Default | Justification / source |
|-----------|---------|------------------------|
| **α grid** | `{0.05, 0.10, 0.20, 0.30, 0.50}` | each tied to k-floor `⌈1/α⌉` = {20,10,5,4,2} (A.3) |
| **FDR estimator (admission)** | knockoff+ eq. 1.9 | exact finite-sample FDR (Thm 2 [1]); keep the `+1` (Thm 2 [2]) |
| **Tolerance τ (FDR-vs-α slack)** | `0.05` absolute | small slack absorbs the `1/k` granularity (A.3) without masking real anti-conservatism; report sensitivity to τ∈{0,0.05} |
| **N_false_min** | `40` | from hypothesis; ensures ≥ k-floor for the demonstrable α grid and stable tail diagnostics |
| **Entrapment ratio r** | `1` (paired, eq. 4) | tightest valid upper bound; matches r=1 one-to-one pairing [5,7]; combined (eq. 1) when pairing unavailable |
| **Entrapment estimator** | paired (default), combined (fallback) | both valid upper bounds [5]; never `sample` (eq. 3, invalid) |
| **Bootstrap B** | `≥ 2000` | stable 2.5/97.5 percentile CI; document-block resampling (C) |
| **Bootstrap unit** | whole document (cluster) | within-doc score dependence → cluster bootstrap [8] |
| **Self-consistency N** (if used) | `5–10` | DINCO @10 calls > self-consistency @100 [12]; start at 10, drop if cost-bound |
| **Tail cutoff** | `= operative knockoff+ t` | "tail" = admission region `W ≥ t` (D.4) |
| **Scoring regime** | isolated, provenance-blinded, order-randomized | avoids batched contrast effect (D.2 channel #2); caching buys headroom |
| **Decoy family** | document-conditioned counterfactual + non-entailment gate | property-matched principle (DeepCoy [9]); random swap = negative control |
| **Tail tests** | one-sided KS (+ tail Mann–Whitney) on `W ≥ t` | exchangeability diagnostics, measurement-only (D.4) |
| **Primary model** | `openai/gpt-4.1-nano` | $0.10/$0.40, logprobs+caching, <$0.30 input [16,18]; fallbacks gpt-4o-mini, then logprob-free DeepSeek/Gemini |
| **Budget** | ≈ $1–3 (hard cap $10) | G.3 arithmetic [15,16,17] |

---

## Follow-up questions (runtime-only; cannot be resolved by this research artifact)

1. Does `openai/gpt-4.1-nano` (selected provider route) return **non-null** `logprobs`/`top_logprobs` on a
   1-call probe through OpenRouter? If not, fall to the logprob-free elicitation path (F.3).
2. Does the document-prefix `cache_control` (or implicit caching) actually yield measured
   `usage.prompt_tokens_details.cached_tokens > 0` on the second call, and at the expected 0.25–0.5× read price?
3. On the CLUTRR labeled slice, does the **tail-conditioned win-rate** sit at ≈0.5 for counterfactual decoys
   (validity) and measurably <0.5 for random type-matched swaps (the predicted anti-conservative control)?


---

## Sources by sub-task
- **A (knockoff+/TDC + 1/k floor):** [1] Barber & Candès; [2] Rajchert & Keich; [3] Ebadi et al.; [4] bandsfdp.
- **B (entrapment estimators / ratio r):** [5] Wen et al. (Nature Methods); [6] FDRBench; [7] OmniNovo.
- **C (document-block bootstrap):** [8] Cameron, Gelbach & Miller.
- **D (null sign-flip + failure modes):** [1] Barber & Candès (Lemma 1); [5] Wen et al. (equal-chance).
- **E (property-matched / counterfactual decoys):** [9] DeepCoy.
- **F (upper-tail elicitations):** [10] Xiong; [11] Tian; [12] DINCO; [13] SelfCheckGPT; [14] FactSelfCheck.
- **G (OpenRouter model + caching + pricing):** [15] caching doc; [16] gpt-4.1-nano; [17] gpt-4o-mini/4.1-mini; [18] parameters/logprobs.
- **H (novelty):** [19] Mohri & Hashimoto; [20] Jin & Candès; [21] coherent factuality; [22] MDPI neuro-symbolic.


## Sources

[1] [Barber & Candès 2015 — Controlling the FDR via Knockoffs (Annals of Statistics 43(5))](https://arxiv.org/pdf/1404.5609) — Source of the knockoff (Def 1, eq 1.8, modified-FDR Thm 1) and knockoff+ (Def 2, eq 1.9, exact-FDR Thm 2) data-dependent thresholds, the antisymmetry property (Def 4), and Lemma 1 (i.i.d. fair-coin signs for the nulls) — the null sign-flip validity condition.

[2] [Rajchert & Keich 2022 — Controlling the FDR via Competition: is the +1 needed?](https://arxiv.org/pdf/2204.13248) — Proves the '+1' is in general NECESSARY: Thm1/Cor1 (reducing the additive constant in (1−1/b,1] leaves the discovery list unchanged) and Thm2/Cor2 (for the a=1 case t=1 is optimal; any t<1 either changes nothing or fails to control FDR, with an explicit counterexample). Applies to TDC.

[3] [Ebadi, Luo, Freestone, Noble & Keich 2023 — Bounding the FDP in competition-based control of the FDR (TDC-SB/TDC-UB)](https://arxiv.org/pdf/2302.11837) — Upper prediction bounds on the FDP for competition-based FDR (TDC-SB standardized band, TDC-UB uniform band) via the negative-binomial decoy-win process; significantly tighter than Katsevich–Ramdas (median bounds γ=0.01: 0.087/0.094/0.243; γ=0.05: 0.079/0.083/0.189).

[4] [CRAN bandsfdp::tdc_ub — Uniform Band upper prediction bound on TDC's FDP](https://search.r-project.org/CRAN/refmans/bandsfdp/html/tdc_ub.html) — Reference implementation of TDC-UB/TDC-SB: tdc_ub(thresholds, labels, alpha, gamma, c=0.5, lambda=0.5, n, interpolate=TRUE); gamma is the confidence parameter (0.05/0.01); portable to Python.

[5] [Wen, Freestone, Riffle, MacCoss, Noble & Keich 2025 — Assessment of FDR control using entrapment (Nature Methods 22:1454, full text)](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12240826/fullTextXML) — Verbatim entrapment FDP estimators: lower bound (eq2, N_E/(N_T+N_E)), combined (eq1, N_E(1+1/r)/(N_T+N_E), upper bound), sample (eq3, N_E(1/r)/N_T, INVALID), paired (eq4, requires r=1, tighter). Defines r=#entrapment/#target and the equal-chance assumption; explains why 'sample' is biased.

[6] [FDRBench (Noble-Lab) — entrapment database generation + FDP estimation tool](https://github.com/Noble-Lab/FDRBench) — Confirms the three estimation methods (lower bound, combined, paired) and the CLI flag -r = #entrapment/#target (database-size ratio); shuffled vs foreign-species entrapment construction.

[7] [OmniNovo 2025 — de novo sequencing (applies Wen et al. paired entrapment)](https://arxiv.org/pdf/2512.12272) — Independent application confirming the r=1 one-to-one paired entrapment-based FDP estimation 'following the framework proposed by Wen et al.' (target↔unique entrapment pairing).

[8] [Cameron, Gelbach & Miller 2008 — Bootstrap-Based Improvements for Inference with Clustered Errors (RESTAT 90(3):414-427)](https://direct.mit.edu/rest/article/90/3/414/57731/Bootstrap-Based-Improvements-for-Inference-with) — Methods anchor for the document-block bootstrap: pairs cluster bootstrap and wild cluster bootstrap correct anti-conservative inference under within-cluster dependence; resample whole clusters (documents).

[9] [Imrie, Bradley & Deane 2021 — Generating property-matched decoy molecules using deep learning (DeepCoy)](https://academic.oup.com/bioinformatics/article/37/15/2134/6126797) — Load-bearing decoy principle: decoys must reproduce the property/score distribution of true positives ('not too easy'); too-easy decoys make estimated FDR optimistic. DOE improved 0.166→0.032 (DUD-E, 81%) and 0.109→0.038 (DEKOIS 2.0, 66%) with no added false-negative risk.

[10] [Xiong et al. 2024 (ICLR) — Can LLMs Express Their Uncertainty? Confidence Elicitation in LLMs](https://arxiv.org/abs/2306.13063) — Verbalized confidence is OVERCONFIDENT in the upper tail (imitating human patterns); calibration improves with scale but stays far from ideal; human-inspired prompting mitigates with diminishing returns in advanced models.

[11] [Tian et al. 2023 (EMNLP) — Just Ask for Calibration (RLHF-LM confidence)](https://aclanthology.org/2023.emnlp-main.330/) — For RLHF LMs (ChatGPT/GPT-4/Claude) verbalized confidences are typically BETTER calibrated than the model's conditional (log)probabilities on TriviaQA/SciQ/TruthfulQA — i.e. logprob calibration degrades under RLHF.

[12] [DINCO 2025 (ICLR 2026) — Distractor-Normalized Coherence](https://arxiv.org/html/2509.25532v1) — Verbalize confidence across self-generated distractors and normalize by the total (eq2: β(C)≈Σ f_VC(c), f_NVC(c)=f_VC(c)/β(C), β←max(1,β)); NLI down-weights non-contradicting distractors; integrates self-consistency. ECE improved over best baseline by 0.077/0.092/0.055; DINCO@10 calls > self-consistency@100; relieves saturation.

[13] [Manakul, Liusie & Gales 2023 — SelfCheckGPT (zero-resource black-box hallucination detection)](https://arxiv.org/abs/2303.08896) — Sampling-based self-consistency scoring: sample N completions and score by agreement; black-box, no logprobs, N× cost; consistency-across-generations correlates with correctness.

[14] [Sawczyn et al. 2025 — FactSelfCheck: Fact-Level Black-Box Hallucination Detection](https://arxiv.org/pdf/2503.17229) — Zero-resource black-box fact-level detection: represents output as KG triples (h,r,t), computes per-fact hallucination score H_fact from consistency across N samples (KG or text variant). Native fact-level granularity; improves correction 35.5% vs SelfCheckGPT 10.6%.

[15] [OpenRouter — Prompt Caching documentation](https://openrouter.ai/docs/features/prompt-caching) — Per-provider cache multipliers: OpenAI writes free/reads 0.25×–0.5×; Grok 0.25×; Moonshot 0.25×; Groq 0.5×; Qwen writes 1.25×/reads 0.1× (explicit cache_control); Anthropic explicit (writes ~1.25×/reads ~0.1×); DeepSeek/Gemini implicit. Cache hits verified via usage.prompt_tokens_details.cached_tokens.

[16] [OpenRouter — GPT-4.1-nano pricing page](https://openrouter.ai/openai/gpt-4.1-nano) — Confirms gpt-4.1-nano at $0.10/M input, $0.40/M output (<$0.30 input cap); GPT-4.1 series exposes logprobs; auto-caching. Recommended PRIMARY model.

[17] [OpenRouter — GPT-4.1-mini / GPT-4o-mini pricing](https://openrouter.ai/openai/gpt-4.1-mini) — gpt-4o-mini $0.15/M in, $0.60/M out (fallback 1); gpt-4.1-mini $0.40/M in, $1.60/M out (EXCEEDS the $0.30 input cap, excluded).

[18] [OpenRouter — API parameters (logprobs / top_logprobs)](https://openrouter.ai/docs/api/reference/parameters) — logprobs/top_logprobs supported (integer 0–20 tokens/position; logprobs must be true). Available for all xAI models, the OpenAI GPT-4.1 series, and several open-weight models (5–20 logprobs).

[19] [Mohri & Hashimoto 2024 (ICML) — Language Models with Conformal Factuality Guarantees](https://arxiv.org/abs/2402.10978) — Novelty differentiator: splits output into atomic sub-claims and filters below a conformal factuality threshold for a marginal guarantee — but the threshold is set on a LABELED calibration set and it certifies the OUTPUT, not a label-free admission boundary.

[20] [Jin & Candès 2023 (JMLR) — Selection by Prediction with Conformal p-values (Conformal Selection)](https://arxiv.org/pdf/2210.01408) — Novelty differentiator: wraps any predictor to select candidates while controlling FDR — but requires LABELED calibration outcomes; not decoy-based and not at a text→logic admission boundary.

[21] [Conformal LM Reasoning with Coherent Factuality 2025](https://arxiv.org/pdf/2505.17126) — Extends conformal factuality to reasoning chains (coherent factuality); still conformal/labeled — differentiated from the label-free decoy-competition gate.

[22] [Neuro-Symbolic Verification for Preventing LLM Hallucinations in Process Control (MDPI Processes 2024)](https://www.mdpi.com/2227-9717/14/2/322) — Nearest-spirit near-miss: uses Abductive Logic Programming coherence + counter-abduction to score LLM explanations — a logic-coherence method, NOT decoy-competition FDR and not an admission-boundary FDR knob.

## Follow-up Questions

- Does openai/gpt-4.1-nano (on the actually-selected OpenRouter provider route) return non-null logprobs/top_logprobs on a 1-call probe? If not, the pipeline must fall back to the logprob-free elicitation path (DINCO + verbalized + self-consistency/FactSelfCheck).
- Does document-prefix caching (implicit, or explicit cache_control) yield measured usage.prompt_tokens_details.cached_tokens > 0 on the second call and the expected 0.25-0.5x cache-read price, so the ~$1-3 budget projection holds?
- On the CLUTRR labeled slice, is the tail-conditioned win-rate ~0.5 for document-conditioned counterfactual decoys (validity) and measurably <0.5 for random type-matched swaps (the predicted anti-conservative control), and does isolated scoring restore the FDR-vs-alpha diagonal where batched scoring does not?

---
*Generated by AI Inventor Pipeline*
