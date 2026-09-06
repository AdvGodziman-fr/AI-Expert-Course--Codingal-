import requests
from config2 import HUGGING_FACE_API_KEY
import traceback

# Using a state-of-the-art zero-shot model
MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

# OPTIMIZATION 1: Enhanced, descriptive semantic labels for higher accuracy
TOPICS = [
"a promotional email about sales, discounts, or marketing offers",
"a social notification from a social media platform or messaging app",
"an automated update or notification about an account, order, or service"
]

HEADERS = {"Authorization": f'Bearer {HUGGING_FACE_API_KEY}'}

# Create a persistent session for better network performance
session = requests.Session()
session.headers.update(HEADERS)

def ask_hf(headline: str) -> dict:
    '''Send optimized zero-shot classification request to HuggingFace API'''
    payload = {
        "inputs": headline,
        "parameters": {
            "candidate_labels": TOPICS,
            # OPTIMIZATION 2: Multi-label evaluation gives independent, realistic probabilities
            "multi_label": True,
            # OPTIMIZATION 3: Framework-specific context template primes the NLI model
            "hypothesis_template": "This email text belongs to the category of {}."
        }
    }
    response = session.post(API_URL, json=payload, timeout=30)
    
    if not response.ok:
        raise RuntimeError(f"HuggingFace Error {response.status_code}: {response.text}")
        
    return response.json()

def parse_predictions(hf_response: dict) -> list:
    '''Convert HF response and sort items descending by confidence score'''
    print(hf_response)
    # parsed = [
    #     {"label": label, "score": score} 
    #     for label, score in zip(hf_response["labels"], hf_response["scores"])
    # ]

    # Explicitly ensure elements are sorted highest score first
    return sorted(hf_response, key=lambda x: x["score"], reverse=True)

def bar(score: float) -> str:
    '''Generate a simple text-based progress bar'''
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(headline: str, predictions: list):
    '''Display the classification results cleanly'''
    top_prediction = predictions[0]
    top_label = top_prediction["label"]
    top_score = top_prediction["score"]
    
    print()
    print("________________________________________________________________________________________")
    print("🗞 Optimized Email Topic Classifier 📧")
    print("________________________________________________________________________________________")
    print("Text:", headline)
    print(f"Best topic: {top_label}")
    print(f"Confidence: [{bar(top_score)}] {round(top_score * 100, 1)}%")
    print("\nRanked Predictions (Independent Probabilities):")
    
    # Safely display up to top 3 predictions
    for i, p in enumerate(predictions[:3], start=1):
        print(f"{i}. {p['label']:<28} [{bar(p['score'])}] {round(p['score']*100, 1)}%")
    print("=" * 60)

def main():
    print("Welcome to the OPTIMIZED EMAIL CLASSIFIER!")
    print("Configured Categories:")
    for topic in TOPICS:
        print(f" - {topic}")
    print("\nType 'exit' to stop.\n")
    
    while True:
        headline = input("Email Text: ").strip()
        if headline.lower() == "exit":
            print("Bye! Keep coding!")
            break
            
        if not headline:
            print("Please type an email text (not empty).\n")
            continue
            
        try:
            raw_response = ask_hf(headline)
            predictions = parse_predictions(raw_response)
            show(headline, predictions)
            print("________________________________________________________________________________________")
        except Exception as e:
            traceback.print_exc()
            print("\nOops! Something went wrong!")
            print("Reason: ", e)
            print("TIP: Check your HF API Key, Model ID, and Internet Connections\n")

if __name__ == "__main__":
    main()