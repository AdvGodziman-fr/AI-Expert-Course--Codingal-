import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from huggingface_hub import InferenceClient
import os

HF_API_KEY = os.environ.get("HF_API_KEY")

MODELS = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    "CompVis/stable-diffusion-v1-4",
    "black-forest-labs/FLUX.1-schnell",
]

client = InferenceClient(api_key=HF_API_KEY)

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Accept": "image/png"}

def generate_image_from_text(prompt):
    """prompt -> PIL.Image (or raises Exception)."""
    #payload, last_err = {"inputs": prompt}, None

    for model in MODELS:
        try:
            image = client.text_to_image(prompt, model=model)
            return image  # Success! Exit the loop

        except Exception as e:
            print(f"  Executing next...")
            print(e)
            continue


def post_process_image(image):
    """Returns the processed PIL.Image (same I/O as your code)."""
    #A function that is defied inside a class is called a method
    image = ImageEnhance.Brightness(image).enhance(1.2)
    image = ImageEnhance.Contrast(image).enhance(1.32)
    return image.filter(ImageFilter.GaussianBlur(radius = 5))


def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates an image from text and applies post-processing effects.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a description for the image (or 'exit' to quit):\n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            print("\nGenerating image...")
            image = generate_image_from_text(user_input)
            print("Applying post-processing effects...\n")
            processed_image = post_process_image(image)
            processed_image.show()

            save_option = input("Do you want to save the processed image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()
                processed_image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")

            print("-" * 80 + "\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()

