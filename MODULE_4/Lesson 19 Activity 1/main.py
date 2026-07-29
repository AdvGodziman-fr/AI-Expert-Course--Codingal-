import requests

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    # Make the request to API
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}" 

    else:
        return "ERROR: Failed to return joke!"


def main():
    print("Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press enter to get a new joke, or type 'exit' to exit.")

        if user_input.lower() == "exit":
            break

        joke = fetch_random_joke()
        print(joke)

main()