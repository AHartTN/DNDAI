# DNDAI Campaign Start Script (Python)
"""
Script to initialize a new campaign: generates setting, initial NPCs, first encounter, and outputs summary.
"""
def campaign_start(params):
    # Step 1: Generate campaign setting
    setting = generate_setting(params)
    # Step 2: Create initial NPCs
    npcs = generate_npcs(setting)
    # Step 3: Generate first encounter
    encounter = generate_encounter(setting, npcs)
    # Step 4: Output summary
    return {
        'setting': setting,
        'npcs': npcs,
        'encounter': encounter
    }

def generate_setting(params):
    # Stub: Replace with actual logic
    return {'region': params.get('region', 'Ashvale'), 'theme': params.get('theme', 'classic fantasy')}

def generate_npcs(setting):
    # Stub: Replace with actual logic
    return [{'name': 'Sir Cedric', 'role': 'Knight'}, {'name': 'Mira the Wise', 'role': 'Sage'}]

def generate_encounter(setting, npcs):
    # Stub: Replace with actual logic
    return {'hook': 'A mysterious stranger offers a quest.', 'npc': npcs[0], 'challenge': 'Solve a riddle', 'reward': 'A magical sword.'}

# Example usage:
# result = campaign_start({'region': 'Ashvale', 'theme': 'dark fantasy'})
# print(result)
