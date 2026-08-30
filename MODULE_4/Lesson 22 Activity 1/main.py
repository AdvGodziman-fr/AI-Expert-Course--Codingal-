import requests
from config import HF_API_KEY 

# TODO: Where is our API KEY?

# TODO: TO WHICH MODEL ARE WE GOING TO SEND OUR REQUESTS?
MODEL_ID = "facebook/bart-large-mnli"

API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

# TODO: WHICH TOPICS?
TOPICS = ['Sports', 'Technology', 'Politics', 'Business', 'Nature', "Health"]

# TODO: HOW TO ATTACH API KEY TO REQUEST? [We are adding a bearer token to our API Request]
HEADERS = {"Authorization": f'Bearer {HF_API_KEY}'}

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


def best_topic(predictions: list):
    '''Find the most likely topic predicted by the BART NLI model'''
    best_category = max(predictions, key=lambda x:x["score"])
    return best_category["label"], best_category["score"]


# TODO: Create the progress bar graphic
def bar(score: float) -> str:
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(headline: str, predictions: list):
    top_label, top_score = best_topic(predictions)
    print("\n" + "=" * 60)
    print("🗞  News Topic Classifier 📊")
    print("=" * 60)
    print("Headline:", headline)
    print(f"Best topic: {top_label}")
    print(f"Confidence: [{bar(top_score)}] {round(top_score * 100, 1)}%")

    print("\nTop 3 guesses:")
    # TODO: Sort the prediction scores received from HF API in descending order & display top 3 predicted topics
    top3 = sorted(predictions, key = lambda x: x["score"], reverse = True)

    for i, p in enumerate(top3, start=1):
        print(f"{i}. {p['label']:<11} [{bar(p['score'])}] {round(p['score']*100, 1)}%")
        if i == 3:
            break

    print("=" * 60)


def main():
    print("Welcome! Type a news headline and I'll guess the topic.")
    print("Topics:", ", ".join(TOPICS))
    print("Type 'exit' to stop.\n")

    while True:
        headline = input("Headline: ").strip()

        if headline.lower() == "exit":
            print("Bye! Keep coding!")
            break

        if not headline:
            print("Please type a headline (not empty).\n")
            continue

        # TODO: ATTEMPT TO MAKE REQUEST TO HUGGINGFACE API LOGIC & RETRY IN CASE OF ERRORS
        try:
            predictions = ask_hf(headline)
            show(headline, predictions)

        except Exception as e:
            print("Oops! Something went wrong!")
            print("Reason: ", e)
            print("TIP: Check your HF API Key and Internet Connections")

if __name__ == "__main__":
    main()

