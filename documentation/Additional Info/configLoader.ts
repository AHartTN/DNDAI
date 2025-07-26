// configLoader.ts
import * as fs from 'fs';
import * as path from 'path';
import * as dotenv from 'dotenv';
import * as yaml from 'js-yaml';

dotenv.config({ path: path.resolve(process.cwd(), '.env') });

export class ConfigLoader {
  private env: Record<string, string | undefined>;
  private yamlConfig: Record<string, any>;

  constructor(configPath = 'config.yaml') {
    this.env = {
      LLAMA4_MODEL_PATH: process.env.LLAMA4_MODEL_PATH,
      STABLE_DIFFUSION_MODEL_PATH: process.env.STABLE_DIFFUSION_MODEL_PATH,
      DISCORD_TOKEN: process.env.DISCORD_TOKEN,
      TWITCH_TOKEN: process.env.TWITCH_TOKEN,
      CAMPAIGN_DB_PATH: process.env.CAMPAIGN_DB_PATH,
      LOG_LEVEL: process.env.LOG_LEVEL || 'INFO',
    };
    const yamlFile = fs.readFileSync(path.resolve(process.cwd(), configPath), 'utf8');
    this.yamlConfig = yaml.load(yamlFile) as Record<string, any>;
  }

  get(key: string): any {
    return this.env[key] || this.yamlConfig[key];
  }

  all(): Record<string, any> {
    return { ...this.yamlConfig, ...Object.fromEntries(Object.entries(this.env).filter(([_, v]) => v !== undefined)) };
  }
}

// Usage example:
// const config = new ConfigLoader();
// const llamaPath = config.get('llama4_model_path');
// console.log(config.all());
