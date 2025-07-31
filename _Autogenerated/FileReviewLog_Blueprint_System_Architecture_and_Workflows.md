# File Review Log: Blueprint_System_Architecture_and_Workflows.md

## Actionable Extracts & Operational Logic

### 1. Modular AI Architecture
- Modules: Narrative engine (Llama 4), encounter generator, NPC builder, item generator, visual asset pipeline (Stable Diffusion), bot interface (Node.js/TypeScript).

### 2. API/Data Contracts
- Narrative: `/api/narrative` (context, player_actions, campaign_state) → narrative, next_hooks, dm_notes.
- Encounter: `/api/encounter` (party_level, terrain, campaign_state) → encounter, balance_rating, loot.
- NPC: `/api/npc` (archetype, tags, campaign_state) → npc, stat_block, portrait_prompt.
- Item: `/api/item` (rarity, type, campaign_state) → item, lore, image_prompt.
- Visual asset: `/api/image` (prompt, style_guide) → image_url, metadata.

### 3. Configuration Management
- Use env vars and config.yaml for all modules.
- Validate paths, tokens, resources at startup.
- Provide sample config files and documentation.

### 4. Sample Workflows
- Campaign generation: user input → bot → narrative → encounter → NPC → item → visual asset → bot → players.
- Encounter resolution: player action → bot → encounter → NPC → visual asset → bot → campaign update.
- Image asset creation: narrative/item → visual asset → bot → players/records.

## Operational Logic
- Modular, API-driven, and config-managed architecture for D&D AI system.
- Clear workflows for campaign, encounter, and asset generation.
- All modules are testable, extensible, and documented.

---

**End of File Review Log: Blueprint_System_Architecture_and_Workflows.md**
