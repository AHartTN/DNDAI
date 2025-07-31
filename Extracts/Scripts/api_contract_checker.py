# DNDAI API Contract Checker
"""
Validates OpenAPI schema against implemented endpoints (stub).
"""
import yaml

API_SCHEMA = 'Extracts/Scripts/dndai_api_schema.yaml'
IMPLEMENTED_ENDPOINTS = [
    '/api/narrative',
    '/api/encounter',
    '/api/npc',
    '/api/item',
    '/api/image',
]

def check_contract():
    with open(API_SCHEMA, 'r') as f:
        schema = yaml.safe_load(f)
    paths = schema.get('paths', {})
    missing = [ep for ep in IMPLEMENTED_ENDPOINTS if ep not in paths]
    if missing:
        print(f'Missing endpoints in schema: {missing}')
    else:
        print('All endpoints present in schema.')

if __name__ == '__main__':
    check_contract()
