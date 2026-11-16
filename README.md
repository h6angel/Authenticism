# Authenticism

**Understand a novel, and understand why it is written that way.**

A literary explanation skill for novels and short stories. Starting from plot, characters, and specific passages, it explains how a work creates its distinctive meaning and emotional effect. You can explore a whole work or keep discussing a single scene or sentence.

[See an example](#see-an-example) · [Quick install](#quick-install) · [First use](#first-use)

## See an example

**Request**

> Continuing our discussion of The Metamorphosis: why does Gregor still worry first about being late for work after turning into an insect? Focus on this question; there is no need to retell the whole work.

**Excerpt from a recorded answer** (translated from the original Chinese; intervening paragraphs omitted)

> For Gregor, **going to work has become a reflex of responsibility that precedes self-preservation**: something inconceivable has happened to his body, yet he still judges himself by the rules of a working day.
>
> Still, "worries first about being late" needs a little qualification. Initially he is bewildered, tries to turn over, and even wants to sleep again and forget the whole thing. But his thoughts quickly turn to exhausting business travel, trains, and his employer. This shift suggests that work has long occupied a central place in how he understands his life.

...

> Kafka places these two scales side by side: the reader sees someone undergoing an immense upheaval in his existence, while Gregor is still calculating how to catch the next train. There is absurd comedy here, but also a painful earnestness: **he can no longer get out of bed normally, yet he still feels obliged to report for work on time.** The transformation immediately changes his body, but it does not immediately release him from the order of responsibility and punishment within him.

[Read the full translated answer](evaluations/results/runtime-simplification/runs/after-followup/answer.md) · [Execution and source coverage](evaluations/results/runtime-simplification/runs/after-followup/execution.json)

This answer comes from a development run on November 16, 2026. The executor read the opening of chapter I in David Wyllie's English translation, not the complete novella or the German original; its exact model deployment was not exposed. Despite the request's conversational wording, the test supplied only this self-contained question, without earlier turns. It illustrates a focused answer, not a multi-turn test or a comparison against using no skill. The English text is an editorial translation, not a new model run.

For a whole-work explanation, read the [translated answer on The Yellow Wallpaper](evaluations/results/runtime-simplification/runs/after-analysis/answer.md) from the same development comparison (contains ending spoilers).

## Quick install

Install into Codex using the community [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add h6angel/Authenticism --skill authenticism -a codex -g
```

You need Node.js, network access, and access to the repository. `-g` installs for your user across projects; omit it to install only in the current project. Private repositories require Git/GitHub authentication.

Codex normally discovers installed skills automatically. If it does not appear, restart Codex. This command installs the version on GitHub; local changes that have not been pushed are not included.

## First use

Mention `$authenticism` in Codex, then name the work and what you want to explore:

```text
$authenticism Explain Charlotte Perkins Gilman's The Yellow Wallpaper in detail,
including the story, relationships, writing, and ending. Spoilers are welcome.
```

| What you want | Example request |
| --- | --- |
| An introduction before reading | `$authenticism Introduce The Gift of the Magi without revealing the final twist.` |
| A closer look at one scene | `$authenticism Why is the moonlit conversation between the couple a turning point in The Yellow Wallpaper?` |
| Discussion of another reading | `$authenticism I find a sense of liberation in the ending of The Yellow Wallpaper. What supports that reading, and what are its limits?` |
| An explanation saved to a file | `$authenticism Explain The Metamorphosis and save the explanation as Markdown.` |

No source upload is required: the skill uses the search and reading tools available in your environment. If you care about a particular translation or wording, supplying the edition or passage helps. Answers follow your language and spoiler preferences. Unless you specify otherwise, introductions and explanations develop the whole work and flag spoilers at the start.

## How it reads

- **Connect story and writing.** Explain what characters experience and how perspective, language, pacing, and details shape the reading experience.
- **Bring interpretation back to the text.** Ground judgments in events and wording; distinguish originals, translations, adaptations, and criticism. State material limitations rather than inventing quotations.
- **Preserve each work's tone.** Avoid making every story about trauma, growth, or redemption, or assuming that tenderness conceals cruelty.
- **Follow your question.** Explore a whole work, focus on a passage, or examine a different reading. Ordinary chat does not require a research archive; exporting an essay alone does not require one either.

## Requirements and limits

The skill currently targets Codex, with a reading framework focused on novels and short stories. Compatibility with other agent platforms is not established here.

The skill supplies methods and instructions; your environment supplies the model, search, and page-reading tools. When browsing or primary text is unavailable, it should explain the limitation rather than present secondary research as a full close reading or attribute translated wording to an unread original. Optional research-record checks require Python 3.10+; ordinary use does not require Python.

The examples show recorded output, but do not establish consistent improvement over ordinary prompting. Current evidence consists of limited development checks and a single-run before/after instruction comparison, without skill-versus-no-skill baselines, repeated runs, or human scoring. See [development and evaluation](docs/development.md#evaluation-status).

## Update or uninstall

For a user-level installation:

```bash
npx skills update authenticism -g
npx skills remove authenticism -a codex -g
```

For a project installation, use `npx skills update authenticism -p` and omit `-g` from the remove command. See the [Skills CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for more options.

## Did an explanation fail to convince you?

Share feedback through [GitHub Issues](https://github.com/h6angel/Authenticism/issues). Include the work and author, your request, the relevant answer excerpt, your model environment, and where you think the interpretation loses touch with the text. Plot errors, unsupported claims, overlooked counterexamples, and a mismatch with the work's tone are all useful to discuss.

## Development and evaluation

[Development, layout, and checks](docs/development.md) · [Evaluation protocol](evaluations/protocol.md) · [Before/after comparison](evaluations/results/runtime-simplification/report.md)

`SKILL.md` is the entry point, `references/` contains reading guidance, and `agents/` contains Codex interface metadata. `evaluations/results/` holds selected development evidence; it is not required reading during normal use or a destination for everyday answers. New trial runs belong in the Git-ignored `evaluations/local-runs/` directory. There is currently no separate minimal release archive, so installation tools may include development materials.
