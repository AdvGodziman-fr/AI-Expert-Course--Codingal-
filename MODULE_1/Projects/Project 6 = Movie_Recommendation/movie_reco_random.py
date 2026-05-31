import pandas as pd
from colorama import Fore, Style
import time
import random

i = 0

def load_data(file_path='MODULE_1\imdb_top_1000.csv'):
    try: 
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File Not Found!")
        raise SystemExit
    
movies_df = load_data()
    

def animation_time():
    for i in range(0, 3):
        time.sleep(1)
        print(".", end = "", flush=True)


def name_check():
    while True:
        username = input(f"{Fore.CYAN}Please enter your name: {Fore.GREEN}").strip()
        name = username.replace(" ", "")

        print(f"{Fore.RESET}Verifying username", end="")
        animation_time()

        print()
        if name.isalpha():
            return username
            
        else:
            print("There has been an error! Please try again!")
            print()
            continue

def recom_random(n=5):
    d = movies_df
    suggestions = []

    for i in range(n):
        movie = random.choice(d["Series_Title"])
        suggestions.append(movie)

    return suggestions


def reco_checker():
    reco = input(">> ").strip().lower()
    if "random" in reco: 
        print("Here are your five recommendations: ")
        print()

        lst = recom_random()

        for t, f in enumerate(lst, start=1):
            print(f"{t}. {Fore.YELLOW}{Style.BRIGHT}{f}{Fore.RESET}{Style.RESET_ALL}")

        print()
        
    elif "AI" in reco:
        print("Alright, please wait a few seconds...")

    else:
        print("Error! Kindly type in 'AI' for AI-based recommendation or 'random' for Random recommendation")            


def main_convo():
    print(f"{Fore.LIGHTMAGENTA_EX}Welcome to {Fore.LIGHTGREEN_EX}MOVIE-RECO.com{Fore.LIGHTMAGENTA_EX}, where you can get personalised suggestions regarding movies!{Style.RESET_ALL}")
    print()
    final_name = name_check()

    print(f"{Fore.LIGHTMAGENTA_EX}Greetings, {Fore.LIGHTBLUE_EX}{final_name}{Fore.LIGHTMAGENTA_EX}!{Fore.RESET}")
    print("Would you like to get a random recommendation or an AI-Powered Recommendation of a movie? ")

    reco_checker()

main_convo()
