# DNDAI Blueprint Auto-Expander
"""
Scans blueprints for referenced assets and generates stubs for missing files.
"""
import os
import re

BLUEPRINTS_DIR = 'Extracts/Blueprints'
ASSET_DIRS = ['Extracts/Scripts', 'Extracts/Prompts', 'Extracts/Checklists']


def find_references():
    refs = set()
    for root, _, files in os.walk(BLUEPRINTS_DIR):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        m = re.findall(r'([A-Za-z0-9_]+\.(py|md|yaml|json))', line)
                        for ref, _ in m:
                            refs.add(ref)
    return refs

def generate_stubs(refs):
    for ref in refs:
        for d in ASSET_DIRS:
            path = os.path.join(d, ref)
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(f'# Auto-generated stub for {ref}\n')

if __name__ == '__main__':
    refs = find_references()
    generate_stubs(refs)
    print('Blueprint auto-expansion complete.')
