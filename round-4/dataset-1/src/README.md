# Application Anchor — Short Professional Legal / News / Regulatory Documents
### with triple-schema gold facts + char-span provenance  ·  iter_4 (scaled to 84 docs)

`data_out.json` is the genre-faithful **application anchor** for the
text → FOL → Prolog neuro-symbolic atomic-fact-extraction & hallucination-control
experiment. It standardizes **84 short, professionally-written documents**
(**30 legal / 28 news / 26 regulatory**) to ONE shared `(head, relation, tail)`
triple schema with character-span provenance, coarse `{PER,LOC,ORG,TIME,NUM,MISC}`
entity typing, a crisp-vs-silver `gold_quality` flag, a per-row license, and folds
for both leave-one-genre-out **and** a crisp-only subset.

**NO LLM is used in gold construction** (preserves non-circularity for the
hallucination experiment). Entity spans/types and silver facts come from offline
tools only (spaCy NER, NLTK WordNet, regex/structure). This is a strict
superset-in-spirit of the iter_2 24-doc anchor: same corpora, same standardization,
same non-circularity guarantee — just larger, cleaner, and richer.

## What's new in iter_4 (vs the 24-doc iter_2 anchor)
- **Legal CRISP scaled 8 → 30** (the priority lever). CUAD's 510 contracts are
  mostly long (median ~33k chars); beyond the ~21 naturally short whole contracts
  we add **deterministic excerpt windows** — pick the ~1.3–3.5k-char window over
  the densest cluster of ≥3 fully-contained human clause spans (preferring the
  Document-Name/Parties preamble), snap to clean sentence/paragraph boundaries
  (NO mid-sentence truncation), **re-base** every clause offset into the excerpt
  (`s' = s − w_start`), keep only fully-contained clauses, and **re-verify** every
  re-based span. One excerpt per distinct contract preserves diversity. Still 100%
  human-annotated → `gold_quality='crisp'`.
- **Regulatory silver deepened 8 → 26** (15 GDPR + 11 eCFR). More GDPR articles
  (38 fetched, 19 in-band) and **6 eCFR parts round-robined** for breadth
  (Reg E, Reg P, COPPA, FTC Safeguards, Reg S-P, HIPAA). Recall deepened: capture
  ALL regex matches and add `prohibits`, `applies_to`, `defined_as`, per-paragraph
  `has_paragraph`/`has_provision` facts.
- **News silver broadened 8 → 28**: added quote attribution (`say`/`announce`/…),
  dependency-gated `located_in` (locative preposition + GPE/LOC tail, NOT adjacency),
  and an explicit `met_with` relation, on top of the NE↔NE SVO + `occurred_on` +
  `affiliated_with` rules.
- **New per-row metadata** (both deterministic, NO model):
  - `metadata_crisp_subset` (bool) — a crisp-only fold alongside the genre folds.
  - `metadata_decidable_fraction` (float in [0,1]) — composite coverage proxy =
    mean of `sentence_coverage`, `entity_participation`, `char_coverage`
    (reported in `metadata_decidable_subscores`). A **descriptive** row feature
    (like `num_facts`) so the experiment can rank/select the most-decidable docs;
    **NOT** an experiment metric.

## Files
| file | purpose |
|---|---|
| `data_out.json` / `full_data_out.json` | the dataset (`exp_sel_data_out` schema), 84 examples |
| `mini_data_out.json` | first 3 examples per source group for prototyping |
| `preview_data_out.json` | mini with strings truncated to 200 chars |
| `dataset_meta.json` | counts, sources, licenses, relation vocab, decidable_fraction summary, determinism |
| `schema/row_payload_schema.json` | JSON Schema for the inner `input`/`output` payloads |
| `data.py` | **canonical entrypoint**: builds + standardizes + writes all outputs |
| `regenerate.sh` | `python data.py` + verify + mini/preview (deterministic, no network) |
| `build/` | `fetch_sources.py` (the only network step) + `common.py` + `build_{legal,news,regulatory}.py` + `verify_dataset.py` |
| `raw/` | cached raw source snapshot (CUAD, GDPR, Wikinews, eCFR) + `nltk_data` |
| `temp/datasets/CANDIDATE_EVALUATION.md` | the HF/web source-evaluation log (4 kept, MAUD/LEDGAR/ContractNLI/… excluded) |

