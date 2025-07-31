# Self-Correction and Guardrails for Autonomous Agents

## Reflexion and Metacognitive Prompting

- After each task, reflect on the process and output.
- Identify mistakes, ambiguities, or inefficiencies.
- Propose corrections and improvements for the next iteration.

## Constitutional AI and Instruction Hierarchy

- Use non-overridable system prompts to enforce alignment and prevent prompt injection.
- Maintain a hierarchy of instructions: system > operational > user.
- Validate all actions against constitutional and operational guardrails before execution.

## Example Reflexion Prompt

Reflect on your last action. Did you:
- Meet the objective?
- Miss any requirements?
- Introduce errors or inefficiencies?
- How will you improve next time?
