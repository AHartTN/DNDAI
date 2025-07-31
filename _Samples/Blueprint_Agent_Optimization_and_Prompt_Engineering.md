# Agent Optimization & Prompt Engineering Blueprint

## Token Efficiency

- Use symbolic references for files, modules, and tasks (e.g., _NARRATIVE_ENGINE_ instead of full path)
  - **Instruction:** Define all symbolic references at the start of a session or in a master instruction file. Example:
    - _NARRATIVE_ENGINE_ = #src/ai/narrative_engine.py
    - _ENCOUNTER_GEN_ = #src/ai/encounter_generator.py
- Apply chain-of-symbol (CoS) paradigm for complex relationships
  - **Example:** Instead of "The output of the narrative engine feeds into the encounter generator and item generator," use:
    - _NARRATIVE_ENGINE_ -> _ENCOUNTER_GEN_; _NARRATIVE_ENGINE_ -> _ITEM_GEN_
- Implement prompt chaining for multi-step tasks
  - **Template:**
    1. "Given [input], extract all relevant facts."
    2. "Given [facts], synthesize a summary."
    3. "Given [summary], generate code or output."

## Context Management

- Use @workspace for broad context, #file for focused context
  - **Prompt Example:**
    - "@workspace: Summarize all modules related to encounter generation."
    - "#file:src/ai/narrative_engine.py: Refactor the main story generation function."
- Maintain a symbolic linking system for all critical files
  - **Instruction:** List all symbols and their file paths at the top of each major prompt or document.
- Regularly prune and summarize context to avoid "lost in the middle" issues
  - **Technique:** After every 5-10 steps, summarize the current state and only carry forward the summary and essential symbols.

## Long-Context Strategies

- Break long tasks into discrete, sequential prompts
  - **Example:**
    - Step 1: "Extract all user requirements from the following document."
    - Step 2: "Given the requirements, design a high-level architecture."
    - Step 3: "Given the architecture, generate module stubs."
- Use output of one step as input for the next
- Archive and reference previous steps symbolically
  - **Instruction:** Assign a symbol to each major output (e.g., _REQS_, _ARCH_, _STUBS_) and reference them in subsequent prompts.

## Modular Prompt Design

- Design prompts to be reusable and composable
  - **Template:**
    - "Given [input], perform [task] and output [format]."
- Use templates for common agent tasks (e.g., code generation, analysis, summarization)
  - **Examples:**
    - "Summarize the following code: [code]"
    - "Generate a test suite for [module]"
    - "Analyze the following user story and suggest improvements."
- Document all prompt patterns and update as new techniques are developed
  - **Instruction:** Maintain a prompt pattern log in the documentation for future reference and improvement.


## Prompt Pattern Log

Maintain a running log of all prompt patterns, templates, and techniques used or developed. Update this section as new patterns are created or refined.

**Sample Log Table:**
| Pattern Name         | Description                                 | Example/Template                                  |
|---------------------|---------------------------------------------|---------------------------------------------------|
| Symbolic Reference  | Use short symbols for files/modules         | _NARRATIVE_ENGINE_ = #src/ai/narrative_engine.py  |
| Prompt Chaining     | Break tasks into sequential prompts         | Step 1: Extract facts → Step 2: Summarize → ...   |
| Modular Template    | Reusable prompt for any input/task/output   | "Given [input], perform [task] and output [format]"|
| Context Pruning     | Summarize and reduce context periodically   | After 5-10 steps, summarize and carry forward     |

---

See also: Blueprint_Prompts_and_Scripts.md for additional prompt templates and script stubs.
