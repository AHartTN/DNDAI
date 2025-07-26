
# Core System Mechanics

## Purpose

This document provides a comprehensive reference for the core mechanics that govern the AI Dungeon Master system. It details the rules, logic, and algorithms that underpin encounters, narrative progression, NPC actions, item usage, and world simulation. All mechanics are designed to be modular, extensible, and genre-accurate for D&D-style campaigns.

## System Overview

- **Turn Structure:** Defines initiative, action economy, and round resolution for both players and AI-controlled entities.
- **Skill Checks & Saving Throws:** Outlines how the AI interprets and resolves ability checks, skill rolls, and saving throws using campaign state and player/NPC stats.
- **Combat Resolution:** Describes attack, defense, damage, and special ability logic, including multi-attack, spellcasting, and legendary actions.
- **Exploration & Travel:** Rules for movement, travel time, random encounters, and environmental hazards.
- **Resource Management:** Tracks inventory, spell slots, hit points, and other consumables for both players and AI entities.
- **Narrative Hooks:** Mechanisms for introducing story events, plot twists, and dynamic world changes.

## Step-by-Step: Implementing a New Mechanic

1. **Define Mechanic Scope:** Clearly describe the rule or system to be added (e.g., morale checks, weather effects).
2. **Specify Data Inputs:** List required stats, campaign state, and any random elements.
3. **Algorithm Design:** Write out the logic in pseudocode or flowchart form.
4. **Integration Points:** Identify where the mechanic hooks into the narrative engine, encounter generator, or other modules.
5. **Testing:** Add unit and integration tests (see [Testing & Validation](testing-and-validation.md)).
6. **Documentation:** Update this file and cross-reference related modules.

## Example: Morale Check Mechanic

- **Trigger:** When an NPC or monster is reduced below 50% HP or outnumbered 2:1.
- **Input:** NPC/monster Wisdom, campaign morale modifiers, random d20 roll.
- **Logic:** If (Wisdom + modifiers + d20) < DC, the entity attempts to flee or surrender.
- **Integration:** Called by the encounter generator during combat resolution.

## Cross-References

- [AI Implementation Architecture](ai-implementation-architecture.md)
- [Module API Contracts](ai-module-api-contracts.md)
- [Creatures & Encounters](creatures-encounters.md)
- [Testing & Validation](testing-and-validation.md)

## Expansion Notes

- All mechanics are reviewed for genre accuracy and campaign consistency.
- Add new mechanics as needed for campaign-specific rules or homebrew content.
- Last reviewed: 2025-07-23.
