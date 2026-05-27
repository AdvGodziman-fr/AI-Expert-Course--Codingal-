import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)

# TODO: Load the data from the CSV dataset
def load_data(file_path='MODULE_1\imdb_top_1000.csv'):
    try: 
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File Not Found!")
        raise SystemExit


movies_df = load_data()

# Get a sorted list of unique genres in the whole dataset
genres = sorted({genre.strip() for sublist in movies_df["Genre"].dropna().str.split(", ") for genre in sublist})

# Filters movies by genre and rating, checks overview sentiment, and returns up to n recommendations
def recommend(genre=None, mood=None, rating=None, n=5):
    d = movies_df
    if genre:
        d = d[d["Genre"].str.contains(genre, case=False, na=False)]

    if rating is not None:
        d = d[d["IMDB_Rating"] >= rating]
    
    if d.empty:
        return "No Suitable Recommendations Found"
    
    d = d.sample(frac=1).reset_index(drop=True)
    need_nonneg = bool(mood)
    out = []

    for _ , r in d.iterrows():
        overview = r.get("Overview")

        if pd.isna(overview):
            continue

        movie_polarity = TextBlob(overview).sentiment.polarity
        if movie_polarity >= 0:
            out.append((r["Series_Title"], movie_polarity))

            if len(out) == n:
                break
    
    return out if out else "No suitable movie recommendations found."


# Get the sentiment category from TextBlob polarity
def get_sentiment(p):
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"


def show(recs, name):
    print(Fore.YELLOW + f"\n AI-Analyzed Movie Recommendations for {name}:")
    for i, (t,p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. {t} (Polarity: {p:.2f}, {get_sentiment(p)})")


def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)


# Show a list of genres and get input from the user
def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.CYAN}{i}. {g}")

    while True:
        x = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x) - 1]
        x = x.title()
        if x in genres:
            return x
        print(Fore.RED + "Invalid input. Try again.\n")


# Get input for the IMDB rating
def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6 - 9.3) or 'skip': ").strip()
        if x.lower() == "skip":
            return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again!\n")


# Welcome message
print(Fore.BLUE + "Welcome to your Personal Movie Recommendation Assistant! \n")
name = input(Fore.YELLOW + "What's your name? ").strip()
print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
print(Fore.BLUE + "\nLet's find the perfect movie for you!\n")

# Get genre input
genre = get_genre()


# TODO: Get mood input
mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
dots()
# TODO: Get mood polarity


# Get rating input
rating = get_rating()
print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
dots()


# TODO: SHOW RECOMMENDATIONS
recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)

# TODO: REQUEST FOR MORE RECOMMENDATIONS
while True:
    a = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()

    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}!\n")
        break
    if a == "yes":
        recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
        print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Invalid choice. Try again.\n")