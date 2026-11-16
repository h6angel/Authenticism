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
