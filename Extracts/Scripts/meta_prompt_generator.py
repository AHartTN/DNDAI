# DNDAI Meta-Prompt Generator
"""
Creates new prompt templates from blueprint/process patterns.
"""
import os
import re

PROMPT_DIR = 'Extracts/Prompts'
META_PROMPT_PATH = 'src/logs/meta_prompts.md'


def generate_meta_prompts():
    patterns = set()
    for root, _, files in os.walk(PROMPT_DIR):
        for file in files:
            if file.endswith('.py') or file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if 'prompt' in line.lower() or 'template' in line.lower():
                            patterns.add(line.strip())
    with open(META_PROMPT_PATH, 'w', encoding='utf-8') as f:
        f.write('# DNDAI Meta-Prompts\n\n')
        for p in sorted(patterns):
            f.write(f'- {p}\n')
    print(f'Meta-prompts written to {META_PROMPT_PATH}')

if __name__ == '__main__':
    generate_meta_prompts()
