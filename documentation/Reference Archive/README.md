
# DNDAI Research Workspace

This repository is a research, planning, and documentation workspace for the upcoming Dungeon Master AI project. **No runnable code is present.**

## Directory Structure

- `research/` — All research, planning, and reference documents (see this folder for all current work)
- `archive/` — Old code stubs, prototypes, and deprecated files
- `docs/` — (If present) Additional documentation

## Guidance

- Do not expect to run any code in this workspace.
- All files are for reference, planning, or prototyping only.
- See `research/` for the latest project context and plans.
- For any command to be run in the terminal (regardless of type), you will always be prompted for explicit approval before the command is executed.

## How to Contribute

All new research, plans, and prototypes must be placed in the `research/` directory. If you are archiving old or deprecated work, move it to `archive/`.

## Note

This workspace is for research and planning only. For more information, see `research/Agent-Optimization-Research-Plan.md` and `.github/copilot-instructions.md`.

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

Each section now contains exhaustive tables, lists, campaign hooks, stat blocks, gameplay examples, and image prompt placeholders for future visual assets. All documentation is fully expanded, genre-accurate, and cross-referenced for campaign use. See `docs/` for details.

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

## Expansion Notes

- This README is kept in sync with the Table of Contents and Knowledge Aggregation log.
- All major sections are cross-referenced and up to date as of 2025-07-23.
- Review after any major documentation or architecture change.

This project uses [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) for Llama 4 model inference. Install with:

```sh
pip install llama-cpp-python
```

Ensure your model path in `config.yaml` is correct and the model file is accessible.
