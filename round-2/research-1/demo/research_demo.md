# Novelty-Delta, Upper-Ontology Grounding Recipe, and LLM-as-Probabilistic-Reasoner Design

## Summary

Source-traceable research closing three iteration-1 reviewer gaps for the decoy-gated neuro-symbolic text-to-logic pipeline, extending (not contradicting) Spec A (FDR gate) and Spec B (pipeline/typing/trace-graph). PART A: a five-dimension NOVELTY-DELTA table pinning six nearest conformal/FDR neighbors - Jin-Candes conformal selection [1], Li-Magesh-Veeravalli multiple-testing hallucination detection [2], COCOCO neuro-symbolic conformal sets [3], Bashari conformal-e-value novelty detection [4], Marandon/Blanchard conformal link-prediction FDR [5,6], Mohri-Hashimoto conformal factuality [7] - on {label requirement, unit certified, exchangeability mechanism, decoy?, FDR-vs-coverage}; all are LABELED and certify a model OUTPUT under assumed exchangeability, whereas OURS is label-free, certifies the INTERMEDIATE text->logic admission, uses engineered+tested decoy sign-flip, and controls FDR. Includes a paste-ready one-sentence delta, a 'not just conformal selection' rebuttal, and an honest adversarial result (no 2025-2026 preprint pre-empts the construction). PART B: OpenCyc honestly reported as discontinued (March 2017 [8,9], third-party-mirror-only [10]) and ResearchCyc as license-gated [8]; a concrete offline-first two-layer argument-typing recipe - WordNet hypernyms [11] anchored to SUMO upper-ontology classes via WordNetMappings30 (verified line: person -> &%Human=) [12,13,14], plus Wikidata P31/P279* [17] or offline YAGO 4.5 [15,16] instance typing, loadable with owlready2/SPARQLWrapper [18] - and a loss/sufficiency/descope-vs-defer justification arguing why typing-only usage cannot break the FDR guarantee (unlike ontology-constraint filtering). PART C: a concrete LLM-as-probabilistic-reasoner design - ProbLog primary (verified API: get_evaluatable().create_from(PrologString).evaluate() -> {Term:prob}; p::fact.; annotated disjunctions; query/evidence; explain/MPE proofs [19,20,21]; LFI weight learning [22]; aProbLog semirings [23]; DeepProbLog neural-predicate precedent [24]) with Bousi~Prolog/FASILL as the fuzzy-unification alternative [25,26,27,28]; a certificate->probabilistic-weight mapping table (p_i=calibrate(Z_i); gate-consistent shrinkage (1-alpha_hat)*p_i [default] or per-pair W_i margin weight; entrapment FDP-hat as consistency prior; full cert kept at the leaf); a probabilistic trace-graph export (reuse Spec-B JSON/Graphviz-DOT, add a 'prob' attribute per node/edge, marginal per derived node, certificate per leaf; janus-swi solve/2 fallback for the proof DAG); and the exact deterministic->probabilistic upgrade swap (janus query_once -> problog get_evaluatable/evaluate). Deliverables: research_out.json + research_report.md with 30 primary sources, tables, recipes, exact APIs, and a positioning note mapping each part to the named reviewer gaps.

## Research Findings

# Novelty-Delta Table, Real Upper-Ontology Grounding Recipe, and the LLM-as-Probabilistic-Reasoner Design at Fuzzy Unifications

> **Scope and continuity.** This artifact closes three reviewer gaps left open by iteration‑1 of the decoy‑gated
> neuro‑symbolic extraction hypothesis. It **extends, and does not contradict**, the two iteration‑1 dependency specs:
> *Spec A* (the label‑free FDR gate — knockoff statistic `W_i = (Z_i ∨ Z̃_i)·sign(Z_i − Z̃_i)`, the knockoff+ threshold
> `T = min{t : (1+#{W_i ≤ −t})/(#{W_i ≥ t} ∨ 1) ≤ α}`, the entrapment bound `FDP̂ = N_E(1+1/r)/(N_T+N_E)`, the certificate
> fields `cert(W_i, T, q/α, FDP̂, r)`, DINCO/FactSelfCheck elicitation, and the Section‑H novelty note that already
> contrasts Mohri–Hashimoto / Jin–Candès / coherent factuality) and *Spec B* (the janus‑swi deterministic `solve/2`
> meta‑interpreter, the provenance+decoy+entrapment trace‑graph JSON/Graphviz‑DOT format, and the WordNet‑hypernym coarse
> typer into `{PER,LOC,ORG,TIME,NUM,MISC}`). **PART A** turns Spec‑A's novelty note into a full table; **PART B** extends
> Spec‑B's typing block with a real upper‑ontology anchor; **PART C** extends Spec‑B's deterministic meta‑interpreter into
> a probabilistic engine. All new symbol names and the certificate schema are kept drop‑in compatible. Citations `[n]`
> index the Sources section. This is pure web research — no code was executed, no datasets downloaded.

---

## PART A — The Novelty‑Delta Table (reviewer gap: *novelty MINOR*)

### A.1 The nearest neighbors, pinned on five dimensions

Every row below was verified by fetching the primary source and `grep`‑ing for the load‑bearing claim (label requirement,
unit certified, exchangeability mechanism, decoy?, FDR‑vs‑coverage). Verbatim anchors are quoted in A.2.

