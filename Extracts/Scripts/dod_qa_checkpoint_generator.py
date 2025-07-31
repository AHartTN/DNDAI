# DNDAI DoD/QA Checkpoint Generator
"""
Auto-creates machine-readable Definition of Done and QA checklists for each file/process.
"""
import os

CHECKPOINTS_PATH = 'src/logs/dod_qa_checkpoints.md'

CHECKPOINTS = [
    '- [ ] File reviewed',
    '- [ ] Actionable content extracted',
    '- [ ] Blueprint/process cross-referenced',
    '- [ ] Test stub present',
    '- [ ] Logging enabled',
    '- [ ] QA/DoD checklist updated',
]

def write_checkpoints():
    with open(CHECKPOINTS_PATH, 'w') as f:
        f.write('# DNDAI DoD/QA Checkpoints\n\n')
        for item in CHECKPOINTS:
            f.write(f'{item}\n')
    print(f'DoD/QA checkpoints written to {CHECKPOINTS_PATH}')

if __name__ == '__main__':
    write_checkpoints()
