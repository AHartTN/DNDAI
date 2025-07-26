# Dungeon Master AI Workspace

This project enables a Dungeon Master AI powered by Llama 4 models (Meta) to interact with Discord and Twitch, controlling all aspects of Dungeons & Dragons gameplay, including world creation, combat, and narrative. 

## Features
- AI-driven Dungeon Master using Llama 4 models
- Discord and Twitch bot integration
- Extensible architecture for future upgrades
- Cross-platform support

## Setup
1. Python virtual environment is created in `.venv`.
2. Core dependencies installed: `llama-cpp-python`, `discord.py`, `twitchio`.
3. Node.js/TypeScript bot scaffolding to be added next.

## Next Steps
- Implement Discord and Twitch bot logic
- Integrate Llama 4 model for AI-driven gameplay
- Add environment configuration and extensibility

## Documentation
All code and documentation are kept in sync. See `.github/copilot-instructions.md` for workspace coding guidelines.

## Knowledge Base Structure
Documentation is modular and cross-referenced. Major sections include:
- Noble & Feudal Structure (with image prompt placeholders for diagrams)
- Economy & Trade
- Magic System
- NPC & Character Templates
- Creatures & Encounters
- Dungeons & Sites
- Timeline & World History
- DM Reference & Style Guide
- Appendices
- Core System Mechanics
- AI Implementation & Architecture (new)

Each section now contains exhaustive tables, lists, campaign hooks, stat blocks, gameplay examples, and image prompt placeholders for future visual assets. All documentation is fully expanded, genre-accurate, and cross-referenced for campaign use. See `documentation/` for details.

## AI Implementation & Architecture
- Modular system design for Dungeon Master AI using Llama 4 for narrative, rules, and campaign logic.
- Stable Diffusion for image generation (NPC portraits, maps, artifacts, etc.).
- Python for AI/model logic, Node.js/TypeScript for Discord/Twitch bot integrations.
- Clear separation of modules: narrative engine, encounter generator, NPC/creature builder, item/artifact generator, visual asset pipeline, bot interface.
- Documentation to include API references, data flow diagrams, model configuration, prompt engineering, and extensibility guidelines.

## Recent Changes
- All documentation files expanded and completed with comprehensive, genre-accurate lists, tables, examples, and cross-references
- Updated expansion notes and campaign hooks for logical cohesion and campaign utility
- README updated to reflect new AI Implementation & Architecture section
- Llama 4 model integration requires llama-cpp-python. Add install instructions to README and CHANGELOG.
- Implemented EncounterGenerator, NPCBuilder, ItemGenerator, and StableDiffusionImageGenerator modules
- Wired up Flask API endpoints for encounter, npc, item, and image generation
- Expanded TypeScript client and bot interface for image workflow
- Added automated tests for core generators
- Updated config.yaml and .env.example to use D:/AI/models as the root for all model files
- Created D:/AI/models directory for storing Llama and Stable Diffusion models
- Added model-download-instructions.md for secure setup and download steps

## Llama 4 model integration

This project uses [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) for Llama 4 model inference. Install with:

```sh
pip install llama-cpp-python
```

Ensure your model path in `config.yaml` is correct and the model file is accessible.
