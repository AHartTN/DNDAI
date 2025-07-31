def generate_npc_dialogue(npc, player_input, world_state):
    # Simple context-aware dialogue generator
    if "help" in player_input.lower():
        return f"{npc['name']} says: 'I can offer guidance, but beware the dangers ahead.'"
    elif "threat" in world_state:
        return f"{npc['name']} warns: 'The {world_state['threat']} is near. Stay alert.'"
    else:
        return f"{npc['name']} says: 'What brings you here, adventurer?'"

# Example usage:
# npc = {"name": "Mira the Wise"}
# player_input = "Can you help us?"
# world_state = {"threat": "goblins"}
# print(generate_npc_dialogue(npc, player_input, world_state))
