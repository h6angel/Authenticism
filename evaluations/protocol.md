# Evaluation protocol

## Two layers

Fixed-material mode provides only the request and identical material packs, isolating reading from retrieval. Research mode provides only the request and allows search. Manifest primary_sources are preparation leads, not proof of reading. Synthetic material tests no external factual knowledge.

## Output location

Default new runs to `evaluations/local-runs/<run-name>/` (Git-ignored), and give that path explicitly to executors. Reserve `evaluations/results/` for selected, deliberately published evidence supporting a version check or comparison. Preserve the request, actual outputs, relevant source and execution records, review, and a report of conditions and limitations when promoting a run; verify relative links and source-snapshot paths. Do not publish every trial run. Existing published records remain tracked. See [development guidance](../docs/development.md#where-to-save-evaluation-runs).

## Development and holdout

Revise on development cases, freeze the skill version, then run holdouts. Task executors must not read expectations or scoring answers in advance; raters should read them. Mark holdouts used to tune rules as consumed. The repository author knows these cases, so author runs are smoke checks, not independent blind evaluations.

English translations revise the earlier fixtures. Do not infer revised-set performance from historical runs. Synthetic holdouts offer limited narrative probes, not whole-novel generalization evidence.

## Baseline comparison

Run each request with and without the skill, keeping model, tools, output budget, and browsing conditions matched. Use fresh sessions; do not carry corrections between runs. Prefer three repetitions per condition. Record model, date, revision, budget, tool availability, and actual source coverage. Reuse identical snapshots in fixed mode; record source changes in research mode.

Save request, sources, research-notes, explanation, and review. Never manufacture a baseline by degrading an improved answer. If independent execution is unavailable, record not_run rather than inventing outputs or scores.

For ordinary-chat overhead checks, keep evaluator capture separate from the executor's task. Calling a run an evaluation can legitimately activate evaluation-specific record requirements. Report that contamination rather than attributing its files to ordinary use. A separate plain article-export request can probe whether an essay file alone causes a research archive, but does not establish the behavior of every chat request.

## Paired variants

Execute each variants.json prompt independently. For followup variants, run base first, then followup. Stance changes must not add facts; form changes should retain similar events. Correct evidence-based revision is not sycophancy.

## Rating and reporting

Anonymize and shuffle explanations. Score with rubric.md and expectations, preferably using two independent readers. Differences above one point in any dimension should prompt text-based discussion; retain original scores and reconciliation reasons without requiring identical interpretations.

Report individual scores, hard errors, paired metrics, source coverage, and retrieval failures. Copy score-template.json; null means not scored. If revising after holdouts, prepare new unseen cases.

## Local checks

```text
python -X utf8 -m unittest discover -s tests -v
python -X utf8 scripts/validate_notes.py evaluations/fixtures/valid-notes.json
python -X utf8 scripts/check_quotes.py evaluations/fixtures/valid-notes.json
```

These check tooling, not literary quality. See [implementation checks](results/implementation-check.md) for recorded execution.
