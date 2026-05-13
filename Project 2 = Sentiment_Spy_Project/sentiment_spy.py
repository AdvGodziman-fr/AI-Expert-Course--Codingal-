import colorama
import time
from datetime import datetime
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

convo_history = []

# FUNCTION TO GET THE VALID NAME
def get_valid_name():
    c = 0
    while True:
        username = input(f"{Fore.LIGHTRED_EX}Enter your name to continue: {Fore.YELLOW}")
        print()
        
        if " " in username:
            x = username.split()

            for ic in x:
                if ic.isalpha():
                    c += 1
                else:
                    c += 0


            if c == len(x):
                print(f"{Fore.GREEN}Woohoo! Welcome aboard, Detective {username.upper()}. Looking forward to this journey!")
                return username
            else:
                print(f"{Fore.RED}Beep! Beep! Looks like you've entered your name incorrectly. Kindly do not use any symbols or numbers in your username.")
                continue
            
        else:
            x = username
            if x.isalpha():
                print(f"{Fore.GREEN}Woohoo! Welcome aboard, Detective {username.upper()}. Looking forward to this journey!")
                return username
            else:
                print(f"{Fore.RED}Beep! Beep! Looks like you've entered your name incorrectly. Kindly do not use any symbols or numbers in your username.")
                continue

# FUNCTION FOR VERY BASIC ANIMATION PROCESSING
def show_processing_animation():
    print("IN...")
    time.sleep(1)

    for i in reversed(range(1, 4)):
        print(i, end = "            ")
        time.sleep(1)

# FUNCTION FOR ANALYSING THE SENTIMENT 
def analyse_sentiment(user_input):

    show_processing_animation()
    print()
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = " 😊 "

    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = " 😭 "
        
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = " 😑 "

    print(f"{color}{emoji}{sentiment_type} Sentiment Detected! (Polarity: {polarity:.2f})")
    convo_history.append({"text": user_input, "polarity": polarity, "type": sentiment_type})

# FUNCTION TO EXECUTE COMMANDS 
def execute_command(command):
    if command == "history":
        if not convo_history:
            print(f"{Fore.YELLOW}No conversation history yet.")
        else:
            print(f"{Fore.CYAN} Conversation History:")

            for i, h in enumerate(convo_history, start=1):
                print(f"{i}. [{h['type']}] {h['text']} ({h['polarity']:.2f})")

    elif command == "summary":
        if not convo_history:
            print("No summary currently detective!")

        else:
            print("Summary of the conversation: ")

            p = sum(1 for h in convo_history if h['type'] == "Positive")
            ng = sum(1 for h in convo_history if h['type'] == "Negative")
            ne = sum(1 for h in convo_history if h['type'] == "Neutral")

            print(f"{Fore.MAGENTA}--- Mission Summary ---")
            print(f"{Fore.GREEN}Positive: {p} {Fore.CYAN}| {Fore.RED}Negative: {ng} {Fore.CYAN}| {Fore.YELLOW}Neutral: {ne}")

    elif command == "reset" or command == "clear":
        if not convo_history:
            print("Nothing to clear, detective!")
        
        else:
            convo_history.clear()
            print("Reset successful!")

    elif command == "help":
        print("You are eligible to use the following commands: ")
        print("1. History - Displays all the previous messages and their sentiment analyses.")
        print("2. Summary - Displays the summary of all sentiment analyses")
        print("3. Reset - Resets all of the stored data, which includes conversation history and sentiment couters.")
        print("4. Exit - End the mission")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------DEFINING FUNCTIONS OVER-------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print()
print()
print(f"{Fore.BLUE}🕵️    WELCOME ABOARD ON 'THE SENTIMENT DETECTIVE'!!    🕵️")
print(f"{Fore.GREEN}Get your minds blown by this AI tool as it detects your sentiments and emotions while you send up lines and lines of text!")

# Calling Valid Name Function
final_name = get_valid_name()

print()
print(f"{Fore.CYAN}Type a sentence into the prompt and I will analyze your sentences with TextBlob and show you the sentiment. I will also save your history of analyses.")
print()
print(f"{Fore.CYAN}Commands you can use? => {Fore.YELLOW}'summary'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN}, {Fore.YELLOW}'reset/clear'{Fore.CYAN}, {Fore.YELLOW}'help'{Fore.CYAN} or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.\n")
print()
print(f"{Fore.RED} Note: Please do refrain from using these keywords in your sentences for analysis! Thank you!")
print(f"                                          {Fore.MAGENTA}SO...   LET'S GET STARTED!!!")
print()


while True:
    user_input = input(f"{Fore.BLUE}>> {Style.RESET_ALL}").strip()

    if "history" in user_input.lower():
        command = "history"
        execute_command(command)
        continue

    elif "summary" in user_input.lower():
        command = "summary"
        execute_command(command)
        continue

    elif "reset" in user_input.lower() or "clear" in user_input.lower():
        command = "reset"
        execute_command(command)
        continue

    elif "help" in user_input.lower():
        command = "help"
        execute_command(command)
        continue

    elif user_input.lower() == "exit":
        p = sum(1 for h in convo_history if h['type'] == "Positive")
        ng = sum(1 for h in convo_history if h['type'] == "Negative")
        ne = sum(1 for h in convo_history if h['type'] == "Neutral")

        print(f"\n{Fore.GREEN} Quitting Sentiment Detective. Farewell, Agent {final_name}!")
        print()
        print(f"{Fore.LIGHTYELLOW_EX}FINAL MISSION REPORT")
        print(f"{Fore.GREEN}Positive: {p}")
        print(f"{Fore.RED}Negative: {ng}")
        print(f"{Fore.YELLOW}Neutral: {ne}")
        
        filename = f"Detective_{final_name}_sentiment_analysis.txt"
        f = open(filename, "w")
        f.write("FINAL MISSION REPORT\n")
        f.write(f"Positive: {p}\n")
        f.write(f"Negative: {ng}\n")
        f.write(f"Neutral: {ne}\n")
        break

    analyse_sentiment(user_input)