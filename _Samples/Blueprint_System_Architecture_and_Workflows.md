# System Architecture & Workflows Blueprint

## Modular AI Architecture

- Narrative engine (Llama 4)
- Encounter generator
- NPC builder
- Item generator
- Visual asset pipeline (Stable Diffusion)
- Bot interface (Node.js/TypeScript)

## API/Data Contracts

- **Narrative Engine**
  - Endpoint: `/api/narrative`
  - Input: `{ context: string, player_actions: array, campaign_state: object }`
  - Output: `{ narrative: string, next_hooks: array, dm_notes: string }`
- **Encounter Generator**
  - Endpoint: `/api/encounter`
  - Input: `{ party_level: int, terrain: string, campaign_state: object }`
  - Output: `{ encounter: object, balance_rating: string, loot: array }`
- **NPC Builder**
  - Endpoint: `/api/npc`
  - Input: `{ archetype: string, tags: array, campaign_state: object }`
  - Output: `{ npc: object, stat_block: object, portrait_prompt: string }`
- **Item Generator**
  - Endpoint: `/api/item`
  - Input: `{ rarity: string, type: string, campaign_state: object }`
  - Output: `{ item: object, lore: string, image_prompt: string }`
- **Visual Asset Pipeline**
  - Endpoint: `/api/image`
  - Input: `{ prompt: string, style_guide: string }`
  - Output: `{ image_url: string, metadata: object }`

## Configuration Management

- Use environment variables and config.yaml for all modules
- Validate paths, tokens, and resources at startup
- Provide sample config files and documentation

**Sample config.yaml:**
```yaml
llama4_model_path: "C:/ai/models/llama4.bin"
stable_diffusion_model_path: "C:/ai/models/stable-diffusion-v1-5"
discord_token: "YOUR_DISCORD_TOKEN"
twitch_token: "YOUR_TWITCH_TOKEN"
campaign_db_path: "e:/Repositories/DNDAI/data/campaigns.db"
log_level: "INFO"
encounter_templates: "e:/Repositories/DNDAI/data/encounter_templates.json"
monster_db_path: "e:/Repositories/DNDAI/data/monsters.json"
npc_templates: "e:/Repositories/DNDAI/data/npc_templates.json"
item_db_path: "e:/Repositories/DNDAI/data/items.json"
artifact_templates: "e:/Repositories/DNDAI/data/artifacts.json"
stat_block_schema: "e:/Repositories/DNDAI/data/stat_block_schema.json"
style_guides: "e:/Repositories/DNDAI/data/style_guides.json"
```

## Sample Workflows

**Campaign Generation:**
1. User input (campaign start, player action) → Bot interface
2. Bot interface → Narrative engine (context, player actions)
3. Narrative engine → Story, DM notes, next hooks
4. Encounter generator → Encounters
5. NPC builder → Stat blocks, portraits
6. Item generator → Loot, lore
7. Visual asset pipeline → Images
8. Bot interface → Players (narrative, images, updates)

**Encounter Resolution:**
1. Player action → Bot interface
2. Bot interface → Encounter generator
3. Encounter generator → Encounter details, loot
4. NPC builder → Stat blocks, portraits
5. Visual asset pipeline → Images
6. Bot interface → Campaign state update

**Image Asset Creation:**
1. Narrative engine/item generator → Image prompt
2. Visual asset pipeline → Image
3. Bot interface → Players, campaign records

---

See also: Blueprint_Worldbuilding_and_Game_Mechanics.md for worldbuilding data structures.
