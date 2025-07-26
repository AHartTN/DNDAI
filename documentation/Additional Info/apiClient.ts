// apiClient.ts
import axios from 'axios';

export async function getNarrative(context: string, playerActions: any[], campaignState: any) {
  const response = await axios.post('http://127.0.0.1:5000/api/narrative', {
    context,
    player_actions: playerActions,
    campaign_state: campaignState
  });
  return response.data;
}

export async function getEncounter(partyLevel: number, terrain: string, campaignState: any) {
  const response = await axios.post('http://127.0.0.1:5000/api/encounter', {
    party_level: partyLevel,
    terrain,
    campaign_state: campaignState
  });
  return response.data;
}

export async function getNPC(archetype: string, tags: string[], campaignState: any) {
  const response = await axios.post('http://127.0.0.1:5000/api/npc', {
    archetype,
    tags,
    campaign_state: campaignState
  });
  return response.data;
}

export async function getItem(rarity: string, type: string, campaignState: any) {
  const response = await axios.post('http://127.0.0.1:5000/api/item', {
    rarity,
    type,
    campaign_state: campaignState
  });
  return response.data;
}

export async function getImage(prompt: string, style: string, outputType: string) {
  const response = await axios.post('http://127.0.0.1:5000/api/image', {
    prompt,
    style,
    output_type: outputType
  });
  return response.data;
}

// Usage example:
// getNarrative('The party enters the ruins.', ['explore'], {}).then(console.log);
// getEncounter(5, 'forest', {}).then(console.log);
// getNPC('warrior', ['brave', 'loyal'], {}).then(console.log);
// getItem('rare', 'sword', {}).then(console.log);
// getImage('a fantasy landscape', 'vivid', 'jpeg').then(console.log);
