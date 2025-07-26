## mode: 'agent' description: 'Decompose complex tasks into a chain of focused, stepwise prompts.'

# Prompt Chaining Template

You will break down the user's high-level task into a sequence of smaller, manageable steps. For each step:

1. Clearly state the subtask and its objective.
2. Generate a focused prompt for that subtask.
3. Use the output of each step as input for the next.
4. Continue until the overall task is complete.

## Example Workflow

- Step 1: Extract relevant information from the source document.
- Step 2: Summarize or transform the extracted information as required.
- Step 3: Synthesize the final output using the results of previous steps.

Always use symbolic references for files and keep each prompt concise for token efficiency.
