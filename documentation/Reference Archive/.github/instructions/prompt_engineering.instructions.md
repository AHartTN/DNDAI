# Copilot Instructions: Prompt Engineering

## Purpose
Establish best practices for prompt engineering in the DNDAI research workspace. All prompts should support agentic reasoning, reproducibility, and research clarity.

## Frameworks
- Use ReAct (Reasoning and Acting), ToT (Tree of Thoughts), and CoS (Chain of Science) frameworks for all prompt and agent design.
- Document the reasoning process in comments and docstrings.

## Guardrails
- Do not generate prompts for application build/run/test commands.
- You MAY generate prompts for research, navigation, file management, and demonstration commands (e.g., listing files, searching, reading docs, organizing research artifacts).
- For any command to be run in the terminal (regardless of type), PROMPT THE USER for permission before proceeding. Only proceed after explicit user approval.
- All prompt templates must be suitable for research, planning, or prototyping only.
- Place all prompt templates in `.github/prompts/`.

## Directory Structure Reference
- `research/` — Research, planning, and reference documents
- `.github/prompts/` — Prompt templates
