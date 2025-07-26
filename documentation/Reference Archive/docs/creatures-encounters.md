
# Creatures & Encounters

## Purpose

This document details the design, generation, and management of creatures and encounters within the AI Dungeon Master system. It provides guidelines for creating balanced, engaging, and genre-accurate encounters, as well as instructions for integrating new creature types and encounter templates.

## Encounter Design Workflow

1. **Define Encounter Type:** Combat, social, exploration, puzzle, or mixed.
2. **Select/Generate Creatures:** Use [NPC Character Templates](npc-character-templates.md) and campaign-specific monster lists.
3. **Set Difficulty:** Adjust creature stats, numbers, and environment for party level and resources.
4. **Add Narrative Hooks:** Tie encounters to ongoing storylines, world events, or player goals.
5. **Integrate Environmental Factors:** Terrain, hazards, magical effects, and weather.
6. **Test & Validate:** Simulate encounter outcomes and adjust for balance (see [Testing & Validation](testing-and-validation.md)).

## Creature Generation

- **Stat Blocks:** Use templates from [NPC Character Templates](npc-character-templates.md) and [Noble & Feudal Structure](noble-feudal-structure.md) for humanoids.
- **Special Abilities:** Assign unique traits, spells, or actions based on lore and campaign needs.
- **Image Prompts:** Generate visual assets using [Visual Asset Pipeline](ai-module-api-contracts.md#visual-asset-pipeline-stable-diffusion).

## Encounter Templates

- **Random Encounter Tables:** Weighted lists by region, time, and campaign state.
- **Boss Encounters:** Multi-phase, narrative-driven, and with unique mechanics.
- **Social Encounters:** Dialogue trees, negotiation, and intrigue.

## Cross-References

- [Core System Mechanics](core-system-mechanics.md)
- [AI Implementation Architecture](ai-implementation-architecture.md)
- [Module API Contracts](ai-module-api-contracts.md)
- [Timeline & World History](timeline-world-history.md)

## Expansion Notes

- All encounter templates and creature lists are reviewed for balance and campaign fit.
- Add new templates for campaign-specific or homebrew content.
- Last reviewed: 2025-07-23.
