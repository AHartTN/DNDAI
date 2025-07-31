# DNDAI Dependency Mapper
"""
Scans code and docs for cross-file dependencies and outputs a dependency graph (DOT format).
"""
import os
import re

DOT_PATH = 'src/logs/dependency_graph.dot'


def find_dependencies(base_dir):
    deps = set()
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py') or file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        m = re.findall(r'(src/ai/\w+\.py)', line)
                        for dep in m:
                            deps.add((file, dep))
    return deps

def write_dot(deps):
    with open(DOT_PATH, 'w') as f:
        f.write('digraph Dependencies {\n')
        for src, dst in deps:
            f.write(f'  "{src}" -> "{dst}";\n')
        f.write('}\n')
    print(f'Dependency graph written to {DOT_PATH}')

if __name__ == '__main__':
    deps = find_dependencies('Extracts')
    write_dot(deps)
