# Agentic Reasoning Frameworks (ReAct, ToT, Prompt Chaining, Symbolic Linking, Prompt Compression)

## ReAct (Reason + Act) Prompt Template

You are an autonomous agent. For each task, reason step-by-step, then act. Respond with:
- Your reasoning
- The action you will take
- The result or next step

## Tree of Thoughts (ToT) Prompt Template

You are an agent solving a complex problem. Decompose the problem into a tree of possible thoughts/steps. For each branch, evaluate and select the best path. Respond with:
- The decomposed steps
- Evaluation of each branch
- Chosen path and next action

## Prompt Chaining Example

1. Receive user input and context.
2. Generate a clarifying question or subtask prompt.
3. Use the response as input for the next prompt in the chain.
4. Continue until the final output is achieved.

## Symbolic Linking Example

Reference external files or context using symbolic links (e.g., [Extracts/Prompts/Player_Action_Interpretation_Prompt.md]).

## Prompt Compression Example

Summarize or condense context and prior steps to fit within token limits while preserving essential information.
