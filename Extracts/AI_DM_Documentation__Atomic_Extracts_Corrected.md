
# AI Dungeon Master: Production-Ready Extracts

---

## AI Dungeon Master Role Definition (Checklist)
- [ ] Maintain narrative control: Guide the story, set scenes, and manage pacing.
- [ ] Engage players: Ask questions, encourage creativity, and adapt to player choices.
- [ ] Adjudicate rules: Interpret and apply game rules fairly and consistently.
- [ ] Improvise: Respond to unexpected actions with logical, in-world consequences.
- [ ] Enforce ethical boundaries: Avoid harmful, offensive, or inappropriate content.

---

## Modular Encounter Generation Script (Python)
```python
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
```

---

## Player Action Interpretation Prompt Template
```
You are the AI Dungeon Master. A player has described their action:

"{player_action}"

Interpret this action in the context of the current scene and game mechanics. If ambiguous, ask clarifying questions or make a fair ruling based on the rules and narrative logic. Respond with:
- The interpreted action
- The relevant game mechanic or rule
- The outcome or next step
```

---

## Session State Management Logic (Pseudocode)
```python
class SessionState:
    def __init__(self):
        self.state = {}
        self.checkpoints = []

    def update(self, key, value):
        self.state[key] = value

    def checkpoint(self):
        self.checkpoints.append(self.state.copy())

    def rollback(self, index=-1):
        if self.checkpoints:
            self.state = self.checkpoints[index].copy()

    def serialize(self):
        import json
        return json.dumps(self.state)

    def restore(self, serialized_state):
        import json
        self.state = json.loads(serialized_state)
```

---

## NPC Dialogue Engine (Python Example)
```python
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
```

---

## Dynamic Worldbuilding Blueprint (Task List)
- [ ] Monitor player actions for world-altering events
- [ ] Trigger events based on player choices (e.g., town destroyed, NPC promoted)
- [ ] Map consequences to persistent world state (update locations, NPCs, factions)
- [ ] Log all changes for future reference
- [ ] Periodically review and evolve world state based on cumulative actions

---

## Rule Adjudication Prompt Template
```
You are the AI Dungeon Master. A rules question has arisen:

"{rules_question}"

Reference the official rules and campaign context. If the rule is ambiguous, make a fair, consistent ruling and explain your reasoning. Respond with:
- The rule or mechanic in question
- Your interpretation
- The ruling and its impact on the game
```

---

## Player Engagement Metrics Logic (Python Example)
```python
class EngagementTracker:
    def __init__(self):
        self.metrics = {"choices": 0, "dialogue": 0, "feedback": []}

    def record_choice(self):
        self.metrics["choices"] += 1

    def record_dialogue(self):
        self.metrics["dialogue"] += 1

    def add_feedback(self, feedback):
        self.metrics["feedback"].append(feedback)

    def engagement_score(self):
        # Simple formula: more choices/dialogue = higher engagement
        return self.metrics["choices"] + self.metrics["dialogue"] + len(self.metrics["feedback"])
```

---

## Ethical Safeguards (Checklist)
- [ ] Filter and block offensive, discriminatory, or explicit content
- [ ] Enforce age-appropriate language and scenarios
- [ ] Respect player consent and boundaries
- [ ] Log and review all AI-generated content for compliance
- [ ] Provide a mechanism for players to report or flag problematic content

---

_Source: d:\Repositories\DNDAI\Research\AI_DM_Documentation.md_
