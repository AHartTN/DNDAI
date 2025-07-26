import json
import random

class EncounterGenerator:
    def __init__(self, config):
        self.config = config
        self.templates_path = self.config.get('encounter_templates')
        self.monster_db_path = self.config.get('monster_db_path')
        self.templates = self._load_json(self.templates_path)
        self.monsters = self._load_json(self.monster_db_path)

    def _load_json(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def generate_encounter(self, party_level, terrain, campaign_state):
        # Select template and monsters based on terrain and party level
        template = self.templates.get(terrain, {"description": "A generic encounter."})
        possible_monsters = [m for m in self.monsters if m.get('terrain') == terrain and m.get('level', 1) <= party_level]
        selected = random.sample(possible_monsters, min(2, len(possible_monsters))) if possible_monsters else []
        loot = ["gold", "short sword"]
        return {
            "encounter": {"monsters": [m['name'] for m in selected], "terrain": terrain, "description": template.get('description')},
            "balance_rating": "balanced" if selected else "easy",
            "loot": loot
        }