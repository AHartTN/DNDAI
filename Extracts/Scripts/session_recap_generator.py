# DNDAI Session Recap Generator
"""
Auto-generates a session recap from campaign logs.
"""
import os

LOG_PATH = 'src/logs/session.log'
RECAP_PATH = 'src/logs/session_recap.md'


def generate_recap():
    if not os.path.exists(LOG_PATH):
        print('No session log found.')
        return
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    recap = lines[-10:] if len(lines) > 10 else lines
    with open(RECAP_PATH, 'w', encoding='utf-8') as f:
        f.write('# Session Recap\n\n')
        for line in recap:
            f.write(f'- {line.strip()}\n')
    print(f'Session recap written to {RECAP_PATH}')

if __name__ == '__main__':
    generate_recap()
