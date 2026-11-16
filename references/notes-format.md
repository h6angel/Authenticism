# Research records and script interfaces

The [schema](../schemas/research-notes.schema.json) defines the complete structure. Scripts require Python 3.10+ and only the standard library. `notes_common.py` implements the limited schema keywords used here; it is not a general JSON Schema engine. Update the validator and tests when extending the schema. Version-specific requirements (the 1.1 groups and essay plan) are enforced by notes_common.validate in addition to the shared JSON schema.

## Task files

```text
<task>/
  research-notes.json
  sources/             # Necessary UTF-8 excerpts with provenance and coverage
  explanation.md
  review.json          # Mechanical checks and a short semantic review
```

A source's `snapshot` is relative to the notes file's directory. Paths or symlinks must not escape that directory. A snapshot cannot prove provenance by itself: save material actually read rather than manufacturing text to pass a check.

## Fields

- `schema_version`: write `1.1` for new notes. Historical `1.0` records remain readable; no historical result is retroactively upgraded.
- `work`: title, author, edition (null if unknown), medium, and optional language.
- `request`: the actual request.
- `sources`: unique ID, title, type, URL/location, language, ISO access date, and actual coverage; optional edition and local snapshot.
- `understanding`: `story/characters/tone/ideas/highlights/ending/context/reception`. Version 1.1 requires all eight groups; empty arrays are allowed for irrelevant or unavailable material. For whole-work explanations, story entries should preserve connected development, not only isolated facts.
- `essay_plan`: required in 1.1; `throughline` describes the article's progression, `sections` lists each section's distinct purpose, and `context_reception_decision` explains the inclusion or omission of that material. A focused task may have one section. The plan contains editorial decisions, not unsourced factual claims.
- Each entry: unique ID, statement, `fact/observation/interpretation`, references, scope, and status. Use optional `qualification` for limitations.
- Each `source_refs` item: `source_id` and `locator`. A `supported` entry needs a source; referencing memory does not establish verification.
- `quotes`: unique ID, text, source ID, locator, and `verbatim/self_translation`. Use an empty array when there are no quotations.
- `open_questions`: unresolved important gaps, or an empty array.

`supported` means supported by current material, not uniquely correct. `provisional` awaits verification; `disputed` retains a conflict. Complete fields do not replace reading.

The [runnable fixture](../evaluations/fixtures/valid-notes.json) uses original synthetic text and tests data and tooling only.

## Commands and interpretation

```text
python -X utf8 scripts/validate_notes.py <task>/research-notes.json
python -X utf8 scripts/check_quotes.py <task>/research-notes.json
python -X utf8 -m unittest discover -s tests -v
```

JSON output; exit codes: 0 passed, 1 error, 2 unverifiable. Quote checking first validates notes, then attempts exact matching, followed only by whitespace normalization. Punctuation remains significant. No fuzzy matching or automatic network requests. Self-translations require semantic review.

With no quotations, `checked: 0` is not a whole-essay verification. Scripts do not extract quotations from the final essay: register every direct quotation and review attribution, location, and context. A quote absent from a partial snapshot requires re-reading, not a claim that it is absent from the original.
