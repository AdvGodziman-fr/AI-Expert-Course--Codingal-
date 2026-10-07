from huggingface_hub import InferenceClient
from PIL import Image, ImageEnhance, ImageFilter
import os

HF_API_KEY = os.environ.get("HF_API_KEY")

def generate_image_from_text(prompt):
    client = InferenceClient(provider="auto", api_key=HF_API_KEY)
    return client.text_to_image(
        prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",
    )
    
def post_process_image(image):
    image1 = daylight_effect(image)
    image2 = night_mood_effect(image)

    return image1, image2

def daylight_effect(image_prompt):
    image = ImageEnhance.Brightness(image_prompt).enhance(1.3)
    image = ImageEnhance.Contrast(image_prompt).enhance(1.1)
    return image.filter(ImageFilter.GaussianBlur(radius=0.1))

def night_mood_effect(image_prompt):
    image = ImageEnhance.Brightness(image_prompt).enhance(0.5)
    image = ImageEnhance.Contrast(image_prompt).enhance(0.8)
    return image.filter(ImageFilter.GaussianBlur(radius=0.5))

def main():
    print("Welcome to the Styled Image Creator!")
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
            daylight_image, night_image = post_process_image(image)
            daylight_image.show()
            night_image.show()

            save_option = input("Do you want to save the processed images? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()
                daylight_image.save(f"{file_name}(DayLight Mod).png")
                night_image.save(f"MODULE_5\Projects\Project 2 = Image\{file_name}(NightMood Mod).png")
                print(f"Images saved.\n")

            print("-" * 80 + "\n")

        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()