`datasets[]` is grouped by **source corpus** (CUAD / Wikinews / GDPR / eCFR);
each document is ONE example. `metadata_fold = genre` enables leave-one-genre-out;
`metadata_crisp_subset` enables a clean crisp-only fold.

## Row schema (`datasets[g].examples[i]`)
`input` and `output` are **JSON strings** (decode with `json.loads`):
- `input`  → `{doc_id, document_text, genre, source, char_length, entities:[{name,type,char_span:[s,e]}]}`
- `output` → `{gold_atomic_facts:[{head, relation, tail, provenance_char_span:[s,e]}]}`
- metadata: `metadata_fold`(=genre), `metadata_genre`, `metadata_gold_quality`(crisp|silver),
  `metadata_crisp_subset`(bool), `metadata_decidable_fraction`(float), `metadata_decidable_subscores`,
  `metadata_source`, `metadata_license`, `metadata_relation_vocab`, `metadata_char_length`,
  `metadata_num_facts`, `metadata_num_entities`, `metadata_doc_id`, `metadata_excerpt` (legal),
  `metadata_entity_types_fine` (optional).

## Sources & licenses (all free for commercial + research reuse)
| genre | source | license | gold |
|---|---|---|---|
| legal | **CUAD v1** (Atticus Project), human clause spans + deterministic excerpt windows | CC BY 4.0 | **crisp** |
| news | **Wikinews** articles | CC BY 2.5 | silver (spaCy SVO + 5W + quote attribution) |
| regulatory (EU) | **GDPR** / Reg (EU) 2016/679 (EUR-Lex CELEX:32016R0679) | EUR-Lex free reuse | silver (structural regex) |
| regulatory (US) | **eCFR** §§ (Reg E/P, COPPA, FTC Safeguards, Reg S-P, HIPAA) @ 2024-12-31 | US public domain (17 USC §105) | silver (structural regex) |

**Excluded** (documented in `dataset_meta.json`): MAUD (source texts CC-BY-**NC**-SA;
multiple-choice on very long docs), LEDGAR (provision *classification*, no span facts),
ContractNLI (CC-BY-**NC**-SA), REDFM (CC BY-SA-**NC**), WebRED (sentence-level TFRecord),
LDC ACE/TACRED (research-restricted). No free-license span-annotated 5th legal corpus
exists, so CUAD excerpt windows supply the crisp depth.

## Verification (`python build/verify_dataset.py`) — independently re-parses every string
- **84 docs** (legal 30 / news 28 / regulatory 26); char_length 1161–3493 (mean 2196), in band.
- **2774 / 2774 entity char_spans verify** (`document_text[s:e]==name`); all types in the coarse set.
- **547 facts**; value-tails are substrings of their provenance span (98.5%); clause/label facts
  carry the annotated clause/structure span as evidence. Fact heads link to the doc 100%, tails 98.5%.
- **crisp_subset 30/84**; `decidable_fraction` composite min 0.114 / mean 0.304 / median 0.248 / max 0.769
  (regulatory mean 0.466 > news 0.240 > legal 0.223).
- 41 distinct relations. **0 span errors, 0 warnings.** Validates against `exp_sel_data_out`.
- Deterministic: `regenerate.sh` reproduces **byte-identical** `data_out.json` (seed 42, pinned tools).

## Reproduce
```bash
bash regenerate.sh          # network-free: rebuild from cached raw/, verify, write variants
python build/fetch_sources.py all   # ONLY to refresh raw/ from the live sources (network)
```
Pinned: python 3.12, spaCy 3.7.5 + en_core_web_sm 3.7.1, numpy 1.26.4 (spaCy ABI-crashes on numpy≥2),
nltk 3.9.1 (wordnet/omw-1.4), beautifulsoup4 4.12.3 (lxml 5.3.0). `PYTHONHASHSEED=42`, `SEED=42`.

## Limitations
Legal gold is **crisp** (CUAD human clause-span annotation), including the excerpt-window docs
whose every clause span is re-based and re-verified. News & regulatory gold are **silver**
(deterministic rule/structure curation, no LLM): facts are span-supported and high-precision, but
rule-based recall is partial — `metadata_decidable_fraction` reports this per-document coverage so
the experiment can select the most-decidable docs. `gold_quality` + `crisp_subset` carry the
crisp/silver split per row.
