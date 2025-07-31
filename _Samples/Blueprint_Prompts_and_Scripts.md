# Prompts & Scripts Blueprint

## Campaign Prompts

- **Campaign Generation Prompt:**
  - "Generate a new campaign setting with the following parameters: [genre], [theme], [party level], [region]. Output a summary, key factions, and campaign hooks."
- **Worldbuilding Prompt:**
  - "Expand the lore for [region] including history, major NPCs, and current conflicts."
- **Modular Narrative Prompt:**
  - "Given the current campaign state, generate the next narrative event and DM notes."

## Encounter & Asset Prompts

- **Encounter Resolution Prompt:**
  - "Given the party's actions and current terrain, generate a balanced encounter with stat blocks and loot."
- **Image Asset Prompt:**
  - "Create a Stable Diffusion prompt for an NPC portrait: [description, style, mood]."
- **NPC Stat Block Prompt:**
  - "Generate a stat block for an NPC with the following traits: [archetype], [motivation], [gear]."

## Modular Script Stubs

- **Campaign Start Script:**
  - Input: campaign parameters
  - Steps: generate setting → create initial NPCs → generate first encounter → output summary
- **Encounter Script:**
  - Input: player action, terrain
  - Steps: generate encounter → create stat blocks → generate loot → output encounter details
- **Asset Generation Script:**
  - Input: prompt, style guide
  - Steps: generate image → return URL/metadata

## Instruction Templates

- **Context Management Instruction:**
  - "Always use symbolic references for files and modules. Summarize context every 5-10 steps."
- **Transparency Instruction:**
  - "For every major action, provide a brief explanation of reasoning."
- **User Adaptation Instruction:**
  - "Detect and adapt to user-preferred interaction patterns (AI-first, request-driven, etc.)."
- **Human-in-the-Loop Validation:**
  - "After each automated analysis, prompt for human review and correction."
- **Feedback Mechanism:**
  - "Provide a way for users to flag errors or request clarification at any step."

---

See also: Blueprint_Agent_Optimization_and_Prompt_Engineering.md for prompt chaining and symbolic reference techniques.
