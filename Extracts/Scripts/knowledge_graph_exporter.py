# DNDAI Knowledge Graph Exporter
"""
Exports agent/module relationships as a Graphviz DOT file for visualization.
"""
import os

DOT_PATH = 'src/logs/knowledge_graph.dot'

MODULES = [
    'narrative_engine',
    'encounter_generator',
    'npc_builder',
    'item_generator',
    'visual_asset_pipeline',
    'bot_interface',
]

RELATIONSHIPS = [
    ('narrative_engine', 'encounter_generator'),
    ('narrative_engine', 'item_generator'),
    ('encounter_generator', 'npc_builder'),
    ('npc_builder', 'visual_asset_pipeline'),
    ('bot_interface', 'narrative_engine'),
]

def export_graph():
    with open(DOT_PATH, 'w') as f:
        f.write('digraph DNDAI {\n')
        for m in MODULES:
            f.write(f'  {m};\n')
        for src, dst in RELATIONSHIPS:
            f.write(f'  {src} -> {dst};\n')
        f.write('}\n')
    print(f'Knowledge graph exported to {DOT_PATH}')

if __name__ == '__main__':
    export_graph()
