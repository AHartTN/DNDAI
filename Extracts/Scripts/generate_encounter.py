import random

def generate_encounter(theme, difficulty):
    hooks = [
        "A mysterious stranger offers a quest.",
        "A sudden storm reveals a hidden ruin.",
        "A local NPC pleads for help with a threat."
    ]
    npcs = [
        {"name": "Sir Cedric", "role": "Knight", "motivation": "Honor"},
        {"name": "Mira the Wise", "role": "Sage", "motivation": "Knowledge"},
        {"name": "Thorn", "role": "Bandit", "motivation": "Greed"}
    ]
    challenges = [
        "Solve a riddle to open the gate.",
        "Defeat a group of goblins.",
        "Navigate a trapped corridor."
    ]
    rewards = [
        "A magical sword.",
        "Ancient lore.",
        "A pouch of gold."
    ]
    return {
        "hook": random.choice(hooks),
        "npc": random.choice(npcs),
        "challenge": random.choice(challenges),
        "reward": random.choice(rewards),
        "theme": theme,
        "difficulty": difficulty
    }

# Example usage:
# encounter = generate_encounter("forest", "medium")
# print(encounter)
