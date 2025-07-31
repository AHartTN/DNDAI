# DNDAI Prompt Pattern Extractor
"""
Scans all prompt and script files, extracts reusable prompt patterns, and logs them centrally.
"""
import os
import re

PATTERN_LOG = 'src/logs/prompt_pattern_log.md'


def extract_patterns(base_dir):
    patterns = set()
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py') or file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if 'prompt' in line.lower() or 'template' in line.lower():
                            patterns.add(line.strip())
    return patterns

def write_patterns(patterns):
    with open(PATTERN_LOG, 'w', encoding='utf-8') as f:
        f.write('# DNDAI Prompt Pattern Log\n\n')
        for p in sorted(patterns):
            f.write(f'- {p}\n')
    print(f'Prompt patterns written to {PATTERN_LOG}')

if __name__ == '__main__':
    patterns = extract_patterns('Extracts')
    write_patterns(patterns)
