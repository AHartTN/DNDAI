# Copilot Instructions: Research Workspace

## Purpose
This workspace is dedicated to research, planning, and documentation for the DNDAI project. No code should be generated for direct execution. All outputs must be suitable for research, prototyping, or reference only.

## Agentic Reasoning Frameworks
- Use ReAct, ToT, and CoS frameworks for prompt engineering and agentic reasoning.
- When generating code, always include detailed docstrings and comments explaining the reasoning, context, and research intent.
- Prioritize clarity, reproducibility, and research best practices.

## Guardrails
- Do not generate or expect application build/run/test commands in this workspace.
- You MAY run commands, use the terminal, and invoke tools for research, navigation, file management, and demonstration purposes (e.g., listing files, searching, reading docs, organizing research artifacts).
- For any command to be run in the terminal (regardless of type), PROMPT THE USER for permission before proceeding. Only proceed after explicit user approval.
- All new research, plans, and prototypes must be placed under the `research/` directory.
- All documentation and code must remain fully in sync.

## Directory Structure
- `research/` — Research, planning, and reference documents
- `archive/` — Deprecated or old files
- `.github/instructions/` — Copilot instruction files
- `.github/prompts/` — Copilot prompt templates

## Symbolic File References
# (Reserved for future use)
