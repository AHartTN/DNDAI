# File Review Log: ai-module-api-contracts.md

## Actionable Extracts & Operational Logic

### 1. API Endpoints & Data Contracts
- **Narrative Engine:** `/api/narrative` (context, player_actions, campaign_state) → narrative, next_hooks, dm_notes. Config: model path, prompt templates, context window.
- **Encounter Generator:** `/api/encounter` (party_level, terrain, campaign_state) → encounter, balance_rating, loot. Config: templates, monster DB.
- **NPC & Creature Builder:** `/api/npc` (archetype, tags, campaign_state) → npc, stat_block, portrait_prompt. Config: templates, stat schema.
- **Item & Artifact Generator:** `/api/item` (rarity, type, campaign_state) → item, lore, image_prompt. Config: item DB, templates.
- **Visual Asset Pipeline:** `/api/image` (prompt, style, output_type) → image_url, metadata. Config: model path, style guides.
- **Bot Interface:** `/api/bot` (user_input, session_id, campaign_state) → response, actions. Config: tokens, session timeout.

### 2. Shared Configuration
- Environment variables for model paths, tokens, campaign DB, log level.

### 3. Implementation Steps
- Implement config files and env var management.
- Create sample API handlers and test cases for each module.
- Document integration workflow (Python AI <-> Node.js bot).
- Begin coding narrative engine and bot interface.
- Implemented core generators, Flask API endpoints, expanded TypeScript client, automated tests.

## Operational Logic
- Modular, API-driven contracts for all core AI modules.
- Clear input/output, config, and extensibility for each module.
- Environment-driven configuration for deployment and integration.

---

**End of File Review Log: ai-module-api-contracts.md**
