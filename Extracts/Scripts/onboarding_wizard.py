# DNDAI Interactive Onboarding Wizard (CLI)
"""
Guides new contributors through setup, documentation review, and config verification.
"""
import os

def onboarding():
    print('Welcome to DNDAI!')
    print('Step 1: Review documentation in _Samples and Extracts/Blueprints.')
    print('Step 2: Verify config file at src/config/config.yaml.')
    if os.path.exists('src/config/config.yaml'):
        print('Config file found.')
    else:
        print('Config file missing!')
    print('Step 3: Run test_stub_generator.py to create test stubs.')
    print('Step 4: Review contribution standards in Blueprint_Documentation_and_Onboarding.md.')
    print('Onboarding complete!')

if __name__ == '__main__':
    onboarding()
