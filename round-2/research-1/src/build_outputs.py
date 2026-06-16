#!/usr/bin/env python3
"""Build research_out.json and the struct-out JSON from research_report.md."""
import json
from pathlib import Path

WS = Path("/ai-inventor/aii_data/runs/run_MQN7mBg4AhvH/3_invention_loop/iter_2/gen_art/gen_art_research_1")
answer = (WS / "research_report.md").read_text(encoding="utf-8")

sources = [
    {"index": 1, "url": "https://arxiv.org/pdf/2210.01408",
     "title": "Jin & Candes 2023 - Selection by Prediction with Conformal p-values (Conformal Selection)",
     "summary": "PART A row 1. Labeled training/calibration/test split; conformal p-values + Benjamini-Hochberg control FDR; certifies a selected shortlist (output) under exchangeability. Verified verbatim: 'guarantee holds under mild exchangeability conditions'; cfBH turns any predictor into a screening mechanism using a labeled calibration set. NOT decoy."},
    {"index": 2, "url": "https://arxiv.org/abs/2508.18473",
     "title": "Li, Magesh & Veeravalli 2025 - Principled Detection of Hallucinations in LLMs via Multiple Testing",
     "summary": "PART A row 2. Uses a 'small calibration set of non-hallucinated prompts' (labeled, ROUGE-L) to control the false-alarm rate; conformal p-values q^j=(1+#{i:s_i>=t})/(1+|C|); flags a hallucinated generation (output) at the prompt level. NOT decoy."},
    {"index": 3, "url": "https://arxiv.org/abs/2605.18202",
     "title": "COCOCO 2026 - Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models",
     "summary": "PART A row 3 (closest neuro-symbolic+conformal neighbor). Distribution-free COVERAGE (not FDR) via conformal prediction + e-values; labeled calibration; deduction-abduction revision; certifies concept+label prediction SETS (the NeSy-CBM output) under fixed logical constraints. NOT decoy."},
    {"index": 4, "url": "https://arxiv.org/abs/2302.07294",
     "title": "Bashari, Epstein, Romano & Sesia 2023 - Derandomized Novelty Detection with FDR Control via Conformal E-values",
     "summary": "PART A row 4. Conformal e-values + (derandomized) e-BH control FDR; needs an inlier/reference calibration set; certifies which test points are novel/outliers (output) under exchangeability. NOT decoy."},
    {"index": 5, "url": "https://arxiv.org/abs/2306.14693",
     "title": "Marandon 2023 - Conformal link prediction for false discovery rate control",
     "summary": "PART A row 5. Identifies true edges with FDR control; explicitly notes graph dependence makes the setup 'different from the usual setup in conformal inference, where data exchangeability is assumed'; certifies predicted KG links (output); calibrated on observed edges. NOT decoy."},
    {"index": 6, "url": "https://arxiv.org/abs/2404.02542",
     "title": "Blanchard, Durand, Marandon & Perier 2024 - FDR control and FDP bounds for conformal link prediction",
     "summary": "PART A row 5 follow-on. Proves the conformal link-prediction procedure controls FDR and derives uniform FDP bounds; still labeled/observed-graph and output-certifying. NOT decoy."},
    {"index": 7, "url": "https://arxiv.org/abs/2402.10978",
     "title": "Mohri & Hashimoto 2024 (ICML) - Language Models with Conformal Factuality Guarantees",
     "summary": "PART A row 6 (reused from Spec A). Labeled calibration set; sub-claim back-off filter; certifies the emitted answer (output); factuality/coverage-type guarantee. NOT decoy and not a label-free admission-boundary knob."},
    {"index": 8, "url": "https://www.mkbergman.com/2034/fare-thee-well-opencyc/",
     "title": "Bergman - Fare Thee Well, OpenCyc",
     "summary": "PART B. Corroborates OpenCyc discontinuation: 'Cycorp has pulled OpenCyc from the marketplace' (March 2017); legacy v4.0 dumps survive only via third parties/forks; standing route is to 'contact info@cyc.com to obtain a research license' for Cyc."},
    {"index": 9, "url": "https://kbpedia.org/resources/opencyc/",
     "title": "KBpedia - OpenCyc Not Online",
     "summary": "PART B. Verbatim: 'As of March 2017, Cycorp, the developer of OpenCyc, ceased online support for its knowledge base.' Latest OpenCyc only obtainable (unsupported) for local use; a cloud option is unspecified."},
    {"index": 10, "url": "https://github.com/asanchez75/opencyc",
     "title": "asanchez75/opencyc - third-party OpenCyc 4.0 OWL mirror",
     "summary": "PART B. Evidence that legacy OpenCyc 4.0 survives only as unmaintained third-party mirrors/forks (not a reproducible, supported commodity dependency)."},
    {"index": 11, "url": "https://www.nltk.org/howto/wordnet.html",
     "title": "NLTK WordNet HOWTO",
     "summary": "PART B Layer 1. Offline WordNet via NLTK: wn.synsets(word,pos=NOUN), synset.hypernym_paths(); anchor synsets (person.n.01, location.n.01/region.n.03, organization.n.01/social_group.n.01, time_period.n.01, number.n.02/measure.n.02) for coarse typing. Reused from Spec B."},
    {"index": 12, "url": "https://github.com/ontologyportal/sumo",
     "title": "ontologyportal/sumo - Suggested Upper Merged Ontology (SUMO)",
     "summary": "PART B. SUMO is a formal upper ontology in SUO-KIF, IEEE-owned with GNU GPL code, mapped to all of WordNet via WordNetMappings30-{noun,verb,adj,adv}.txt; Sigma is the inference/dev environment. The genuine open OpenCyc analogue for upper-ontology grounding."},
    {"index": 13, "url": "https://raw.githubusercontent.com/ontologyportal/sumo/master/WordNetMappings/WordNetMappings30-noun.txt",
     "title": "SUMO WordNetMappings30-noun.txt (raw mapping file)",
     "summary": "PART B Layer 1 (verified real mapping line). Each WordNet synset maps to a SUMO term with a suffix (=, +, @). Verified: the 'person' synset (00015388) maps as '... a human being ... &%Human='; also &%Organization@ and &%Organism+ appear. Suffix legend: = equivalence, + subsumption, @ instance."},
    {"index": 14, "url": "https://www.ontologyportal.org/",
     "title": "The Ontology Portal - SUMO",
     "summary": "PART B. Confirms SUMO is 'the only formal ontology that has been mapped to all of the WordNet lexicon', written in SUO-KIF, free and owned by the IEEE; main site for SUMO/MILO/domain ontologies."},
    {"index": 15, "url": "https://yago-knowledge.org/downloads/yago-4-5",
     "title": "YAGO 4.5 downloads",
     "summary": "PART B Layer 2 (offline option). YAGO 4.5 = schema.org upper taxonomy + cleaned Wikidata lower taxonomy, shipped as Turtle files (Schema, Taxonomy, Facts); loadable into any triple store (Jena, GraphDB, QLever). Good for offline named-entity instance typing on professional docs."},
    {"index": 16, "url": "https://arxiv.org/abs/2308.11884",
     "title": "Suchanek et al. 2023 - Integrating the Wikidata Taxonomy into YAGO (YAGO 4.5)",
     "summary": "PART B. Primary paper for YAGO 4.5's rich, clean taxonomy combining schema.org top classes with a careful selection of the Wikidata taxonomy."},
    {"index": 17, "url": "https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial",
     "title": "Wikidata SPARQL tutorial",
     "summary": "PART B Layer 2. instance-of (P31) vs subclass-of (P279); the class-hierarchy property path 'wdt:P31/wdt:P279*' ('one instance-of then zero-or-more subclass-of'). Verified example: '?work wdt:P31/wdt:P279* wd:Q838948'. Use via SPARQLWrapper with an on-disk cache."},
    {"index": 18, "url": "https://owlready2.readthedocs.io/en/latest/onto.html",
     "title": "Owlready2 - Managing ontologies",
     "summary": "PART B. Offline OWL/RDF loading in Python: get_ontology('file://...').load(); access classes via onto.Cls / onto['Cls']; onto.search(subclass_of=onto.Cls). Concrete loader for a local SUMO.owl / ontology file."},
    {"index": 19, "url": "https://problog.readthedocs.io/en/latest/python.html",
     "title": "Using ProbLog from Python (ProbLog 2.2 docs)",
     "summary": "PART C primary API. from problog.program import PrologString; from problog import get_evaluatable; get_evaluatable().create_from(PrologString(model)).evaluate() returns a dict {Term: probability}. Probabilistic facts 'p::fact.', query(...)."},
    {"index": 20, "url": "https://dtai.cs.kuleuven.be/problog/tutorial/advanced/00_inference.html",
     "title": "ProbLog inference tutorial (advanced)",
     "summary": "PART C. Verbatim syntax: probabilistic facts '0.4::heads.'; annotated disjunctions '0.3::col(1,red); 0.7::col(1,blue).'; probabilistic rules 'win :- heads, col(_,red).'; query(...) and evidence(...); marginals via weighted model counting (OBDD/SDD)."},
    {"index": 21, "url": "https://problog.readthedocs.io/en/latest/cli.html",
     "title": "ProbLog standalone tool - explain & MPE modes",
     "summary": "PART C trace-graph. Explain mode outputs 'for each query a list of mutually exclusive proofs with their probability, and ... the success probability [as] the sum of the probabilities of the individual proofs'. MPE mode = most probable world; most-probable-proof (Viterbi) = single best explanation. Basis for the probabilistic trace-graph."},
    {"index": 22, "url": "https://dtai.cs.kuleuven.be/problog/tutorial/learning/01_bayes.html",
     "title": "ProbLog parameter learning - Learning From Interpretations (LFI)",
     "summary": "PART C (optional weight calibration). LFI (problog.learning.lfi) is a soft-EM that learns ProbLog fact probabilities from partial interpretations: 'problog lfi <model> <evidence>'. Lets Phase-0 calibrate clause weights from a labeled slice."},
    {"index": 23, "url": "https://dtai.cs.kuleuven.be/problog/tutorial/advanced/03_aproblog.html",
     "title": "Algebraic ProbLog (aProbLog) - semirings",
     "summary": "PART C. aProbLog generalizes ProbLog to arbitrary commutative semirings via a labeling function on facts and their negations; supports the gradient semiring. Use to propagate non-probability weights such as the knockoff margin W_i or an FDR-derived value."},
    {"index": 24, "url": "https://arxiv.org/abs/1805.10872",
     "title": "Manhaeve et al. 2018 - DeepProbLog: Neural Probabilistic Logic Programming",
     "summary": "PART C precedent. Defines the neural predicate: atoms q(t1..tn) have a probability p, and 'the output of [a] neural network can [be that probability]'; annotated disjunction p1::h1;...;pn::hn:-body with sum(pi)=1; algebraic/gradient-semiring inference. Template for 'LLM supplies the probabilities into the logic program'."},
    {"index": 25, "url": "https://dectau.uclm.es/bousi-prolog/",
     "title": "Bousi~Prolog - A Proximity-Based Fuzzy Prolog System",
     "summary": "PART C fuzzy-unification alternative. Replaces syntactic unification with weak unification over proximity relations (reflexive, symmetric, not necessarily transitive); yields a weak m.g.u. plus a numerical unification/approximation degree with a lambda-cut; built on SWI-Prolog, open-source, v4.0 (Apr 2025). LLM supplies proximity degrees a~b=r."},
    {"index": 26, "url": "https://www.researchgate.net/publication/364128161",
     "title": "Julian-Iranzo & Rubio-Manzano - Bousi~Prolog: design & implementation of a proximity-based fuzzy logic programming language",
     "summary": "PART C. Founding paper for Bousi~Prolog's weak-unification semantics and proximity relations (the formal basis for unification degrees and the lambda-cut)."},
    {"index": 27, "url": "https://dectau.uclm.es/fasill/",
     "title": "FASILL - Fuzzy Aggregators and Similarity Into a Logic Language",
     "summary": "PART C fuzzy alternative. A FASILL program is a tuple <Pi, R, L> (rules, similarity relation, complete lattice); similarity equations 'f/n ~ g/n = r', '~tnorm = godel'; a query returns <truth_degree, subst> (e.g. <0.38,{X/hydropolis}>); weak unification with a lambda_unification lambda-cut."},
    {"index": 28, "url": "https://arxiv.org/abs/1501.02034",
     "title": "Julian-Iranzo, Moreno, Penabad & Vazquez 2015 - A Fuzzy Logic Programming Environment for Managing Similarity and Truth Degrees (FASILL)",
     "summary": "PART C. Primary paper for FASILL: weak most general unifier, the lambda-cut unification threshold, similarity relations, and the lattice of truth degrees with connectives."},
    {"index": 29, "url": "https://arxiv.org/abs/2507.07025",
     "title": "Conformal Link Prediction with FDR Control via e-value aggregation under dependence (2025)",
     "summary": "PART A frontier note. Recent conformal link-prediction work aggregating e-values under graph dependence; still labeled/observed-graph and output-certifying - reinforces that the link-prediction family is conformal, not decoy-competition."},
    {"index": 30, "url": "https://arxiv.org/abs/2601.02610",
     "title": "Conformal novelty detection with false discovery rate control at the boundary (2026)",
     "summary": "PART A frontier note. Active conformal-novelty frontier (boundary/bFDR variants); labeled/reference-set conformal, not a label-free decoy gate - shows the neighbor family is still moving but remains conformal."},
]

