# File Review Log: Blueprint_Agent_Optimization_and_Prompt_Engineering.md

## Actionable Extracts & Operational Logic

### 1. Token Efficiency
- Use symbolic references for files/modules/tasks (e.g., _NARRATIVE_ENGINE_ = #src/ai/narrative_engine.py).
- Define all symbols at session start or in a master file.
- Apply chain-of-symbol (CoS) paradigm for relationships (e.g., _NARRATIVE_ENGINE_ -> _ENCOUNTER_GEN_).
- Implement prompt chaining for multi-step tasks (extract facts → synthesize summary → generate output).

### 2. Context Management
- Use @workspace for broad, #file for focused context in prompts.
- Maintain symbolic linking system for critical files; list symbols/paths at top of prompts/docs.
- Regularly prune/summarize context to avoid "lost in the middle" (summarize every 5-10 steps, carry forward only essentials).

### 3. Long-Context Strategies
- Break long tasks into discrete, sequential prompts (requirements → architecture → stubs).
- Use output of one step as input for the next; archive/reference outputs symbolically (e.g., _REQS_, _ARCH_, _STUBS_).

### 4. Modular Prompt Design
- Design prompts to be reusable/composable ("Given [input], perform [task] and output [format]").
- Use templates for common tasks (summarization, code/test generation, analysis).
- Document all prompt patterns and update as new techniques are developed (maintain a prompt pattern log).

### 5. Prompt Pattern Log
- Maintain a running log of all prompt patterns/templates/techniques.
- Sample log table provided (symbolic reference, prompt chaining, modular template, context pruning).

## Operational Logic
- Symbolic, modular, and context-aware prompt engineering for agent optimization.
- Chain-of-symbols, prompt chaining, and context pruning are core strategies.
- All patterns and templates are documented and iteratively improved.

---

**End of File Review Log: Blueprint_Agent_Optimization_and_Prompt_Engineering.md**
