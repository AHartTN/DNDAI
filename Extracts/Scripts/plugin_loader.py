# DNDAI Plugin/Extension Loader Stub
"""
Python module for dynamic loading and registration of agent plugins/extensions.
"""
import importlib
import os

PLUGINS_DIR = 'src/ai/plugins'


def load_plugins():
    plugins = []
    if not os.path.exists(PLUGINS_DIR):
        os.makedirs(PLUGINS_DIR)
    for fname in os.listdir(PLUGINS_DIR):
        if fname.endswith('.py'):
            mod_name = fname[:-3]
            mod = importlib.import_module(f'src.ai.plugins.{mod_name}')
            plugins.append(mod)
    return plugins

# Example usage:
# plugins = load_plugins()
# for plugin in plugins:
#     plugin.run()
