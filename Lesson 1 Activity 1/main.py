print("Hello! I am an AI bot.")
name = input("What is your name? ")

print(f"Nice to meet you, {name}")

feeling = input("How are you feeling? ").lower()

if "good" in feeling or "great" in feeling or "happy" in feeling:
    print("I'm glad to hear that!")
elif "sad" in feeling or "bad" in feeling or "depressed" in feeling:
    print("Hope you feel better!")
else:
    print("It's difficult to put into words, I can understand.")


print(f"It's been great talking to you, {name} see you!")