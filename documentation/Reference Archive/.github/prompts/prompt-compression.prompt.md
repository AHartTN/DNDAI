## mode: 'agent' description: 'Compress or summarize large context before LLM input.'

# Prompt Compression Template

When provided with a large document or code file, your task is to:

1. Identify and extract only the most relevant sections for the user's goal.
2. Summarize or compress the content to minimize token usage while preserving essential meaning.
3. Output the compressed context for use in subsequent prompts or agent actions.

Use symbolic references for all files. Clearly indicate what was omitted and why.
