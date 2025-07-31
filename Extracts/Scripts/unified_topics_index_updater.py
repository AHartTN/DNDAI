# DNDAI Unified Topics Index Auto-Updater
"""
Keeps Unified Topics Index.md in sync with workspace content.
"""
import os

INDEX_PATH = '_Samples/Unified Topics Index.md'


def update_index():
    topics = set()
    for root, _, files in os.walk('Extracts'):
        for file in files:
            if file.endswith('.md'):
                topics.add(file.replace('.md', ''))
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write('# Unified Topics Index\n\n')
        for t in sorted(topics):
            f.write(f'- {t}\n')
    print(f'Unified Topics Index updated: {INDEX_PATH}')

if __name__ == '__main__':
    update_index()
