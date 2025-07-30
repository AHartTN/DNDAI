# AI Implementation & Architecture

## Overview
This document describes the modular architecture for the Dungeon Master AI system, focusing on Llama 4 for narrative/game logic and Stable Diffusion for image generation. It outlines the separation of concerns, integration points, and extensibility for future modules.

## Core Modules
- **Narrative Engine (Llama 4):** Handles story generation, rules adjudication, campaign hooks, NPC dialogue, and world-building. Python-based, with prompt engineering and context management.
- **Encounter Generator:** Uses Llama 4 to create balanced encounters, terrain, monsters, and boss mechanics. Integrates with campaign state and player actions.
- **NPC & Creature Builder:** Generates stat blocks, motivations, relationships, gear, and quirks for NPCs and monsters. Supports custom archetypes and campaign-specific templates.
- **Item & Artifact Generator:** Produces magic items, artifacts, crafting recipes, and lore hooks. Ensures genre-appropriate rarity, properties, and attunement rules.
- **Visual Asset Pipeline (Stable Diffusion):** Generates NPC portraits, maps, artifacts, and other visual assets. Accepts prompts from narrative engine and campaign modules. Python-based, with API integration and output management.
- **Bot Interface (Node.js/TypeScript):** Connects AI modules to Discord and Twitch. Handles user input, session management, and real-time campaign updates.

## Integration & Data Flow
- API endpoints for each module, with clear input/output contracts.
- Shared context/state management for campaign progression, player actions, and world events.
- Asynchronous communication between Python AI logic and Node.js bot interface.
- Extensible design for adding new modules (e.g., map generator, lore database, player dashboard).

## Model Configuration & Prompt Engineering
- Llama 4: Custom system prompts, context windows, memory management, and role-based instructions.
- Stable Diffusion: Prompt templates for genre-accurate images, style guides, and asset post-processing.

## Extensibility Guidelines
- All modules should be independently testable and replaceable.
- Documentation for API, data formats, and integration points.
- Support for future model upgrades and new AI capabilities.

## Next Steps
- Document API endpoints and data contracts for each module.
- Define configuration files and environment variables for model selection and resource management.
- Create sample workflows for campaign generation, encounter resolution, and image asset creation.
- Begin implementation of core modules, starting with the narrative engine and bot interface.

## Recent Changes

- Implemented Llama 4 model integration in Python narrative engine (requires llama-cpp-python)
- Updated README and inline comments for new model logic
- Implemented EncounterGenerator, NPCBuilder, ItemGenerator, and StableDiffusionImageGenerator modules
- Wired up Flask API endpoints for encounter, npc, item, and image generation
- Expanded TypeScript client and bot interface for image workflow
- Added automated tests for core generators
- Updated config.yaml and .env.example to use D:/AI/models as the root for all model files
- Created D:/AI/models directory for storing Llama and Stable Diffusion models
- Added model-download-instructions.md for secure setup and download steps
