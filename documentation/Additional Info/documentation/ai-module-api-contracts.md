# AI Module API & Data Contracts

## Overview
Defines API endpoints, data contracts, and configuration for each core module in the Dungeon Master AI system. Ensures modularity, testability, and extensibility for Llama 4, Stable Diffusion, and bot integrations.

## Narrative Engine (Llama 4)
- **Endpoint:** /api/narrative
- **Input:** {
    "context": string,
    "player_actions": array,
    "campaign_state": object
  }
- **Output:** {
    "narrative": string,
    "next_hooks": array,
    "dm_notes": string
  }
- **Config:** llama4_model_path, prompt_templates, context_window_size

## Encounter Generator
- **Endpoint:** /api/encounter
- **Input:** {
    "party_level": int,
    "terrain": string,
    "campaign_state": object
  }
- **Output:** {
    "encounter": object,
    "balance_rating": string,
    "loot": array
  }
- **Config:** encounter_templates, monster_db_path

## NPC & Creature Builder
- **Endpoint:** /api/npc
- **Input:** {
    "archetype": string,
    "tags": array,
    "campaign_state": object
  }
- **Output:** {
    "npc": object,
    "stat_block": object,
    "portrait_prompt": string
  }
- **Config:** npc_templates, stat_block_schema

## Item & Artifact Generator
- **Endpoint:** /api/item
- **Input:** {
    "rarity": string,
    "type": string,
    "campaign_state": object
  }
- **Output:** {
    "item": object,
    "lore": string,
    "image_prompt": string
  }
- **Config:** item_db_path, artifact_templates

## Visual Asset Pipeline (Stable Diffusion)
- **Endpoint:** /api/image
- **Input:** {
    "prompt": string,
    "style": string,
    "output_type": string
  }
- **Output:** {
    "image_url": string,
    "metadata": object
  }
- **Config:** stable_diffusion_model_path, style_guides

## Bot Interface (Discord/Twitch)
- **Endpoint:** /api/bot
- **Input:** {
    "user_input": string,
    "session_id": string,
    "campaign_state": object
  }
- **Output:** {
    "response": string,
    "actions": array
  }
- **Config:** discord_token, twitch_token, session_timeout

## Shared Configuration
- **Environment Variables:**
    - LLAMA4_MODEL_PATH
    - STABLE_DIFFUSION_MODEL_PATH
    - DISCORD_TOKEN
    - TWITCH_TOKEN
    - CAMPAIGN_DB_PATH
    - LOG_LEVEL

## Next Steps
- Implement configuration files and environment variable management.
- Create sample API handlers and test cases for each module.
- Document integration workflow between Python AI logic and Node.js bot interface.
- Begin coding the narrative engine and bot interface modules.
- Implemented EncounterGenerator, NPCBuilder, ItemGenerator, and StableDiffusionImageGenerator modules
- Wired up Flask API endpoints for encounter, npc, item, and image generation
- Expanded TypeScript client and bot interface for image workflow
- Added automated tests for core generators