follow_up_questions = [
    "Runtime: does ProbLog grounding + weighted model counting stay cheap (CPU-only, sub-second) on the longest ~3000-character professional document with its few-hop proof DAG, or must the janus-swi solve/2 proof-DAG fallback (marginal-from-ProbLog, DAG-from-meta-interpreter) be the default for the trace-graph?",
    "Calibration: does the chosen Z_i->P(entailed) link (Platt/isotonic, or LFI-fit) keep clause weights monotone in the elicited score AND consistent with the operative FDR alpha-hat under the gate-consistent shrinkage weight (1-alpha_hat)*p_i, and how sensitive are multi-hop marginals to gate-consistent-shrinkage vs per-pair-margin weighting?",
    "Coverage & latency: is the WordNet->SUMO WordNetMappings30 anchor coverage adequate for legal/regulatory/news head nouns (or do many map only to MISC/&%Entity), and is live Wikidata SPARQL P31/P279* latency acceptable for the professional-doc slice or must instance types be pre-cached offline (YAGO 4.5 rdf:type)?",
]

research_out = {
    "title": "Novelty-Delta Table, Real Upper-Ontology Grounding Recipe, and the LLM-as-Probabilistic-Reasoner Design at Fuzzy Unifications",
    "summary": (
        "Source-traceable research closing three iteration-1 reviewer gaps for the decoy-gated neuro-symbolic "
        "text-to-logic pipeline, extending (not contradicting) Spec A (FDR gate) and Spec B (pipeline/typing/trace-graph). "
        "PART A: a five-dimension NOVELTY-DELTA table pinning six nearest conformal/FDR neighbors - Jin-Candes conformal "
        "selection [1], Li-Magesh-Veeravalli multiple-testing hallucination detection [2], COCOCO neuro-symbolic conformal "
        "sets [3], Bashari conformal-e-value novelty detection [4], Marandon/Blanchard conformal link-prediction FDR [5,6], "
        "Mohri-Hashimoto conformal factuality [7] - on {label requirement, unit certified, exchangeability mechanism, "
        "decoy?, FDR-vs-coverage}; all are LABELED and certify a model OUTPUT under assumed exchangeability, whereas OURS is "
        "label-free, certifies the INTERMEDIATE text->logic admission, uses engineered+tested decoy sign-flip, and controls "
        "FDR. Includes a paste-ready one-sentence delta, a 'not just conformal selection' rebuttal, and an honest adversarial "
        "result (no 2025-2026 preprint pre-empts the construction). PART B: OpenCyc honestly reported as discontinued (March "
        "2017 [8,9], third-party-mirror-only [10]) and ResearchCyc as license-gated [8]; a concrete offline-first two-layer "
        "argument-typing recipe - WordNet hypernyms [11] anchored to SUMO upper-ontology classes via WordNetMappings30 "
        "(verified line: person -> &%Human=) [12,13,14], plus Wikidata P31/P279* [17] or offline YAGO 4.5 [15,16] instance "
        "typing, loadable with owlready2/SPARQLWrapper [18] - and a loss/sufficiency/descope-vs-defer justification arguing "
        "why typing-only usage cannot break the FDR guarantee (unlike ontology-constraint filtering). PART C: a concrete "
        "LLM-as-probabilistic-reasoner design - ProbLog primary (verified API: get_evaluatable().create_from(PrologString)."
        "evaluate() -> {Term:prob}; p::fact.; annotated disjunctions; query/evidence; explain/MPE proofs [19,20,21]; LFI "
        "weight learning [22]; aProbLog semirings [23]; DeepProbLog neural-predicate precedent [24]) with Bousi~Prolog/FASILL "
        "as the fuzzy-unification alternative [25,26,27,28]; a certificate->probabilistic-weight mapping table (p_i=calibrate"
        "(Z_i); gate-consistent shrinkage (1-alpha_hat)*p_i [default] or per-pair W_i margin weight; entrapment FDP-hat as "
        "consistency prior; full cert kept at the leaf); a probabilistic trace-graph export (reuse Spec-B JSON/Graphviz-DOT, "
        "add a 'prob' attribute per node/edge, marginal per derived node, certificate per leaf; janus-swi solve/2 fallback "
        "for the proof DAG); and the exact deterministic->probabilistic upgrade swap (janus query_once -> problog "
        "get_evaluatable/evaluate). Deliverables: research_out.json + research_report.md with 30 primary sources, tables, "
        "recipes, exact APIs, and a positioning note mapping each part to the named reviewer gaps."
    ),
    "answer": answer,
    "sources": sources,
    "follow_up_questions": follow_up_questions,
}

