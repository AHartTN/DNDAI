import json
import random

class ItemGenerator:
    def __init__(self, config):
        self.config = config
        self.item_db_path = self.config.get('item_db_path')
        self.artifact_templates_path = self.config.get('artifact_templates')
        self.items = self._load_json(self.item_db_path)
        self.artifacts = self._load_json(self.artifact_templates_path)

    def _load_json(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def generate_item(self, rarity, type_, campaign_state):
        item = next((i for i in self.items if i.get('type') == type_ and i.get('rarity') == rarity), None)
        if not item:
            item = {"name": f"{rarity.title()} {type_.title()}", "type": type_, "rarity": rarity}
        lore = self.artifacts.get(type_, "Forged in the first light of the new age.")
        image_prompt = f"ornate {rarity} {type_}"
        return {
            "item": item,
            "lore": lore,
            "image_prompt": image_prompt
        }