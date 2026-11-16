# Initial implementation checks

Date: 2026-11-16. This records actual implementation checks, not an independent literary benchmark.

## Implemented scope

- Entry point and research, reading, and explanation rules are operational; scripts have no unimplemented placeholders.
- Notes schema, dependency-free structural validation, reference checks, and snapshot quote matching are implemented.
- Four published-work development cases contain requests, coverage requirements, stance variants, and false corrections. Source identity pages were opened; formal scoring still requires case-by-case primary reading.
- Two original synthetic holdouts probe limited narrative distinctions, not long-novel generalization. They remain unrun; the author knows their contents, so independent executors must not see expectations.
- Comparison protocol, six-dimensional anchors, hard errors, paired metrics, and a score template are present.

## Actual smoke run

[D01-smoke](D01-smoke/explanation.md) used independently located English text of The Yellow Wallpaper to produce notes and a concise explanation. The continuous story was read rather than relying solely on its automatically generated description. Only a necessary short quotation was retained locally; other locations refer to the web reader.

This illustrates content and tool flow, not a full-length scored response. No independent blind conditions, effectiveness scores, or fabricated baseline were used. Notes validation passed and one direct quotation matched exactly. The delivered explanation contained no direct quotations, so this was not represented as automatic verification of an entire essay. See review.json in that directory.

## Commands

```text
python -X utf8 -m unittest discover -s tests -v
python -X utf8 scripts/validate_notes.py evaluations/fixtures/valid-notes.json
python -X utf8 scripts/check_quotes.py evaluations/fixtures/valid-notes.json
python -X utf8 scripts/validate_notes.py evaluations/results/D01-smoke/research-notes.json
python -X utf8 scripts/check_quotes.py evaluations/results/D01-smoke/research-notes.json
```

Twelve unit/CLI tests passed, covering structure, missing fields, types, dangling references, duplicate IDs, exact matching, whitespace, punctuation, missing snapshots, self-translations, path escape, and exit codes. JSON syntax, local Markdown links, and diff whitespace checks passed.

The skill-creator quick validator passed with UTF-8 mode. Its default Windows GBK decoding failed on UTF-8 files; `-X utf8` resolved it. Initial tests encountered sandbox restrictions in the system temporary directory and passed after execution permission was granted.

## English revision

Instructions, metadata, evaluation cases, and this report were translated to English. Synthetic passages were adapted into English; their language-level effects must be evaluated anew. The D01 explanation and notes below are translated artifacts of the historical author smoke run, not a new independent run. The quotation snapshot remains unchanged. Mechanical checks are rerun for this revision.

All twelve unit/CLI tests passed again after translation. The historical smoke notes still pass structural and quotation checks, and the skill manifest passes the bundled quick validator. A repository scan found no remaining Chinese text. JSON parsing and local Markdown links were checked again.

The Skills CLI command `npx --yes skills add . --list` successfully discovered exactly one local skill, `authenticism`, from the repository root. This was discovery only: no user-level installation or remote-release installation was performed. Node.js used for the check was v24.18.0. Downloading the CLI initially failed under the sandbox's cache-only mode and succeeded after network execution permission was granted. The README now uses the configured GitHub remote, `h6angel/Authenticism`; publishing the current local revision remains a separate step.

## Effectiveness status

Independent baseline comparisons, repeated runs, dual-reader scoring, and real-work holdout evaluation have not been executed. No independent model runner is configured; no additional chats or delegated agents were created. These checks cannot establish improved literary sensitivity. Follow protocol.md in independent sessions for that validation.

## Whole-work explanation revision (2026-11-16)

Replaced the writing guide's optional topic outline with connected story overview, editorial planning, sustained development, independent attention to form, and proportionate context/reception. Updated research selection and completion criteria rather than adding a parallel workflow. Added a complete original miniature story and essay to the existing examples; it is illustrative, not an independent behavioral test.

New notes use version 1.1 with context/reception groups and an essay plan; version 1.0 historical records remain readable. Shared schema validates field structure and the Python validator applies version-specific requirements. Added tests for required planning data, legacy compatibility, and reception source references. Quote matching is unchanged.

All 15 unit/CLI tests passed after permission to rerun outside the system-temp sandbox restriction. Current fixture structure and one exact quote passed; the skill-creator UTF-8 quick validator and diff whitespace check passed. Historical D01 notes were also rechecked for compatibility. No new real-work literary evaluation or user-level skill installation was performed for this revision.

## Explanation-depth revision (2026-11-16)

Retained the whole-work throughline and added scene-level development, section plans identifying explanatory material, a distinction between repetition and further examination, and checks for transitions hidden by summary words. Added a thin-versus-developed comparison using the existing synthetic story and a cross-scene planning example. Reading guidance now checks uneven source coverage; rubric anchors distinguish plausible conclusions from developed explanation. No schema or script changes were needed.

Validation: diff whitespace check and UTF-8 skill quick validation passed. All 15 unit/CLI tests passed on an approved rerun outside the system-temp sandbox restriction; the initial sandbox run had two temporary-directory permission errors.

### Real-work regression: The Vegetarian

Status: not_run. The user supplied a prior output, but no fresh independent session or matched comparison has been executed. No literary-quality improvement is claimed from tooling checks or from examples authored while revising the instructions.

Use the unaugmented request `$authenticism 解析一下素食者这本书` in a fresh session. Compare the parent revision and revised skill under matched model, tools, output budget, and browsing conditions; preserve actual source coverage and source changes. Keep the earlier user output as a diagnostic example rather than a controlled baseline. Following protocol.md, save request, sources, research notes, explanation, and review.

Inspect whether consequential transitions are explained rather than merely named; whether the artist and sister sections develop interactions and changing relationships; whether plant imagery is traced through changes rather than assigned one meaning; and whether additional prose adds supported understanding rather than repeated conclusions. Also check continuity, distinct section contributions, and unsupported specificity. Diagnose remaining weaknesses as retrieval, planning, or drafting gaps before adding further rules. Longer output alone does not pass this regression.
