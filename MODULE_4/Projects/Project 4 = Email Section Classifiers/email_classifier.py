import requests
from config2 import HUGGING_FACE_API_KEY

MODEL_ID = "facebook/bart-large-mnli"

API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

TOPICS = ['Primary', 'Promotions', 'Social', 'Updates']
HEADERS = {"Authorization": f'Bearer {HUGGING_FACE_API_KEY}'}

# Asking Hugging Face for the details of the desired topics
def ask_hf(headline: str):
    '''Send request to HuggingFace API'''

    payload = {
        "inputs": headline,
        "parameters": {
            "candidate_labels": TOPICS
        }
    }

    r = requests.post(API_URL, headers=HEADERS, json = payload, timeout = 30) #In seconds, not milliseconds

    if not r.ok:
        raise RuntimeError(f"HuggingFace Error: {r.status}: {r.text}")

    return r.json()

# Getting the best topic
def best_topic(predictions: list):
    '''Find the most likely topic predicted by the BART NLI model'''
    best_category = max(predictions, key=lambda x:x["score"])
    score = best_category["score"]
    return best_category["label"], best_category["score"]

def bar(score: float) -> str:
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(headline: str, predictions: list):
    top_label, top_score = best_topic(predictions)
    print()
    print("________________________________________________________________________________________")
    print("🗞  Email Topic Classifier 📧")
    print("________________________________________________________________________________________")
    print("Text:", headline)
    print(f"Best topic: {top_label}")
    print(f"Confidence: [{bar(top_score)}] {round(top_score * 100, 1)}%")


# Main Loop
def main():
    print("Welcome to EMAIL CLASSIFIER!")
    print("Topics:", ", ".join(TOPICS))
    print("Type 'exit' to stop.\n")

    while True:
        headline = input("Email Text: ").strip()

        if headline.lower() == "exit":
            print("Bye! Keep coding!")
            break

        if not headline:
            print("Please type an email text (not empty).\n")
            continue

        try:
            predictions = ask_hf(headline)
            show(headline, predictions)
            print("________________________________________________________________________________________")

        except Exception as e:
            print("Oops! Something went wrong!")
            print("Reason: ", e)
            print("TIP: Check your HF API Key and Internet Connections")

if __name__ == "__main__":
    main()

