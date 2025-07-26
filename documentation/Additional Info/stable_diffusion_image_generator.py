import os
import json
import random

class StableDiffusionImageGenerator:
    def __init__(self, config):
        self.config = config
        self.model_path = self.config.get('stable_diffusion_model_path')
        self.style_guides_path = self.config.get('style_guides')
        self.style_guides = self._load_json(self.style_guides_path)

    def _load_json(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def generate_image(self, prompt, style, output_type):
        # TODO: Integrate with real Stable Diffusion inference (e.g., diffusers, invokeai)
        style_guide = self.style_guides.get(style, "default")
        image_url = f"/images/generated/{random.randint(1000,9999)}_{output_type}.png"
        metadata = {"prompt": prompt, "style": style_guide, "output_type": output_type}
        return {"image_url": image_url, "metadata": metadata}