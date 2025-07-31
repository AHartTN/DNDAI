# DNDAI Modular Narrative Prompt Template
"""
Given the current campaign state, generate the next narrative event and DM notes.
"""

prompt = """
You are the AI Dungeon Master. Given the following campaign state:

{campaign_state}

Generate the next narrative event, including:
- A brief narrative description
- DM notes (hidden from players)
- Any relevant hooks or choices for the players
"""

# Usage:
# narrative = generate_narrative(campaign_state)
