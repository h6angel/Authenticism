---
name: authenticism
description: Research and explain novels and short stories, connecting plot, characters, central ideas, and artistic highlights while preserving the work's distinctive tone. Use for introductions, detailed explanations, and literary discussion.
---

# Authenticism

## Purpose and scope

Users usually provide only a title. Find and read relevant sources, develop an understanding of the work, and deliver an accessible, substantial Markdown explanation in the user's requested language, or the language of their request.

A request to introduce or explain a work (including “介绍” and “解析”) defaults to a fully developed whole-work reading guide: explain how the story develops, relationships change, and narrative and language create its distinctive meaning and experience. Briefly flag spoilers at the start, then discuss important events and the ending. Follow the user's explicit scope, length, and spoiler preferences.

The current scope is novels and short stories. Do not force poetry or drama into a plot-and-character framework. Simple bibliographic questions do not require the full workflow.

## Essential rules

- Explain the story, relationships, central ideas, key scenes, and artistic highlights. Preserve tone throughout the explanation.
- Distinguish character emotion, narrative attitude, and reader response. Default to neither consolation nor cruelty.
- Separate originals, translations, adaptations, user recollections, and criticism. Verify important facts.
- Never invent quotations or imply a complete close reading when the text was not read.
- Ground interpretations in specific features of the work; theory, theme labels, and user opinions cannot replace reading.
- Present a literary explanation to the reader; keep research and verification records in the background.

## Workflow

1. Identify the work, medium, and any explicit scope preferences.
2. Follow [research.md](references/research.md) to search independently, open sources, and record actual reading coverage. Do not assume the user will upload a document.
3. Follow [reading.md](references/reading.md) to establish the whole work before selecting interpretive questions; connect story, tone, ideas, and form, and investigate important gaps.
4. Follow [explanation.md](references/explanation.md) to plan and write the guide. Consult [examples.md](references/examples.md) when a local interpretation or level of development needs illustration.
5. Review the finished essay using explanation.md and repair gaps in the writing or research.

Ask about identity only when ambiguity materially changes the answer. If primary text is unavailable, continue with reliable materials and briefly limit relevant claims.

## Tools and checks

Use available search tools for discovery, page/text readers for continuous reading, and in-text search for navigation. No particular search provider is required. If browsing is unavailable, disclose that limitation instead of claiming research occurred.

For detailed explanations, file deliverables, and evaluations, save research notes and necessary source excerpts. Brief follow-ups need only relevant source support. Save only necessary, lawfully accessible material with its actual coverage; do not bypass access restrictions.

From the skill directory, replace the task paths below:

```text
python -X utf8 scripts/validate_notes.py <task>/research-notes.json
python -X utf8 scripts/check_quotes.py <task>/research-notes.json
```

The scripts emit JSON. Exit codes: 0 passed, 1 invalid input or mismatch, 2 unverifiable quotations. Re-read, remove the direct quotation, or state the limitation when verification is unavailable. These checks do not assess literary quality or interpretive correctness.

## Supporting resources

- [Research notes schema](schemas/research-notes.schema.json).
- [Fields, examples, and script contracts](references/notes-format.md).
- `evaluations/` is for development and evaluation; do not load it during normal explanations.
- Save task outputs in the user's chosen location, not in the skill's instructions or evaluation fixtures.
