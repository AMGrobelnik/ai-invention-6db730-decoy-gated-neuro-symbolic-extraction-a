# Application Anchor — Short Professional Legal / News / Regulatory Documents
### with triple-schema gold facts + char-span provenance

`data_out.json` is the genre-faithful **application anchor** for the
text → FOL → Prolog neuro-symbolic atomic-fact-extraction & hallucination-control
experiment. It standardizes **24 short, professionally-written documents**
(8 legal / 8 news / 8 regulatory) to ONE shared `(head, relation, tail)` triple
schema with character-span provenance, coarse `{PER,LOC,ORG,TIME,NUM,MISC}`
entity typing, a crisp-vs-silver `gold_quality` flag, a per-row license, and a
genre fold for leave-one-genre-out.

**NO LLM is used in gold construction** (preserves non-circularity for the
next-iteration hallucination experiment). Entity spans/types and silver facts
come from offline tools only (spaCy NER, NLTK WordNet, regex/structure).

## Files
| file | purpose |
|---|---|
| `data_out.json` / `full_data_out.json` | the dataset (`exp_sel_data_out` schema) |
| `mini_data_out.json` | 3 examples (one per genre) for prototyping |
| `preview_data_out.json` | mini with strings truncated to 200 chars |
| `dataset_meta.json` | counts, sources, licenses, relation vocab, determinism notes |
| `schema/row_payload_schema.json` | JSON Schema for the inner `input`/`output` payloads |
| `data.py` | **canonical entrypoint**: builds + standardizes + writes all outputs |
| `regenerate.sh` | `python data.py` + verify (deterministic, no network) |
| `build/` | `fetch_sources.py` (network) + `common.py` + `build_{legal,news,regulatory}.py` + `verify_dataset.py` |
| `raw/` | cached raw source snapshot (reproducibility) + `nltk_data` |

`datasets[]` is grouped by **source corpus** (CUAD / Wikinews / GDPR / eCFR);
each document is ONE example. `metadata_fold = genre` still enables
leave-one-genre-out across the 8 legal / 8 news / 8 regulatory docs.

## Row schema (`datasets[0].examples[i]`)
`input` and `output` are **JSON strings** (decode with `json.loads`):
- `input`  → `{doc_id, document_text, genre, source, char_length, entities:[{name,type,char_span:[s,e]}]}`
- `output` → `{gold_atomic_facts:[{head, relation, tail, provenance_char_span:[s,e]}]}`
- metadata: `metadata_fold`(=genre), `metadata_gold_quality`(crisp|silver),
  `metadata_source`, `metadata_license`, `metadata_relation_vocab`,
  `metadata_char_length`, `metadata_num_facts`, `metadata_num_entities`,
  `metadata_entity_types_fine`.

## Sources & licenses (all free)
| genre | source | license | gold |
|---|---|---|---|
| legal | **CUAD v1** (Atticus Project), human-annotated clause spans | CC BY 4.0 | **crisp** |
| news | **Wikinews** articles | CC BY 2.5 | silver (spaCy SVO+5W) |
| regulatory (EU) | **GDPR** / Reg (EU) 2016/679 (EUR-Lex CELEX:32016R0679) | EUR-Lex free reuse | silver (structural regex) |
| regulatory (US) | **eCFR** sections | US public domain | silver (structural regex) |

**Excluded** (documented in `dataset_meta.json`): REDFM (CC BY-SA-**NC**),
ContractNLI-HF (CC BY-**NC**-SA) — fail the free-license rule; WebRED (usable but
sentence-level TFRecord, not genre-faithful documents).

## Verification (run `python build/verify_dataset.py`)
- 24 docs, balanced 8/8/8; char_length 1239–3474 (mean 2372), in band.
- **946 / 946 entity char_spans verify** (`document_text[s:e]==name`); all types in the coarse set.
- 140 facts; value-tails are substrings of their provenance span; clause/label
  facts carry the annotated clause span as evidence.
- entity-linking baseline: **93.6%** of fact endpoints link to the typed `entities[]`.
- Deterministic: `regenerate.sh` reproduces byte-identical `data_out.json` (seed 42, pinned tools).

## Relation vocabularies (per genre, controlled / documented)
- **legal**: has_title, has_party, agreement_date, effective_date, expiration_date,
  governed_by, renewal_term, notice_to_terminate_renewal, liability_cap,
  warranty_duration, revenue_profit_sharing, contains_* (clause-presence).
- **news**: action predicates (verb lemmas: score, direct, win, choose, call, …),
  occurred_on, affiliated_with.
- **regulatory**: has_title, grants_right, obligates, has_exception,
  cross_references, defined_as, requires.

## Limitations
Legal gold is **crisp** (CUAD human annotation). News & regulatory gold are
**silver** (deterministic rule/structure curation, no LLM): facts are
span-supported and high-precision, but rule-based recall is partial. The
`gold_quality` flag carries this per row.
