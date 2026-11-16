# Development and evaluation

## Repository language

All tracked project content uses English. This includes documentation, example prompts, and published evaluation records. The installed skill still follows the language requested by its users. Historical runtime records have English publication translations; see [translation provenance](../evaluations/results/runtime-simplification/translation-note.md). New evaluation runs should use English prompts.

## Develop locally

Clone the repository, then install your checkout into a separate test project if you want to test changes before publishing:

```bash
git clone https://github.com/h6angel/Authenticism.git
cd Authenticism
npx skills add . --list
```

From a separate test project's directory, replace the path below with your checkout:

```bash
npx skills add /path/to/Authenticism --skill authenticism -a codex
```

The root `SKILL.md` is the installable skill entry point; no nested skill folder or custom installer is required. The CLI can install supporting repository files, including development materials. Those materials are not loaded during normal use. This repository does not currently publish a separate minimal release archive.

## Repository layout

```text
SKILL.md              Entry point and essential rules
agents/               Codex interface metadata
references/           Research, reading, explanation, and note formats
schemas/              Research-note JSON schema
scripts/              Structural and quotation checks
tests/                Script tests
evaluations/          Cases, scoring protocol, fixtures, and recorded results
```

## Validate

### Where to save evaluation runs

Save new trial runs under `evaluations/local-runs/<run-name>/` by default. This directory is ignored by Git, so ordinary staging such as `git add .` will not include its contents. Create it when needed; do not force-add temporary runs.

`evaluations/results/` contains deliberately published evaluation evidence, not automatic output. Existing records remain tracked. Only copy a representative run into that directory when it supports a documented version check or comparison. Include its request, actual outputs, relevant source and execution records, review, and a report explaining conditions and limitations. Keep relative links and source-snapshot paths valid when copying; exclude unrelated temporary files and private data.

Ordinary skill use saves answers in the user's chosen location, outside these evaluation directories. Git ignore rules do not redirect output: evaluation executors must be given the local run path explicitly. They also do not remove already tracked files or define a minimal installation package.

### Run checks

Run from the repository root:

```bash
python -X utf8 -m unittest discover -s tests -v
python -X utf8 scripts/validate_notes.py evaluations/fixtures/valid-notes.json
python -X utf8 scripts/check_quotes.py evaluations/fixtures/valid-notes.json
```

For your own task, replace the fixture path with its `research-notes.json`. Scripts emit JSON: exit code `0` means passed, `1` means invalid input or mismatch, and `2` means a quotation cannot be verified. A textual match does not prove attribution, context, or literary quality.

## Evaluation status

The repository includes four development cases, two synthetic holdout passages, adversarial variants, a scoring rubric, and a research-to-explanation smoke example. Mechanical tests have passed. A [single-run before/after development comparison](../evaluations/results/runtime-simplification/report.md) covers three requests with independent executors and one blinded model reviewer. It found usable outputs under shorter instructions, without consistent quality improvement. Skill-versus-no-skill baselines, repeated runs, human scoring, and whole-novel generalization remain untested; improved literary sensitivity is a design goal, not a demonstrated benchmark result.

See [the evaluation protocol](../evaluations/protocol.md) and [implementation checks](../evaluations/results/implementation-check.md). Translated fixtures are a revised evaluation set; historical smoke checks do not establish performance on the revised set.
