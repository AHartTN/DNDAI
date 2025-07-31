# DNDAI Contribution Checklist Generator
"""
Auto-generates a checklist for new PRs based on documentation standards.
"""
CHECKLIST_PATH = 'src/logs/contribution_checklist.md'

CHECKLIST = [
    '- [ ] Place new work in correct directory',
    '- [ ] Archive deprecated work',
    '- [ ] Cross-reference related docs',
    '- [ ] Keep code and docs in sync',
    '- [ ] Update Unified Topics Index.md',
    '- [ ] Run all tests and validate config',
    '- [ ] Review and update blueprints/prompts/scripts as needed',
]

def write_checklist():
    with open(CHECKLIST_PATH, 'w') as f:
        f.write('# DNDAI Contribution Checklist\n\n')
        for item in CHECKLIST:
            f.write(f'{item}\n')
    print(f'Contribution checklist written to {CHECKLIST_PATH}')

if __name__ == '__main__':
    write_checklist()
