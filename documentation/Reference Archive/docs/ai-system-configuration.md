# AI System Configuration

## Environment Variables

- LLAMA4_MODEL_PATH: Path to Llama 4 model file
- STABLE_DIFFUSION_MODEL_PATH: Path to Stable Diffusion model file
- DISCORD_TOKEN: Discord bot token
- TWITCH_TOKEN: Twitch bot token
- CAMPAIGN_DB_PATH: Path to campaign database
- LOG_LEVEL: Logging verbosity (DEBUG, INFO, WARNING, ERROR)

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

## Configuration File Example (config.yaml)

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

## Usage

- Load environment variables from system or .env file.
- Load config.yaml at application startup for module configuration.
- Validate paths and tokens before initializing modules.

## Next Steps

- Implement config loader in Python for AI modules.
- Implement config loader in Node.js/TypeScript for bot interface.
- Add sample .env and config.yaml files to repository.
- Begin coding narrative engine and bot interface modules.

## Expansion Notes

- Configuration details are being reviewed for accuracy and completeness.
- Ensure all environment variables and config options are documented.
- Last reviewed: 2025-07-23.
