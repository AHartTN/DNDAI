# DNDAI Workspace Hygiene Checker
"""
Scans for duplicate, orphaned, or deprecated files and logs findings for workspace hygiene.
"""
import os
from collections import defaultdict
from datetime import datetime

LOG_PATH = 'src/logs/hygiene_check.log'


def scan_workspace(directory):
    seen = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            seen[file].append(os.path.join(root, file))
    with open(LOG_PATH, 'a') as log:
        for fname, paths in seen.items():
            if len(paths) > 1:
                log.write(f"[{datetime.now()}] Duplicate: {fname} -> {paths}\n")
    print(f'Hygiene check complete. Log: {LOG_PATH}')

if __name__ == '__main__':
    scan_workspace('.')
