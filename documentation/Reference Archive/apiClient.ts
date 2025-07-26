/**
 * Prototype API client for DNDAI research workspace.
 * This file is for reference and planning only. It is not runnable production code.
 * Do not use for deployment. For symbolic reference, use *API_CLIENT* if needed.
 */
// Moved to research/prototypes/apiClient.ts
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
// Moved to client/apiClient.ts
