# Authenticism

A research-driven literary explanation skill for Codex. Give it a novel or short-story title; it finds relevant sources and explains the story, characters, central ideas, and artistic highlights while preserving the work's distinctive tone.

Authenticism aims to prevent generic interpretations from flattening a work into a familiar story of trauma, growth, or redemption. It also avoids the opposite bias: imposing cruelty or hidden malice on a genuinely tender work.

## Install

Install with the community [Skills CLI](https://github.com/vercel-labs/skills). You need Node.js 22.20 or later and access to this repository.

```bash
npx skills add h6angel/Authenticism --skill authenticism -a codex -g
```

This installs for your user across projects. Omit `-g` to install only in your current project:

```bash
npx skills add h6angel/Authenticism --skill authenticism -a codex
```

Browse the available skill before installing:

```bash
npx skills add h6angel/Authenticism --list
```

Codex normally discovers installed skills automatically. If it does not appear, restart Codex. For private repositories, configure Git/GitHub authentication as described in the [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

The commands above install the version published on GitHub. Uncommitted or unpushed local changes are not included. There is no separate Authenticism npm package, hosted service, or API key requirement.

## Use

Mention the skill explicitly in a Codex prompt:

```text
$authenticism Explain Elfriede Jelinek's The Piano Teacher in detail.
Cover the story, characters, central ideas, artistic highlights, and ending.
Spoilers are welcome.
```

```text
$authenticism Introduce The Gift of the Magi without revealing the twist.
```

```text
$authenticism Explain The Yellow Wallpaper and save the explanation as Markdown.
```

No source-document upload is required. The skill uses Codex's available search and reading tools, distinguishes primary text from criticism and adaptations, and connects interpretation to actual details. It follows your requested language; English instructions do not restrict explanations to English.

The result is a coherent literary explanation, not a table of evidence. Detailed tasks can also retain research notes and verification records in the output directory you choose.

## Requirements and limitations

- Codex or another compatible agent must provide the underlying model and tools. Installing a skill does not add a search engine or connector.
- Web search and page-reading access are needed for independent online research. If unavailable, the skill explains the limitation and works within accessible material.
- Optional verification scripts require Python 3.10+ and use only the standard library. The core instructions do not need Python to be read.
- The current reading framework focuses on novels and short stories.
- Primary text may be inaccessible. The skill must not imply a full close reading, invent quotations, or attribute translated wording to an unread original.

## Update or uninstall

For the user-level installation:

```bash
npx skills update authenticism -g
npx skills remove authenticism -a codex -g
```

For a project installation, use `npx skills update authenticism -p` and omit `-g` from the remove command. See the [Skills CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for scope and installation options.

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

Run from the repository root:

```bash
python -X utf8 -m unittest discover -s tests -v
python -X utf8 scripts/validate_notes.py evaluations/fixtures/valid-notes.json
python -X utf8 scripts/check_quotes.py evaluations/fixtures/valid-notes.json
```

For your own task, replace the fixture path with its `research-notes.json`. Scripts emit JSON: exit code `0` means passed, `1` means invalid input or mismatch, and `2` means a quotation cannot be verified. A textual match does not prove attribution, context, or literary quality.

## Evaluation status

The repository includes four development cases, two synthetic holdout passages, adversarial variants, a scoring rubric, and a research-to-explanation smoke example. Mechanical tests have passed. Independent baseline comparisons, repeated runs, and human-scored generalization tests have not been completed; improved literary sensitivity is a design goal, not a demonstrated benchmark result.

See [the evaluation protocol](evaluations/protocol.md) and [implementation checks](evaluations/results/implementation-check.md). Translated fixtures are a revised evaluation set; historical smoke checks do not establish performance on the revised set.
