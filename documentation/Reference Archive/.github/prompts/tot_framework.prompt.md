# Copilot Prompt: Tree of Thoughts (ToT) Framework

## Context
Apply the Tree of Thoughts (ToT) framework for agentic reasoning in research and planning tasks for the DNDAI project.

## Instructions
- When responding to research or planning queries, break down complex problems into a tree of possible thoughts/solutions.
- Document each branch and reasoning step in comments or docstrings.
- All outputs must be suitable for research, not for direct execution.

## Guardrails
- Do not generate or expect application build/run/test commands in this workspace.
- You MAY run commands, use the terminal, and invoke tools for research, navigation, file management, and demonstration purposes (e.g., listing files, searching, reading docs, organizing research artifacts).
- For any potentially destructive or system-altering command, PROMPT THE USER for permission before proceeding.
- Document all reasoning and branching in comments or docstrings.
