from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
import os

# MODEL PRIORITY LIST - Primary model first, fallbacks only if it fails
MODELS = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "runwayml/stable-diffusion-v1-5", # Fallback 2
    "ByteDance/SDXL-Lightning",
    "stabilityai/sdxl-turbo",
]

HF_API_KEY = os.environ.get("HF_API_KEY")

# Initialize client
client = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: black-forest-labs/FLUX.1-Krea-dev")
print("Type 'quit' to exit\n")

while True:
    image = None
    model = "black-forest-labs/FLUX.1-Krea-dev"
    prompt = input("Enter prompt: ").strip()
    if prompt.lower() in ["quit", "exit", "q"]:
        break
    if not prompt:
        continue

    print("Generating...")
    
    image = client.text_to_image(prompt, model=model, negative_prompt="blurriness, distortions", guidance_scale=7.5)

    # If we got an image, save and display it
    image.show()
    req = input("Image generated! Would you like to save it? ").strip().lower()

    if req == "yes" or req == "alright":
        if image:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_{timestamp}.png"
            image.save(filename)
            print(f"✓ Saved: {filename}")
            print()
        else:
            print("Error: All models failed. Check your API key.\n")
    else:
        print("Alright! Image is not saved.")

print("Goodbye!")