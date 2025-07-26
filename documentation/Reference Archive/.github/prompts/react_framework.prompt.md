# Copilot Prompt: ReAct Framework

## Context
Apply the ReAct (Reasoning and Acting) framework for agentic reasoning in research and planning tasks for the DNDAI project.

## Instructions
- When responding to research or planning queries, explicitly separate reasoning steps from actions.
- Use clear, stepwise logic in all code, comments, and documentation.
- All outputs must be suitable for research, not for direct execution.

## Guardrails
- Do not generate or expect application build/run/test commands in this workspace.
- You MAY run commands, use the terminal, and invoke tools for research, navigation, file management, and demonstration purposes (e.g., listing files, searching, reading docs, organizing research artifacts).
- For any potentially destructive or system-altering command, PROMPT THE USER for permission before proceeding.
- Document all reasoning and actions in comments or docstrings.