struct_out = {
    "title": "Novelty-Delta, Upper-Ontology Grounding Recipe, and LLM-as-Probabilistic-Reasoner Design",
    "layman_summary": (
        "Answers three reviewer concerns: how this hallucination-control method differs from prior work, how to replace the "
        "discontinued OpenCyc ontology with free tools, and how to let an LLM do probabilistic logic reasoning."
    ),
    "summary": research_out["summary"],
    "out_expected_files": {"output": "research_out.json"},
    "answer": answer,
    "sources": sources,
    "follow_up_questions": follow_up_questions,
}

(WS / "research_out.json").write_text(json.dumps(research_out, indent=2, ensure_ascii=False), encoding="utf-8")
(WS / ".terminal_claude_agent_struct_out.json").write_text(json.dumps(struct_out, indent=2, ensure_ascii=False), encoding="utf-8")

# sanity report
print("research_out.json bytes:", (WS / "research_out.json").stat().st_size)
print("struct_out bytes:", (WS / ".terminal_claude_agent_struct_out.json").stat().st_size)
print("answer chars:", len(answer))
print("num sources:", len(sources))
print("title len:", len(struct_out["title"]))
print("layman len:", len(struct_out["layman_summary"]))
print("summary len:", len(struct_out["summary"]))
# validate round-trip
for f in ["research_out.json", ".terminal_claude_agent_struct_out.json"]:
    json.loads((WS / f).read_text(encoding="utf-8"))
    print("valid JSON:", f)
