# Download Instructions for Llama and Stable Diffusion Models

## Llama 4 Model (Scout, Maverick, etc.)
1. Install the Llama CLI:
   ```sh
   pip install llama-stack
   ```
2. List available models:
   ```sh
   llama model list
   llama model list --show-all
   ```
3. Download your desired model using your custom URL:
   ```sh
   llama model download --source meta --model-id <MODEL_ID>
   # When prompted, paste your custom URL from Meta
   # Example destination: D:/AI/models/llama4.bin
   ```

## Stable Diffusion Model
- Download the official Stable Diffusion v1.5 weights from Hugging Face or the official source.
- Place the file at: `D:/AI/models/stable-diffusion-v1-5`

## Notes
- Ensure all model files are placed in `D:/AI/models/` as referenced in your config files.
- Do not share your custom URLs or model files publicly.
- For more details, see the official documentation and your Meta access email.
