# narrative_engine.py
import logging
from config_loader import Config
import llama_cpp

class NarrativeEngine:
    def __init__(self):
        self.config = Config()
        self.llama_path = self.config.get('llama4_model_path')
        self.context_window = self.config.get('context_window_size') or 4096
        self.prompt_templates = self.config.get('prompt_templates') or {}
        logging.basicConfig(level=self.config.get('log_level') or 'INFO')
        logging.info(f"Loaded Llama 4 model from: {self.llama_path}")
        # Load Llama 4 model
        self.llm = llama_cpp.Llama(model_path=self.llama_path, n_ctx=self.context_window)

    def generate_narrative(self, context, player_actions, campaign_state):
        # Compose prompt using context, player actions, and campaign state
        prompt = self._build_prompt(context, player_actions, campaign_state)
        # Call Llama 4 model
        output = self.llm(prompt, max_tokens=512)
        # Parse output (stub: replace with real parsing logic)
        return {
            "narrative": output["choices"][0]["text"],
            "next_hooks": ["Stub: parse hooks from output"],
            "dm_notes": "Stub: parse DM notes from output"
        }

    def _build_prompt(self, context, player_actions, campaign_state):
        # Example prompt engineering logic
        prompt = f"Context: {context}\nPlayer Actions: {player_actions}\nCampaign State: {campaign_state}\nGenerate next narrative, hooks, and DM notes."
        return prompt

# Integrated Llama 4 model using llama-cpp-python in Python narrative engine.
# Updated generate_narrative to use real model calls and prompt engineering.
# See README for llama-cpp-python installation and configuration details.

# Usage example:
# engine = NarrativeEngine()
# result = engine.generate_narrative(context, player_actions, campaign_state)
# print(result)
