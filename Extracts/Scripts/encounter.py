# DNDAI Encounter Script (Python)
"""
Script to generate an encounter: takes player action and terrain, outputs encounter details, stat blocks, and loot.
"""
def generate_encounter(player_action, terrain):
    # Step 1: Generate encounter details
    encounter = {
        'terrain': terrain,
        'challenge': 'Defeat a group of goblins',
        'stat_blocks': [
            {'name': 'Goblin', 'hp': 7, 'ac': 15, 'abilities': ['Nimble Escape']}
        ],
        'loot': ['A pouch of gold', 'Ancient lore']
    }
    # Step 2: Output encounter details
    return encounter

# Example usage:
# result = generate_encounter('attack', 'forest')
# print(result)
