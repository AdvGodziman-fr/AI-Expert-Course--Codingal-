# Name the file as main.py , complete the code by writing remaining functions

import re, random
from colorama import Fore, init

# # Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# # Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    p = normalize_input(input("Beaches, mountains or cities"))

    if p in destinations:
        suggestion = random.choice(destinations[p])
        print(f"Do you like {suggestion}? (Yes or No)")

        ans = normalize_input(input())

        if ans == "yes":
            print(f"Enjoy the {suggestion}!")
            show_help()

        elif ans == "no":
            print("Let's try another one!")
            recommend()

        else:
            print("Please say Yes or No! Response not considered.")

    else:
        print("Sorry! I don't have that destination.")

# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(f"Travel Bot:", end = "") 
    place = normalize_input(input("Where to? "))
    time = normalize_input(input("How many days? "))

    print(f"Packing tips for {time} days in the location {place}")

    print("1. Check the weather forecast.")
    print("2. Pack versatile clothes.")
    print("3. Bring chargers.")

# Tell a random joke
def joke():
    print(f"Travel Bot:", end = "") 
    print(f"{random.choice(jokes)}")

# Display help menu
def show_help():
    print("I can: ")
    print("1. Suggest travel spots")
    print("2. Offer packing tips")
    print("3. Tell a joke (travel-related)")
    print("Press 'bye' or 'exit' to end.")

# Main chat loop
def chat():
    print("Hello! I am a travel bot.")
    c = input("What's your name? ")

    print(f"Hello {c}. Nice to meet you!")
    show_help()

    while True:
        user_input = input(">>  ")
        user_input = normalize_input(user_input)

        if 'recommend' in user_input or 'suggest' in user_input:
            recommend()
        
        elif 'tips' in user_input or 'packing' in user_input:
            packing_tips()

        elif 'joke' in user_input:
            joke()

        elif 'help' in user_input:
            show_help()

        elif "exit" in user_input:
            break

        else:
            print("Unexpected input! Try again.")

# Run the chatbot
if __name__ == "__main__":
    chat()