# Changelog

## [0.1.0] - 2025-07-18

- Initial workspace setup for Dungeon Master AI
- Python virtual environment created
- Installed llama-cpp-python, discord.py, twitchio
- Added README and copilot-instructions

## [0.1.1] - 2025-07-19

- Added image prompt placeholders for feudal hierarchy and genealogy diagrams
- Expanded noble-feudal-structure.md with sample NPCs/stat blocks, gameplay example, and image links
- Ensured cross-references and documentation remain in sync

## [0.1.2] - 2025-07-18

- All documentation files expanded and completed with comprehensive, genre-accurate lists, tables, examples, and cross-references
- Updated expansion notes and campaign hooks for logical cohesion and campaign utility
- README updated to reflect exhaustive documentation update

## [0.1.3] - 2025-07-18

- Added AI Implementation & Architecture documentation, outlining modular system design for Llama 4, Stable Diffusion, and bot integrations
- Updated README to reflect new AI section and modular architecture focus

## [0.1.4] - 2025-07-18

- Added AI Module API & Data Contracts documentation
- Added AI Implementation Sample Workflow documentation
- Updated next steps for modular AI system implementation

## [0.1.5] - 2025-07-18

- Added api_server.py: Flask API server for narrative engine endpoint
- Added apiClient.ts: TypeScript client for calling Python API server
- Next steps: Add endpoints for encounter, npc, item modules and expand integration

## [0.1.6] - 2025-07-18

- Implemented Llama 4 model integration in Python narrative engine (requires llama-cpp-python)
- Added prompt engineering and real model calls to generate_narrative
- Updated README with llama-cpp-python dependency note
- Next: Expand encounter, NPC, item modules and Stable Diffusion integration

## [0.1.7] - 2025-07-18

- Implemented EncounterGenerator, NPCBuilder, ItemGenerator, and StableDiffusionImageGenerator modules
- Wired up Flask API endpoints for encounter, npc, item, and image generation
- Expanded TypeScript client and bot interface for image workflow
- Added automated tests for core generators

## [0.1.8] - 2025-07-18

- Updated config.yaml and .env.example to use D:/AI/models as the root for all model files
- Created D:/AI/models directory for storing Llama and Stable Diffusion models
- Added model-download-instructions.md for secure setup and download steps
