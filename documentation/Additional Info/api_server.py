# api_server.py
from flask import Flask, request, jsonify
from narrative_engine import NarrativeEngine
from encounter_generator import EncounterGenerator
from npc_builder import NPCBuilder
from item_generator import ItemGenerator
from stable_diffusion_image_generator import StableDiffusionImageGenerator

app = Flask(__name__)
narrative_engine = NarrativeEngine()
encounter_generator = EncounterGenerator(narrative_engine.config)
npc_builder = NPCBuilder(narrative_engine.config)
item_generator = ItemGenerator(narrative_engine.config)
image_generator = StableDiffusionImageGenerator(narrative_engine.config)

@app.route('/api/narrative', methods=['POST'])
def api_narrative():
    data = request.get_json()
    context = data.get('context', '')
    player_actions = data.get('player_actions', [])
    campaign_state = data.get('campaign_state', {})
    result = narrative_engine.generate_narrative(context, player_actions, campaign_state)
    return jsonify(result)

@app.route('/api/encounter', methods=['POST'])
def api_encounter():
    data = request.get_json()
    party_level = data.get('party_level', 1)
    terrain = data.get('terrain', '')
    campaign_state = data.get('campaign_state', {})
    result = encounter_generator.generate_encounter(party_level, terrain, campaign_state)
    return jsonify(result)

@app.route('/api/npc', methods=['POST'])
def api_npc():
    data = request.get_json()
    archetype = data.get('archetype', 'commoner')
    tags = data.get('tags', [])
    campaign_state = data.get('campaign_state', {})
    result = npc_builder.build_npc(archetype, tags, campaign_state)
    return jsonify(result)

@app.route('/api/item', methods=['POST'])
def api_item():
    data = request.get_json()
    rarity = data.get('rarity', 'common')
    type_ = data.get('type', 'sword')
    campaign_state = data.get('campaign_state', {})
    result = item_generator.generate_item(rarity, type_, campaign_state)
    return jsonify(result)

@app.route('/api/image', methods=['POST'])
def api_image():
    data = request.get_json()
    prompt = data.get('prompt', '')
    style = data.get('style', 'default')
    output_type = data.get('output_type', 'portrait')
    result = image_generator.generate_image(prompt, style, output_type)
    return jsonify(result)

# Additional endpoints for other modules can be added here

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