| # | Method (source) | (1) Label requirement | (2) Unit certified | (3) Exchangeability mechanism | (4) Decoy / competition‑based? | (5) Controls FDR or coverage? |
|---|---|---|---|---|---|---|
| 1 | **Conformal Selection** — Jin & Candès 2023 [1] | **Labeled** calibration set with observed outcomes `Y` | A **selected shortlist of test candidates** (model OUTPUT) | Conformal exchangeability of labeled calibration ∪ test, BH on conformal p‑values | **No** | **FDR** (BH on conformal p‑values) |
| 2 | **Multiple‑testing hallucination detection** — Li, Magesh & Veeravalli 2025 [2] | **Labeled** calibration set of *non‑hallucinated* prompts (ROUGE‑L labels) | The **generation / prompt** (flags a hallucinated OUTPUT) | Conformal p‑values `q^j = (1+#{i: s^j_i ≥ t^j})/(1+|C|)` against calibration `C` | **No** | **False‑alarm / FDR** at the generation level (BH/BY) |
| 3 | **COCOCO** — Concise & Logically Consistent Conformal Sets for NeSy‑CBMs 2026 [3] | **Labeled** calibration set | **Concept + label prediction SETS** (OUTPUT of a NeSy concept model) | Conformal exchangeability + e‑values, deduction–abduction revision | **No** | **Distribution‑free COVERAGE** (+ consistency, conciseness) — *not* FDR |
| 4 | **Derandomized novelty detection** — Bashari et al. 2023 [4] | **Labeled‑ish** inlier / reference set | **Which test points are novel/outliers** (OUTPUT selection) | Conformal e‑values + **e‑BH** (derandomized) | **No** | **FDR** |
| 5 | **Conformal link prediction** — Marandon 2023 [5]; Blanchard et al. 2024 [6] | **Observed‑graph labels** (sampled true/false edges) | **Predicted true edges** (OUTPUT) | Graph‑adapted conformal (explicitly *non‑standard* exchangeability) | **No** | **FDR** (+ uniform FDP bounds [6]) |
| 6 | **Conformal factuality** — Mohri & Hashimoto 2024 [7] | **Labeled** calibration set | **Retained sub‑claims of the emitted answer** (OUTPUT) | Conformal exchangeability, score quantile back‑off | **No** | **Factuality / coverage‑type** guarantee |
| — | **OURS** (decoy‑gated text→logic admission) | **Label‑free** (zero operation labels) | The **INTERMEDIATE admission** of facts/bridges *into* the symbolic layer (a boundary, not an output) | **Engineered + empirically‑tested decoy sign‑flip** (knockoff+/TDC, Spec‑A), independently corroborated by **entrapment** | **YES** — decoy competition is the mechanism | **FDR** (finite‑sample exact via knockoff+) |

### A.2 Verbatim anchors (verified via fetch_grep)

- **Jin & Candès [1]** — labeled calibration + output selection + BH: *"the procedure selects candidates whose predictions
  are above a data‑dependent threshold … Our theoretical guarantee holds under mild exchangeability conditions"*; the FDP
  is *"computed by averaging … in N=100 independent splits of training, **calibration**, and test data"*; the algorithm
  *"turns any prediction model into a screening mechanism"* by applying BH to conformal p‑values built on a *"prediction
  model from a training process that is independent of the **calibration** and test samples."* [1]
- **Li, Magesh & Veeravalli [2]** — labeled non‑hallucinated calibration, false‑alarm control: *"our framework adds a
  lightweight calibration step that uses a **small calibration set of non‑hallucinated prompts** to provide theoretical
  control of the **false‑alarm rate**"*; conformal p‑values `q^j_con = (1+|{i: s^j_i ≥ t^j_test}|)/(1+|C|)` are computed
  against the calibration set `C` of prompts that do not generate hallucinations. [2]
- **COCOCO [3]** — coverage (not FDR), labeled, deduction‑abduction, certifies concept/label sets: *"integrating ideas from
  Conformal Prediction (CP), a framework providing rigorous, **distribution‑free coverage** guarantees … COCOCO, a post‑hoc
  framework that conformalizes concepts and labels jointly and reconciles them via a single **deduction–abduction** revision
  step … retains distribution‑free **coverage** … leverage e‑values to ensure the prediction sets attain maximal coverage
  for any given size budget."* This is the closest *neuro‑symbolic + conformal* neighbor, and it conformalizes the
  concept‑bottleneck **OUTPUT** under fixed logical constraints. [3]
- **Bashari et al. [4]** — conformal e‑values + e‑BH, reference/inlier calibration, certifies test points: *"leveraging
  suitable conformal e‑values instead of p‑values … provably controlling the false discovery rate"*; the *"calibration
  procedure yields a conformal p‑value that can be utilized to test for outliers … incorrectly labeling an **inlier** data
  point as an outlier."* [4]
- **Marandon [5]** — identifies true edges with FDR control, graph dependence ≠ standard exchangeability: *"we consider the
  problem of identifying a set of true edges with a control of the false discovery rate (FDR) … The graph structure induces
  intricate dependence in the data, which we carefully take into account, as this makes the setup different from the usual
  setup in conformal inference, where data **exchangeability** is assumed."* Blanchard et al. [6] prove FDR control and add
  uniform FDP bounds.
- **Mohri & Hashimoto [7]** — labeled calibration, certifies emitted output (from Spec‑A and the conformal‑factuality
  algorithm): splits output into atomic sub‑claims and back‑off‑filters those below a conformal threshold set on a
  **labeled calibration set**, certifying the emitted answer.

### A.3 The one‑sentence delta (paste into the paper)

> *Unlike every conformal selection / factuality / novelty / link method — all of which require a **labeled** calibration
> or reference set and certify a model **output** (a selected shortlist, a retained‑sub‑claim answer, a novel‑point set, a
> concept/label set, or a predicted link) under **conformal or graph exchangeability assumed from labeled data** — ours is
> the first **label‑free, decoy‑competition** FDR knob that gates the **intermediate neural‑to‑symbolic admission boundary**
> (the entry of extracted facts/bridges into the Prolog layer), with exchangeability **engineered and empirically tested in
> the score tail** rather than assumed, and independently corroborated by an entrapment bound.*

