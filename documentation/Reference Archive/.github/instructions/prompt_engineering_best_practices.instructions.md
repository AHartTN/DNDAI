---
applyTo: "**/*.md"
---

# Prompt Engineering Best Practices

- Always use symbolic references for key files and documents (see .github/copilot-instructions.md).
- Decompose complex tasks into stepwise, chainable prompts (Prompt Chaining).
- Use prompt compression to minimize token usage for large context.
- Apply Chain-of-Verification for fact-checking and claim validation.
- Orchestrate agentic workflows as reasoning graphs, not just linear chains.
- Use clear delimiters and explicit guardrails in all system prompts.
- Document all prompt templates and instructions for reproducibility.
- Regularly audit and update all prompts and instructions for compliance with the latest research plan.
- For any command to be run in the terminal (regardless of type), always prompt the user for permission and only proceed after explicit approval.
