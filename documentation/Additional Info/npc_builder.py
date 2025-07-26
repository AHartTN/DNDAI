import json
import random

class NPCBuilder:
    def __init__(self, config):
        self.config = config
        self.templates_path = self.config.get('npc_templates')
        self.stat_block_schema_path = self.config.get('stat_block_schema')
        self.templates = self._load_json(self.templates_path)
        self.stat_schema = self._load_json(self.stat_block_schema_path)

    def _load_json(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def build_npc(self, archetype, tags, campaign_state):
        template = self.templates.get(archetype, {"name": "Unknown", "archetype": archetype, "tags": tags})
        stat_block = {k: v for k, v in self.stat_schema.items()}
        portrait_prompt = f"fantasy portrait of {archetype} with tags {tags}"
        return {
            "npc": template,
            "stat_block": stat_block,
            "portrait_prompt": portrait_prompt
        }