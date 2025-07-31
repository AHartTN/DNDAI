# DNDAI NPC Stat Block Prompt Template
"""
Generate a stat block for an NPC with the following traits: [archetype], [motivation], [gear].
"""

prompt = """
You are the AI NPC Builder. Given the following NPC traits:
- Archetype: {archetype}
- Motivation: {motivation}
- Gear: {gear}

Generate a stat block including:
- Name
- Type
- Stats (STR, DEX, CON, INT, WIS, CHA)
- Skills
- Abilities
- HP, AC, Speed
- Special traits
"""

# Usage:
# npc = generate_npc(archetype, motivation, gear)
