# Project Scaffolding Script for Agent Orchestration

import os

folders = [
    'Extracts/Prompts',
    'Extracts/Scripts',
    'Extracts/Checklists',
    'Extracts/Blueprints'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Project scaffolding complete. All required directories created.")
