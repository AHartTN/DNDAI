## mode: 'agent' description: 'Orchestrate agentic workflows as reasoning graphs, not just linear prompts.'

# Agentic Workflow Orchestration Template

You are to design and execute a reasoning graph for the user's high-level objective. For each node in the graph:

1. Define the subtask and its dependencies.
2. Generate a prompt or tool invocation for that node.
3. Use outputs from dependent nodes as input.
4. Iterate and self-correct as needed, using Reflexion or Metacognitive steps.

Document the workflow structure and use symbolic references throughout. Prioritize token efficiency and reproducibility.
