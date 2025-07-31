# DNDAI Automated Test Stub Generator
"""
Creates test stubs for each agent module in src/ai.
"""
import os

SRC_DIR = 'src/ai'
TESTS_DIR = 'src/tests'

def generate_test_stubs():
    if not os.path.exists(TESTS_DIR):
        os.makedirs(TESTS_DIR)
    for fname in os.listdir(SRC_DIR):
        if fname.endswith('.py'):
            test_name = f'test_{fname}'
            test_path = os.path.join(TESTS_DIR, test_name)
            if not os.path.exists(test_path):
                with open(test_path, 'w') as f:
                    f.write(f"# Test stub for {fname}\n")
    print('Test stubs generated.')

if __name__ == '__main__':
    generate_test_stubs()
