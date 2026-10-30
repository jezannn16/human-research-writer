![Human Research Writer cover](assets/cover.png)

# Human Research Writer

[English](README.md) · [Русский](README.ru.md) · [Español](README.es.md)

**Make research read like someone understood it.**

A reusable agent skill for clear, natural academic writing grounded in verifiable sources, with deliberate style rules and a transparent source-review process.

## What it does

Draft or revise coursework, chapters, sections, tables and research-based academic text. It responds in the language requested by the user.

## How it works

Connects factual claims to evidence, separates analysis from sourced claims and removes stock phrasing and decorative typography while preserving quotations and formatting.

## Requirements

The independent audit workflow calls for the newest available Luna with medium reasoning. If unavailable, the skill labels the result as a draft. The style checker requires Python.

## Install

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/jezannn16/human-research-writer.git ~/.agents/skills/human-research-writer
```

## Try it

> Use the provided sources to draft one academic chapter in clear, natural language with citations.

See [SKILL.md](SKILL.md) and [references/](references/) for the complete workflow.

## Research basis

This skill draws inspiration from Russell et al., [StoryScope: Investigating idiosyncrasies in AI fiction](https://arxiv.org/abs/2604.03136v6). The paper studies fictional narratives; applying its observations to academic writing is an adaptation, not a validated result. The skill does not promise to identify authorship or bypass AI detectors.
