# DNDAI Self-Improvement Log Analyzer
"""
Parses the running improvement log and suggests next actions or optimizations.
"""
import re

LOG_PATH = '_Samples/Process_Running_Improvement_Log.md'
SUGGESTIONS_PATH = 'src/logs/self_improvement_suggestions.md'


def analyze_log():
    suggestions = set()
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Next Steps:' in line:
                step = line.split('Next Steps:')[-1].strip()
                if step:
                    suggestions.add(step)
    with open(SUGGESTIONS_PATH, 'w', encoding='utf-8') as f:
        f.write('# Self-Improvement Suggestions\n\n')
        for s in sorted(suggestions):
            f.write(f'- {s}\n')
    print(f'Suggestions written to {SUGGESTIONS_PATH}')

if __name__ == '__main__':
    analyze_log()
