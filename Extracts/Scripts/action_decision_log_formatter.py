# DNDAI Action/Decision Log Auto-Formatter
"""
Ensures all logs are timestamped, structured, and cross-referenced.
"""
import os
from datetime import datetime

LOG_PATH = 'src/logs/action_decision.log'


def log_action(action, decision, reference=None):
    with open(LOG_PATH, 'a') as f:
        ts = datetime.now().isoformat()
        f.write(f'[{ts}] ACTION: {action} | DECISION: {decision}')
        if reference:
            f.write(f' | REF: {reference}')
        f.write('\n')
    print(f'Logged: {action}')

# Example usage:
# log_action('Review file', 'Extracted actionable content', 'Extracts/AI_DM_Documentation__Atomic_Extracts_Corrected.md')
