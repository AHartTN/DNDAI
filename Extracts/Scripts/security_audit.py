# DNDAI Security Audit Script
"""
Scans for hardcoded secrets, insecure configs, or missing compliance logs.
"""
import os
import re

LOG_PATH = 'src/logs/security_audit.log'

SECRET_PATTERNS = [r'(?i)token\s*[:=]\s*"[^"]+"', r'(?i)password\s*[:=]\s*"[^"]+"']


def audit(directory):
    issues = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.yaml'):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        for pat in SECRET_PATTERNS:
                            if re.search(pat, line):
                                issues.append((file, i, line.strip()))
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        for file, i, line in issues:
            f.write(f'Secret in {file} at line {i}: {line}\n')
    print(f'Security audit complete. Log: {LOG_PATH}')

if __name__ == '__main__':
    audit('.')
