import pandas as pd
from colorama import Fore, Style
import time
import random

# Load the dataset
def load_data(file_path="MODULE_1\imdb_top_1000.csv"):
    try: 
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File Not Found! Please check your file path.")
        raise SystemExit
    
movies_df = load_data()

def animation_time():
    for _ in range(0, 3):
        time.sleep(0.5)
        print(".", end = "", flush=True)
    print()

def name_check():
    while True:
        username = input(f"{Fore.CYAN}Please enter your name: {Fore.GREEN}").strip()
        name = username.replace(" ", "")

        print(f"{Fore.RESET}Verifying username", end="")
        animation_time()

        if name.isalpha() and len(name) > 0:
            return username
        else:
            print(f"{Fore.RED}There has been an error! Names should only contain letters. Please try again!{Fore.RESET}\n")

# TASK 3 & 4: Select a random movie and display detailed information
def get_random_recommendation():
    # Pick a completely random single row from the dataframe
    random_row = movies_df.sample(n=1).iloc[0]
    return random_row

# TASK 2 & 4: Filter by user preferences and return an AI/Rule-based match
def get_ai_recommendation(genre, min_rating):
    # Filter by genre (case-insensitive containment) and IMDB Rating
    filtered_df = movies_df[
        (movies_df['Genre'].str.contains(genre, case=False, na=False)) & 
        (movies_df['IMDB_Rating'] >= min_rating)
    ]
    
    if not filtered_df.empty:
        # Return the highest-rated movie matching the criteria or a random selection from the filtered pool
        return filtered_df.sample(n=1).iloc[0]
    else:
        return None

# TASK 4: Standardized display function for movie details
def display_movie_details(movie_row):
    print(f"\n{Fore.GREEN}========================================")
    print(f"{Fore.YELLOW}{Style.BRIGHT}🎬  Title: {movie_row.get('Series_Title', 'N/A')}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🎭  Genre(s): {Fore.RESET}{movie_row.get('Genre', 'N/A')}")
    print(f"{Fore.CYAN}📝  Overview: {Fore.RESET}{movie_row.get('Overview', 'N/A')}")
    print(f"{Fore.CYAN}⭐  IMDB Rating: {Fore.RESET}{movie_row.get('IMDB_Rating', 'N/A')}/10")
    
    # Simple rule-based mock Sentiment Analysis based on IMDB Rating
    rating = movie_row.get('IMDB_Rating', 0)
    if rating >= 8.3:
        sentiment = f"{Fore.GREEN}Very Positive"
    elif rating >= 7.8:
        sentiment = f"{Fore.LIGHTGREEN_EX}Positive"
    else:
        sentiment = f"{Fore.WHITE}Neutral"
        
    print(f"{Fore.CYAN}❤️ Sentiment Analysis: {sentiment}{Fore.RESET}")
    print(f"{Fore.GREEN}========================================{Fore.RESET}\n")


# TASK 5: Handles loop and system mechanics
def recommendation_flow():
    while True:
        print(f"\n{Fore.WHITE}Choose your recommendation type:")
        print(f"1. {Fore.LIGHTBLUE_EX}AI-based Recommendation")
        print(f"2. {Fore.LIGHTYELLOW_EX}Random Recommendation")
        
        choice = input(f"{Fore.RESET}>> ").strip().lower()
        
        # --- AI-BASED PATH ---
        if 'ai' in choice or choice == '1':
            print(f"\n{Fore.MAGENTA}--- AI Preference Filter ---{Fore.RESET}")
            genre_input = input("Enter preferred genre (e.g., Action, Drama, Comedy): ").strip()
            
            try:
                rating_input = float(input("Enter minimum IMDB Rating threshold (e.g., 7.5 to 9.0): ").strip())
            except ValueError:
                print(f"{Fore.RED}Invalid rating format. Defaulting threshold to 7.5{Fore.RESET}")
                rating_input = 7.5
                
            print("\nProcessing preferences with our AI engine", end="")
            animation_time()
            
            matched_movie = get_ai_recommendation(genre_input, rating_input)
            
            if matched_movie is not None:
                print("Here is your AI-powered recommendation:")
                display_movie_details(matched_movie)
            else:
                print(f"{Fore.RED}No movies completely matched those custom criteria. Let's show you a highly rated alternative option instead!{Fore.RESET}")
                display_movie_details(get_random_recommendation())
                
        # --- RANDOM PATH ---
        elif 'random' in choice or choice == '2':
            print("\nSelecting a random hidden gem for you", end="")
            animation_time()
            
            random_movie = get_random_recommendation()
            print("Here is your random recommendation:")
            display_movie_details(random_movie)
            
        else:
            print(f"{Fore.RED}Invalid selection. Kindly enter '1' / 'AI' or '2' / 'random'.{Fore.RESET}")
            continue
            
        # TASK 5: Repeat the process loop check
        print("Would you like to get another movie recommendation?")
        repeat = input(">> ").strip().lower()
        if not ('yes' in repeat or 'ya' in repeat or 'yup' in repeat or repeat == 'y'):
            print(f"\n{Fore.LIGHTMAGENTA_EX}Thank you for using MOVIE-RECO.com! Enjoy your movie marathon! 🍿{Fore.RESET}")
            break

def main_convo():
    print(f"{Fore.LIGHTMAGENTA_EX}Welcome to {Fore.LIGHTGREEN_EX}MOVIE-RECO.com{Fore.LIGHTMAGENTA_EX}, where you can get personalized suggestions regarding movies!{Style.RESET_ALL}")
    print("--------------------------------------------------------------------------------")
    
    final_name = name_check()
    print(f"\n{Fore.LIGHTMAGENTA_EX}Greetings, {Fore.LIGHTBLUE_EX}{final_name}{Fore.LIGHTMAGENTA_EX}! Let's find some entertainment.{Fore.RESET}")
    
    # Fire up the loop flow
    recommendation_flow()

if __name__ == "__main__":
    main_convo()