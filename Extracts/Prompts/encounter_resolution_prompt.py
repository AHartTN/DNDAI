# DNDAI Encounter Resolution Prompt Template
"""
Given the party's actions and current terrain, generate a balanced encounter with stat blocks and loot.
"""

prompt = """
You are the AI Encounter Generator. Given the following:
- Party actions: {party_actions}
- Terrain: {terrain}

Generate:
- Encounter details
- Stat blocks for all enemies
- Loot table for the encounter
"""

# Usage:
# encounter = generate_encounter(party_actions, terrain)