### A.4 Rebuttal paragraph — defusing "this is just conformal selection at the fact level"

> Conformal selection (Jin & Candès [1]) and its hallucination‑detection descendant (Li–Magesh–Veeravalli [2]) both require
> **labeled outcomes**: a calibration set of observed `Y`'s (or of verified non‑hallucinated prompts) whose exchangeability
> with the test set is what licenses the conformal p‑value and the BH guarantee. They certify a **model output** — a
> selected candidate set or a flagged generation. Our setting has **zero operation labels**: there is no annotated
> "this fact is true" calibration corpus, and the gate sits *before* symbolic propagation, deciding which extracted
> facts/bridges may even **enter** the reasoner. We manufacture the needed null behavior with **document‑conditioned
> counterfactual decoys** and *test* the fair‑coin sign‑flip property in the tail (Spec‑A's D.4 diagnostics), rather than
> importing it from a labeled calibration set. That makes the method a label‑free FDR knob on an **admission boundary**, a
> different object from conformal selection's labeled output certificate.

### A.5 Adversarial novelty check (honest result)

Three confirmatory searches — "knockoff filter LLM hallucination fact extraction admission FDR", "target‑decoy competition
language model text‑to‑logic label‑free FDR knowledge‑base admission", and the dependency's own sweep — surfaced **only**
(a) proteomics/statistics target‑decoy & knockoff work (Barber–Candès, TDC, Group‑walk, null‑free decoy permutations
[generic]) and (b) **labeled** conformal LLM methods (the rows above). The nearest *spirit*‑neighbor remains the MDPI
"Neuro‑Symbolic Verification for Preventing LLM Hallucinations in Process Control" (Abductive‑Logic‑Programming coherence,
*not* a decoy‑competition FDR knob). **No 2025–2026 preprint pre‑empts the claim** of a label‑free decoy/knockoff FDR gate
at an LLM text→logic admission boundary. Confidence: **high** for the negative result on the exact construction; **medium**
that no very‑recent unindexed preprint exists.

---

## PART B — Real Upper‑Ontology Grounding Recipe + OpenCyc‑Substitution Justification (reviewer gap: *scope MAJOR*)

### B.1 OpenCyc / ResearchCyc status — why a commodity substitute is required

| Resource | Access route | Offline & reproducible? | License | Verdict |
|---|---|---|---|---|
| **OpenCyc 4.0** | Discontinued by Cycorp **March 2017** [8,9]; legacy OWL dumps survive only via third‑party mirrors (SourceForge `opencyc`, GitHub `asanchez75/opencyc`) [10] | Mirror download yes, but **unmaintained, unsupported** | Apache‑2.0 (legacy) on mirrors | **Not** a reproducible commodity dependency |
| **ResearchCyc / Cyc** | License application to Cycorp (`info@cyc.com`) [8] | **No** — not pip/anonymous‑downloadable; larger curated KB | Research/commercial license | Not commodity / not offline |

Verbatim: *"As of March 2017, Cycorp, the developer of OpenCyc, ceased online support for its knowledge base"* [9];
*"Cycorp has pulled OpenCyc from the marketplace … versions of OpenCyc v 4.0 can still be downloaded from third parties,
including a fork"* [8]; the standing recommendation is to *"contact info@cyc.com to obtain a research license or a
commercial license to Cyc itself"* [8]. **Conclusion:** OpenCyc/ResearchCyc cannot be a reproducible, commodity, offline
dependency for a public pipeline that must be "highly reproducible on any short, professionally written documents". A
commodity substitute is mandatory; the substitution must be argued (B.4), not glossed.

### B.2 Survey of real substitute options

| Substitute | Access / offline | License | Python library | Taxonomy it supplies |
|---|---|---|---|---|
| **WordNet hypernyms (NLTK)** [11] | Offline (`nltk.download('wordnet')`) | BSD‑style | `nltk.corpus.wordnet`, `synset.hypernym_paths()` | Lexical sense hierarchy (the Spec‑B coarse typer) |
| **SUMO** — Suggested Upper Merged Ontology [12,13,14] | Offline (git clone) | IEEE‑owned, GNU GPL code [12] | parse `WordNetMappings30-*.txt`; Sigma for inference | **Genuine formal upper ontology** in SUO‑KIF; **every WordNet synset mapped to a SUMO class** [13,14] |
| **YAGO 4 / 4.5** [15,16] | Offline (Turtle: Schema / Taxonomy / Facts) | CC‑BY | `rdflib`, any triple store (Jena, GraphDB, QLever) | schema.org upper classes + cleaned Wikidata taxonomy; instance typing for named entities |
| **Wikidata class hierarchy** [17] | Live SPARQL endpoint (`query.wikidata.org`) | CC0 | `SPARQLWrapper` (`setQuery`/`setReturnFormat(JSON)`/`query().convert()`) | `P31`/`P279*` instance/subclass hierarchy (network‑dependent) |
| **DBpedia ontology** (Spec‑B note) | SPARQL | CC‑BY‑SA | `SPARQLWrapper` | `dbo:Person/Place/Organisation` named‑entity typing |
| **owlready2** (loader, not an ontology) [18] | Offline OWL/RDF reasoning | LGPL | `get_ontology("file://…").load()`, `.search(subclass_of=…)`, `sync_reasoner` | Loads a local `.owl` (e.g. SUMO.owl) for class lookups |

**Why SUMO is the OpenCyc analogue.** SUMO is *"the only formal ontology that has been mapped to all of the WordNet
lexicon"* [14], is *"written in SUO‑KIF"*, *"free and owned by the IEEE"* (code under GNU GPL) [12], and ships the mapping
files `WordNetMappings30-{noun,verb,adj,adv}.txt` [12,13]. It therefore supplies a **real upper‑ontology class for each
WordNet sense**, letting the pipeline make a legitimate "upper‑ontology taxonomic grounding" claim — exactly the
`OpenCyc`‑role the goal text names — without a license or a discontinued dump.

### B.3 The concrete two‑layer argument‑typing recipe (the deliverable)

**LAYER 1 — argument typing (offline; used for decoy generation + entity linking).**
For each extracted argument's head noun:

1. `paths = wn.synsets(word, pos=wn.NOUN)[0].hypernym_paths()` (NLTK [11]).
2. Map to the Spec‑B coarse set via anchor synsets: `person.n.01 → PER`, `location.n.01 / region.n.03 → LOC`,
   `organization.n.01 / social_group.n.01 → ORG`, `time_period.n.01 → TIME`, `number.n.02 / measure.n.02 → NUM`,
   else `MISC`.
3. **Anchor each coarse type to its SUMO upper‑ontology class** by looking up the head synset's SUMO term in
   `WordNetMappings30-noun.txt` [13]. The mapping line carries the SUMO term with a relation suffix
   (`=` equivalence, `+` subsumption, `@` instance). *Verified real line:* the `person` synset (`00015388`) maps as
   `… a human being … &%Human=` [13]. Recommended coarse→SUMO anchors (all genuine SUMO classes):
   `PER → &%Human`, `LOC → &%GeographicArea`, `ORG → &%Organization`, `TIME → &%TimePosition`, `NUM → &%Number`,
   `MISC → &%Entity`.

   *Worked example:* `"plaintiff"` → WordNet `person.n.01` → coarse `PER` → SUMO `&%Human`.

**LAYER 2 — named‑entity instance typing (for the ~15–30 professional‑doc slice).**
Resolve linked entities to a class via the Wikidata property path `?e wdt:P31/wdt:P279* ?class` [17] (one `instance‑of`
followed by zero‑or‑more `subclass‑of`), through `SPARQLWrapper`, **with a small on‑disk cache** for reproducibility; or
offline via **YAGO 4.5** `rdf:type` over the Taxonomy Turtle file [15]. The tutorial confirms the path idiom verbatim:
`?work wdt:P31/wdt:P279* wd:Q838948` retrieves an item and all subclasses [17].

   *Worked example:* `"the District Court"` → Wikidata `Q…` → `wdt:P31/wdt:P279*` → `court (Q41487)` → coarse `ORG` /
   SUMO `&%Organization`.

This gives a reproducible, offline‑first stack (WordNet + SUMO required; Wikidata/YAGO as enrichers) that names a concrete
library and API at every step.

### B.4 Honest justification of the substitution (the reviewer‑critical paragraph)

**What is lost vs OpenCyc/Cyc.** Cyc supplies **microtheories** (contextualized assertion bundles), a vast hand‑curated
**commonsense assertion base**, rich **disjointness/cardinality/domain‑range axioms**, fine‑grained collections, and
higher‑order/contextual inference. WordNet+SUMO+Wikidata typing reproduces **none** of the assertional commonsense KB or
the contextual logic; it supplies the **taxonomic class hierarchy** only — which is precisely the *"taxonomic grounding"*
the goal names, but not Cyc's *"background structure"* in the full assertional sense.

**Why typing‑only usage suffices (the principled point).** In this method the ontology is used **only** to (i) constrain
**decoy generation** (type‑matched plausible counterfactuals) and (ii) support **entity linking**. It **never filters or
vetoes admissions**. The FDR gate's validity rests on the **decoy‑competition sign‑flip** (the empirically‑tested property,
Spec‑A Lemma‑1/D.4) and on **independent entrapment**, *not* on ontology completeness. Therefore a thin taxonomy **cannot
break the finite‑sample guarantee**; at worst it makes decoys slightly less type‑precise — a **bounded, measurable** effect
on decoy quality (Spec‑A's DeepCoy/DOE lens), not a correctness risk. This is the crucial contrast with
**ontology‑constraint filtering** (ODKE+/SHACL‑style), which *does* depend on rich trusted axioms and whose guarantee
degrades directly with ontology gaps.

**Descope vs defer.** **DESCOPE** Cyc's full microtheory/commonsense‑assertion reasoning — out of commodity‑reproducibility
scope, and not required, because the common‑sense gaps the goal cares about are handled by the **LLM probabilistic‑reasoning
step of PART C**, not by the ontology. **DEFER** richer SUMO/YAGO **axiom‑based consistency checks** (disjointness,
domain–range) as a *complementary* leftover‑budget upgrade that would sit **alongside** the decoy gate, never replace it.
Mapping back to the goal: the goal's **"taxonomic grounding"** requirement is **MET** by WordNet→SUMO(+Wikidata/YAGO); the
goal's **"OpenCyc background structure"** (the full assertional KB) is **descoped with stated rationale**.

---

## PART C — LLM‑as‑Probabilistic‑Reasoning‑Engine at Fuzzy Unifications (reviewer gap: *scope MAJOR*; goal hard requirement)

### C.1 Engine options and the pick

| Engine (source) | Role at the fuzzy/uncertain boundary | Weight semantics | Library / install | Recommendation |
|---|---|---|---|---|
| **ProbLog** [19,20] | LLM supplies **calibrated probabilities** for admitted facts/bridges; engine returns **marginal success probability** of each conclusion | Plain probabilities `p::atom.` (annotated disjunctions `Σpᵢ=1`) | `pip install problog` (Py 3.6+) | **PRIMARY** — cleanest certificate→weight map + marginal trace‑graphs |
| **DeepProbLog** [24] | The **methodological template**: a *neural predicate* whose probability comes from a network — here the network is **replaced by the LLM** as the probability source | Neural‑predicate probability | `deepproblog` | Cite as precedent; LLM‑as‑neural‑predicate |
| **aProbLog** (algebraic) [23] | Propagate **non‑probability weights** (e.g. the knockoff margin `W_i`, or an FDR‑derived value) via a chosen **commutative semiring**; supports gradient semiring | Any commutative semiring label on facts **and** negations | bundled with ProbLog | Use if weights are not plain probabilities |
| **Bousi~Prolog** [25,26] | **Fuzzy/proximity unification**: LLM supplies **proximity degrees** between predicates/constants where strict symbolic match fails | Weak unifier + **unification degree** ∈ [0,1], λ‑cut threshold | SWI‑Prolog build, v4.0 (Apr 2025) [25] | **Named alternative** — when semantics call for *similarity degrees* not probabilities |
| **FASILL** [27,28] | Similarity‑based weak unification with explicit **similarity equations** `f/n ~ g/n = r` and a complete lattice `L` | `<truth_degree, subst>`; `lambda_unification` λ‑cut | `jariazavalverde/fasill` | Alternative fuzzy engine; richer connectives |

**Recommendation:** **ProbLog as primary** (marginal‑probability trace‑graphs + the cleanest certificate→weight mapping),
with **Bousi~Prolog as the named fuzzy‑unification alternative** when the design needs *proximity degrees* rather than
probabilities. DeepProbLog is the precedent that legitimizes "an LLM supplies the probabilities into the logic program":
*"in a probabilistic logic, atomic expressions of the form q(t₁,…,tₙ) … have a probability p. Consequently, the output of
[a] neural network can [be that probability]"* — the **neural predicate** [24]; we substitute the LLM for the network.

**Verified ProbLog API surface** [19,20]:
```python
from problog.program import PrologString
from problog import get_evaluatable
model = """0.3::a.
query(a)."""
result = get_evaluatable().create_from(PrologString(model)).evaluate()   # -> dict {Term: probability}
```
Probabilistic facts `p::fact.`; annotated disjunctions `0.3::col(1,red); 0.7::col(1,blue).` (an AD
`p₁::h₁;…;pₙ::hₙ :- b₁,…,bₘ.` with `Σpᵢ=1`, per DeepProbLog [24]); probabilistic rules `win :- heads, col(_,red).`;
directives `query(...)` and `evidence(...)` [20]. Fact probabilities can be **fit from data** with **LFI** (Learning From
Interpretations, `problog.learning.lfi`, a soft‑EM that learns parameters from partial interpretations [22]) — relevant if
Phase‑0 wants to calibrate weights against a labeled slice.

### C.2 Certificate → probabilistic‑weight mapping (the core design contribution)

Each admitted fact/bridge becomes a **weighted ProbLog clause**. The binary admission decision (knockoff+) is **kept**; the
probability is layered **on top** of admission.

| Certificate field (Spec‑A) | Probabilistic role | Realization |
|---|---|---|
| Elicited score `Z_i` (DINCO/FactSelfCheck) | **Per‑fact probability** `p_i = calibrate(Z_i)` = `P(entailed)` via Platt/isotonic on a labeled slice | `p_i :: fact(rel,a,b).` (bridge → annotated/probabilistic **rule**) |
| Operative FDR `α̂` at cutoff `T` (knockoff+) | **Corpus‑level falsity prior** shared by all admissions | **(i) gate‑consistent shrinkage:** weight `= (1 − α̂)·p_i`, so the KB's expected truth mass matches the FDR certificate |
| Knockoff margin `W_i` (or rank‑normalized `Z_i − Z̃_i`) | **Per‑pair confidence** (bigger real‑vs‑decoy win ⇒ higher weight) | **(ii) per‑pair margin weight:** monotone calibrated link `g(W_i) → P(true)`; optionally carried as an **aProbLog** [23] semiring label |
| Entrapment bound `FDP̂(r)` | **Independent prior / consistency check** on the aggregate admitted‑false mass | Require `E[admitted‑false fraction] ≈ FDP̂(r)` — a **sanity bound**, not a second weighting |
| `cert(W_i,T,α,FDP̂,r)` (full) | **Audit payload** retained at each leaf | Attached unchanged to the trace‑graph leaf (C.3) |

**Recommended default:** option **(i) gate‑consistent shrinkage** `weight = (1 − α̂)·p_i` for the headline (it ties the
probabilistic KB directly to the FDR certificate and is monotone by construction), with option **(ii) margin weight** as
the comparison arm the method‑executor evaluates. Keep `W_i / T / α` in the leaf certificate either way — **do not discard
the gate's binary admission**; the probability augments it.

### C.3 Probabilistic inference + the auditable trace‑graph (C4)

- **Marginals.** ProbLog computes, for each multi‑hop derived conclusion, `query(conclusion) → marginal success probability`
  via weighted model counting over a compiled circuit (SDD/d‑DNNF) [19,20].
- **Proof structure → probabilistic trace‑graph.** ProbLog's **explain mode** emits, *"for each query a list of mutually
  exclusive proofs with their probability, and … the success probability [as] the sum of the probabilities of the individual
  proofs"* [21]; **MPE mode** returns the most probable world, and the **most‑probable‑proof (Viterbi)** task returns the
  single best explanation [21]. Use these to build the **same node/edge shape as Spec‑B's deterministic Graphviz trace**,
  but now **every derived node carries its marginal probability** and **every leaf carries** provenance +
  `decoy_certificate(W_i,T,α)` + `entrapment_certificate(FDP̂,r)` + the calibrated weight `p_i`.
- **Export.** Reuse Spec‑B's JSON + Graphviz‑DOT format, adding a `prob` attribute per node and per edge.
- **Fallback (state explicitly).** If ProbLog's native explanation is too thin for the audit, **run ProbLog for the marginal
  and reuse the janus‑swi `solve/2` meta‑interpreter (Spec‑B) for the proof DAG**, annotating each node with the ProbLog
  marginal. This keeps the human‑auditable DAG while gaining probabilities.

### C.4 Why iteration‑1 was deterministic, and the minimal upgrade path (C5)

**Why deterministic janus‑swi backward‑chaining in iter‑1 was the right first step.** (i) The FDR gate already emits a
**binary** admission decision, so binary proof trees suffice for the crisp‑gold CLUTRR diagonal and the Re‑DocRED wedge;
(ii) determinism **maximizes reproducibility** on commodity CPU and avoids extra inference cost/budget; (iii) it **isolates
the FDR contribution** from probabilistic‑inference confounds. Probabilistic reasoning is exactly what the **goal‑faithful
professional‑doc slice** (where fuzzy unifications dominate) needs — hence the upgrade.

**The minimal, implementable upgrade (the exact swap).**
1. From the admitted clauses, generate a ProbLog program: one `p_i :: fact(...).` (or weighted rule) per admission, with
   `p_i` from C.2.
2. Replace the janus‑swi call:
   ```python
   # iter-1 (deterministic):  janus.query_once("solve(Goal, Proof)", {"Goal": goal})
   # iter-2 (probabilistic):
   from problog.program import PrologString
   from problog import get_evaluatable
   marginals = get_evaluatable().create_from(PrologString(prog)).evaluate()   # {conclusion: P}
   ```
3. Emit the probabilistic trace‑graph of C.3 (add `prob` to nodes/edges; keep the certificate leaves).

CPU‑only feasibility is good: ProbLog grounding is light for short documents / few‑hop proofs (the
~3000‑character, few‑hop regime of the goal). **Fuzzy‑unification alternative (one‑liner):** if the semantics call for
*proximity degrees* rather than probabilities, swap ProbLog for **Bousi~Prolog** [25] — the LLM supplies proximity
relations `a ~ b = r` (reflexive, symmetric, not necessarily transitive [25]) and weak unification returns a **unification
degree** with a **λ‑cut**, or **FASILL** [27,28] with explicit similarity equations `f/n ~ g/n = r` and a λ‑cut flag.

---

## Positioning note — how the three parts close the named reviewer gaps

- **Novelty MINOR → closed (PART A).** The five‑dimension table pins six labeled/output‑certifying neighbors [1–7] and
  isolates the exact delta — *label‑free + decoy‑competition + intermediate text→logic admission boundary* — with a
  paste‑ready one‑sentence delta (A.3) and a targeted rebuttal (A.4). Adversarial search found no pre‑emption (A.5).
- **Scope MAJOR (ontology) → closed (PART B).** OpenCyc is honestly reported as discontinued (March 2017 [8,9]) and
  ResearchCyc as license‑gated [8]; the goal's literal **"taxonomic grounding"** is met by a concrete, offline‑first
  **WordNet→SUMO(+Wikidata/YAGO)** recipe with exact APIs (B.3), and the substitution is argued via loss / sufficiency /
  descope‑vs‑defer (B.4) — including the principled reason typing‑only cannot break the FDR guarantee.
- **Scope MAJOR (probabilistic reasoning) → closed (PART C).** A concrete **ProbLog** design (with **Bousi~Prolog/FASILL**
  as the named fuzzy‑unification alternative) turns the goal's **"LLM as a probabilistic reasoning engine … fuzzy
  unifications"** into code: the LLM supplies calibrated unification probabilities, the decoy/entrapment certificates map
  onto weights (C.2), marginals are computed, and an auditable **probabilistic trace‑graph** is exported (C.3), with the
  exact deterministic→probabilistic swap and the DeepProbLog precedent (C.4).
- **Drop‑in continuity.** Every new piece reuses Spec‑A's certificate schema and Spec‑B's typing vocabulary and trace‑graph
  format, so the method‑executor inherits, rather than re‑derives, the settled machinery.

## Confidence

- **High:** the ProbLog Python API and explain/MPE modes [19,20,21]; OpenCyc discontinuation status [8,9]; the SUMO upper
  ontology + WordNet mapping format with a verified real mapping line [12,13,14]; the Wikidata `P31/P279*` path [17]; the
  novelty rows verified by fetch_grep [1,2,3,4,5,6]; DeepProbLog neural‑predicate semantics [24]; Bousi~Prolog/FASILL weak
  unification [25,27,28].
- **Medium:** that no unindexed 2025–2026 preprint pre‑empts the exact construction (A.5); the precise CPU cost of ProbLog
  grounding on the longest professional document (runtime‑only); whether the WordNet→SUMO mapping has adequate coverage for
  legal/regulatory nouns (runtime‑only); Wikidata SPARQL latency vs. an offline pre‑cache (runtime‑only).


## Sources

[1] [Jin & Candes 2023 - Selection by Prediction with Conformal p-values (Conformal Selection)](https://arxiv.org/pdf/2210.01408) — PART A row 1. Labeled training/calibration/test split; conformal p-values + Benjamini-Hochberg control FDR; certifies a selected shortlist (output) under exchangeability. Verified verbatim: 'guarantee holds under mild exchangeability conditions'; cfBH turns any predictor into a screening mechanism using a labeled calibration set. NOT decoy.

[2] [Li, Magesh & Veeravalli 2025 - Principled Detection of Hallucinations in LLMs via Multiple Testing](https://arxiv.org/abs/2508.18473) — PART A row 2. Uses a 'small calibration set of non-hallucinated prompts' (labeled, ROUGE-L) to control the false-alarm rate; conformal p-values q^j=(1+#{i:s_i>=t})/(1+|C|); flags a hallucinated generation (output) at the prompt level. NOT decoy.

[3] [COCOCO 2026 - Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models](https://arxiv.org/abs/2605.18202) — PART A row 3 (closest neuro-symbolic+conformal neighbor). Distribution-free COVERAGE (not FDR) via conformal prediction + e-values; labeled calibration; deduction-abduction revision; certifies concept+label prediction SETS (the NeSy-CBM output) under fixed logical constraints. NOT decoy.

[4] [Bashari, Epstein, Romano & Sesia 2023 - Derandomized Novelty Detection with FDR Control via Conformal E-values](https://arxiv.org/abs/2302.07294) — PART A row 4. Conformal e-values + (derandomized) e-BH control FDR; needs an inlier/reference calibration set; certifies which test points are novel/outliers (output) under exchangeability. NOT decoy.

[5] [Marandon 2023 - Conformal link prediction for false discovery rate control](https://arxiv.org/abs/2306.14693) — PART A row 5. Identifies true edges with FDR control; explicitly notes graph dependence makes the setup 'different from the usual setup in conformal inference, where data exchangeability is assumed'; certifies predicted KG links (output); calibrated on observed edges. NOT decoy.

[6] [Blanchard, Durand, Marandon & Perier 2024 - FDR control and FDP bounds for conformal link prediction](https://arxiv.org/abs/2404.02542) — PART A row 5 follow-on. Proves the conformal link-prediction procedure controls FDR and derives uniform FDP bounds; still labeled/observed-graph and output-certifying. NOT decoy.

[7] [Mohri & Hashimoto 2024 (ICML) - Language Models with Conformal Factuality Guarantees](https://arxiv.org/abs/2402.10978) — PART A row 6 (reused from Spec A). Labeled calibration set; sub-claim back-off filter; certifies the emitted answer (output); factuality/coverage-type guarantee. NOT decoy and not a label-free admission-boundary knob.

[8] [Bergman - Fare Thee Well, OpenCyc](https://www.mkbergman.com/2034/fare-thee-well-opencyc/) — PART B. Corroborates OpenCyc discontinuation: 'Cycorp has pulled OpenCyc from the marketplace' (March 2017); legacy v4.0 dumps survive only via third parties/forks; standing route is to 'contact info@cyc.com to obtain a research license' for Cyc.

[9] [KBpedia - OpenCyc Not Online](https://kbpedia.org/resources/opencyc/) — PART B. Verbatim: 'As of March 2017, Cycorp, the developer of OpenCyc, ceased online support for its knowledge base.' Latest OpenCyc only obtainable (unsupported) for local use; a cloud option is unspecified.

[10] [asanchez75/opencyc - third-party OpenCyc 4.0 OWL mirror](https://github.com/asanchez75/opencyc) — PART B. Evidence that legacy OpenCyc 4.0 survives only as unmaintained third-party mirrors/forks (not a reproducible, supported commodity dependency).

[11] [NLTK WordNet HOWTO](https://www.nltk.org/howto/wordnet.html) — PART B Layer 1. Offline WordNet via NLTK: wn.synsets(word,pos=NOUN), synset.hypernym_paths(); anchor synsets (person.n.01, location.n.01/region.n.03, organization.n.01/social_group.n.01, time_period.n.01, number.n.02/measure.n.02) for coarse typing. Reused from Spec B.

[12] [ontologyportal/sumo - Suggested Upper Merged Ontology (SUMO)](https://github.com/ontologyportal/sumo) — PART B. SUMO is a formal upper ontology in SUO-KIF, IEEE-owned with GNU GPL code, mapped to all of WordNet via WordNetMappings30-{noun,verb,adj,adv}.txt; Sigma is the inference/dev environment. The genuine open OpenCyc analogue for upper-ontology grounding.

[13] [SUMO WordNetMappings30-noun.txt (raw mapping file)](https://raw.githubusercontent.com/ontologyportal/sumo/master/WordNetMappings/WordNetMappings30-noun.txt) — PART B Layer 1 (verified real mapping line). Each WordNet synset maps to a SUMO term with a suffix (=, +, @). Verified: the 'person' synset (00015388) maps as '... a human being ... &%Human='; also &%Organization@ and &%Organism+ appear. Suffix legend: = equivalence, + subsumption, @ instance.

[14] [The Ontology Portal - SUMO](https://www.ontologyportal.org/) — PART B. Confirms SUMO is 'the only formal ontology that has been mapped to all of the WordNet lexicon', written in SUO-KIF, free and owned by the IEEE; main site for SUMO/MILO/domain ontologies.

[15] [YAGO 4.5 downloads](https://yago-knowledge.org/downloads/yago-4-5) — PART B Layer 2 (offline option). YAGO 4.5 = schema.org upper taxonomy + cleaned Wikidata lower taxonomy, shipped as Turtle files (Schema, Taxonomy, Facts); loadable into any triple store (Jena, GraphDB, QLever). Good for offline named-entity instance typing on professional docs.

[16] [Suchanek et al. 2023 - Integrating the Wikidata Taxonomy into YAGO (YAGO 4.5)](https://arxiv.org/abs/2308.11884) — PART B. Primary paper for YAGO 4.5's rich, clean taxonomy combining schema.org top classes with a careful selection of the Wikidata taxonomy.

[17] [Wikidata SPARQL tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) — PART B Layer 2. instance-of (P31) vs subclass-of (P279); the class-hierarchy property path 'wdt:P31/wdt:P279*' ('one instance-of then zero-or-more subclass-of'). Verified example: '?work wdt:P31/wdt:P279* wd:Q838948'. Use via SPARQLWrapper with an on-disk cache.

[18] [Owlready2 - Managing ontologies](https://owlready2.readthedocs.io/en/latest/onto.html) — PART B. Offline OWL/RDF loading in Python: get_ontology('file://...').load(); access classes via onto.Cls / onto['Cls']; onto.search(subclass_of=onto.Cls). Concrete loader for a local SUMO.owl / ontology file.

[19] [Using ProbLog from Python (ProbLog 2.2 docs)](https://problog.readthedocs.io/en/latest/python.html) — PART C primary API. from problog.program import PrologString; from problog import get_evaluatable; get_evaluatable().create_from(PrologString(model)).evaluate() returns a dict {Term: probability}. Probabilistic facts 'p::fact.', query(...).

[20] [ProbLog inference tutorial (advanced)](https://dtai.cs.kuleuven.be/problog/tutorial/advanced/00_inference.html) — PART C. Verbatim syntax: probabilistic facts '0.4::heads.'; annotated disjunctions '0.3::col(1,red); 0.7::col(1,blue).'; probabilistic rules 'win :- heads, col(_,red).'; query(...) and evidence(...); marginals via weighted model counting (OBDD/SDD).

[21] [ProbLog standalone tool - explain & MPE modes](https://problog.readthedocs.io/en/latest/cli.html) — PART C trace-graph. Explain mode outputs 'for each query a list of mutually exclusive proofs with their probability, and ... the success probability [as] the sum of the probabilities of the individual proofs'. MPE mode = most probable world; most-probable-proof (Viterbi) = single best explanation. Basis for the probabilistic trace-graph.

[22] [ProbLog parameter learning - Learning From Interpretations (LFI)](https://dtai.cs.kuleuven.be/problog/tutorial/learning/01_bayes.html) — PART C (optional weight calibration). LFI (problog.learning.lfi) is a soft-EM that learns ProbLog fact probabilities from partial interpretations: 'problog lfi <model> <evidence>'. Lets Phase-0 calibrate clause weights from a labeled slice.

[23] [Algebraic ProbLog (aProbLog) - semirings](https://dtai.cs.kuleuven.be/problog/tutorial/advanced/03_aproblog.html) — PART C. aProbLog generalizes ProbLog to arbitrary commutative semirings via a labeling function on facts and their negations; supports the gradient semiring. Use to propagate non-probability weights such as the knockoff margin W_i or an FDR-derived value.

[24] [Manhaeve et al. 2018 - DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — PART C precedent. Defines the neural predicate: atoms q(t1..tn) have a probability p, and 'the output of [a] neural network can [be that probability]'; annotated disjunction p1::h1;...;pn::hn:-body with sum(pi)=1; algebraic/gradient-semiring inference. Template for 'LLM supplies the probabilities into the logic program'.

[25] [Bousi~Prolog - A Proximity-Based Fuzzy Prolog System](https://dectau.uclm.es/bousi-prolog/) — PART C fuzzy-unification alternative. Replaces syntactic unification with weak unification over proximity relations (reflexive, symmetric, not necessarily transitive); yields a weak m.g.u. plus a numerical unification/approximation degree with a lambda-cut; built on SWI-Prolog, open-source, v4.0 (Apr 2025). LLM supplies proximity degrees a~b=r.

[26] [Julian-Iranzo & Rubio-Manzano - Bousi~Prolog: design & implementation of a proximity-based fuzzy logic programming language](https://www.researchgate.net/publication/364128161) — PART C. Founding paper for Bousi~Prolog's weak-unification semantics and proximity relations (the formal basis for unification degrees and the lambda-cut).

[27] [FASILL - Fuzzy Aggregators and Similarity Into a Logic Language](https://dectau.uclm.es/fasill/) — PART C fuzzy alternative. A FASILL program is a tuple <Pi, R, L> (rules, similarity relation, complete lattice); similarity equations 'f/n ~ g/n = r', '~tnorm = godel'; a query returns <truth_degree, subst> (e.g. <0.38,{X/hydropolis}>); weak unification with a lambda_unification lambda-cut.

[28] [Julian-Iranzo, Moreno, Penabad & Vazquez 2015 - A Fuzzy Logic Programming Environment for Managing Similarity and Truth Degrees (FASILL)](https://arxiv.org/abs/1501.02034) — PART C. Primary paper for FASILL: weak most general unifier, the lambda-cut unification threshold, similarity relations, and the lattice of truth degrees with connectives.

[29] [Conformal Link Prediction with FDR Control via e-value aggregation under dependence (2025)](https://arxiv.org/abs/2507.07025) — PART A frontier note. Recent conformal link-prediction work aggregating e-values under graph dependence; still labeled/observed-graph and output-certifying - reinforces that the link-prediction family is conformal, not decoy-competition.

[30] [Conformal novelty detection with false discovery rate control at the boundary (2026)](https://arxiv.org/abs/2601.02610) — PART A frontier note. Active conformal-novelty frontier (boundary/bFDR variants); labeled/reference-set conformal, not a label-free decoy gate - shows the neighbor family is still moving but remains conformal.

## Follow-up Questions

- Runtime: does ProbLog grounding + weighted model counting stay cheap (CPU-only, sub-second) on the longest ~3000-character professional document with its few-hop proof DAG, or must the janus-swi solve/2 proof-DAG fallback (marginal-from-ProbLog, DAG-from-meta-interpreter) be the default for the trace-graph?
- Calibration: does the chosen Z_i->P(entailed) link (Platt/isotonic, or LFI-fit) keep clause weights monotone in the elicited score AND consistent with the operative FDR alpha-hat under the gate-consistent shrinkage weight (1-alpha_hat)*p_i, and how sensitive are multi-hop marginals to gate-consistent-shrinkage vs per-pair-margin weighting?
- Coverage & latency: is the WordNet->SUMO WordNetMappings30 anchor coverage adequate for legal/regulatory/news head nouns (or do many map only to MISC/&%Entity), and is live Wikidata SPARQL P31/P279* latency acceptable for the professional-doc slice or must instance types be pre-cached offline (YAGO 4.5 rdf:type)?

---
*Generated by AI Inventor Pipeline*
