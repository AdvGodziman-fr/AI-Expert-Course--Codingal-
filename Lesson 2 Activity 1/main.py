import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initializing colorama
colorama.init(autoreset=True)

print(f"{Fore.CYAN}🕵️   Welcome to Sentiment Detective!   🕵️")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()

if user_name == "":
    user_name = "Demon Slayer"

# Store conversation history as a list of tuples: (text -> User input, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Detective {user_name}!")

print(f"{Fore.CYAN}Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment. I will also save your history of analyses.")

print(f"{Fore.CYAN}Type {Fore.YELLOW}'clear'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'quit'{Fore.CYAN} to quit.\n")


# The main loop - should run forever until "quit" command is typed
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    # Check if user did not input anything
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.")
        continue

    # Check for commands
    if user_input.lower() == "quit":
        print(f"\n{Fore.BLUE} Quitting Sentiment Detective. Farewell, Agent {user_name}!")
        break
    
    # How to quit a loop?
    elif user_input.lower() == "clear":
        # Empty the conversation_history list
        conversation_history.clear()
        # Go back to loop start
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.")
        else:
            print(f"{Fore.CYAN} Conversation History:")
            # TODO: Iterate over the history and print every user-provided sentence with sentiment analysis result
            for i, (text, polarity, sentiment_type) in enumerate(conversation_history):

                # TODO: Based on sentiment_type, assign color & emoji
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "😭"
                else:
                    color = Fore.YELLOW
                    emoji = "😑"
                print(f"{i}. {color}{emoji} {text} (Polarity: {polarity:.2f}, {sentiment_type})")

        # TODO: Go back to loop start
        continue


    # TODO: Let's analyze the sentiment
    polarity = TextBlob(user_input).sentiment.polarity

    # TODO: Check the polarity. Based on it, assign the appropriate sentiment_type, color, and emoji
    # EMOJIS: 😊  😭  😑
    if polarity > 0:
        sentiment_type = "positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < 0:
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "😭"
    else:
        sentiment_type = "neutral"
        color = Fore.YELLOW
        emoji = "😑"
    
    # After analyzing each sentence, save in the history
    conversation_history.append((user_input, polarity, sentiment_type))
    # Print result with color, emojis, and polarity
    # FORMAT: 😊 Positive sentiment detected (Polarity: 0.50)
    print(f"{color}{emoji}{sentiment_type} Sentiment Detected! (Polarity: {polarity:.2f})")