import os
import yaml

class Config:
    def __init__(self, config_path='config.yaml'):
        self.env = {
            'LLAMA4_MODEL_PATH': os.getenv('LLAMA4_MODEL_PATH'),
            'STABLE_DIFFUSION_MODEL_PATH': os.getenv('STABLE_DIFFUSION_MODEL_PATH'),
            'DISCORD_TOKEN': os.getenv('DISCORD_TOKEN'),
            'TWITCH_TOKEN': os.getenv('TWITCH_TOKEN'),
            'CAMPAIGN_DB_PATH': os.getenv('CAMPAIGN_DB_PATH'),
            'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
        }
        with open(config_path, 'r') as f:
            self.yaml = yaml.safe_load(f)

    def get(self, key):
        return self.env.get(key) or self.yaml.get(key)

    def all(self):
        merged = self.yaml.copy()
        merged.update({k: v for k, v in self.env.items() if v is not None})
        return merged

# Usage example:
# config = Config()
# llama_path = config.get('llama4_model_path')
# print(config.all())
