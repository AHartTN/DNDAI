# DNDAI Blueprint/Prompt/Script Indexer
"""
Auto-generates a markdown index of all blueprints, prompts, and scripts in Extracts.
"""
import os

INDEX_PATH = 'src/logs/blueprint_prompt_script_index.md'


def index_files(base_dir, exts):
    index = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if any(file.endswith(ext) for ext in exts):
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                index.append(rel_path)
    return index

def write_index(index):
    with open(INDEX_PATH, 'w') as f:
        f.write('# DNDAI Blueprint/Prompt/Script Index\n\n')
        for path in sorted(index):
            f.write(f'- {path}\n')
    print(f'Index generated: {INDEX_PATH}')

if __name__ == '__main__':
    exts = ['.md', '.py', '.yaml', '.json']
    index = index_files('Extracts', exts)
    write_index(index)
