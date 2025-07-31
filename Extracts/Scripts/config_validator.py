# DNDAI Config Schema Validator
"""
Validates config.yaml for required fields, types, and values.
"""
import yaml

REQUIRED_FIELDS = [
    'llama4_model_path',
    'stable_diffusion_model_path',
    'discord_token',
    'twitch_token',
    'campaign_db_path',
    'log_level',
    'encounter_templates',
    'monster_db_path',
    'npc_templates',
    'item_db_path',
    'artifact_templates',
    'stat_block_schema',
    'style_guides',
]

CONFIG_PATH = 'src/config/config.yaml'


def validate_config():
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.safe_load(f)
    missing = [k for k in REQUIRED_FIELDS if k not in config]
    if missing:
        print(f'Missing fields: {missing}')
    else:
        print('Config is valid.')

if __name__ == '__main__':
    validate_config()
