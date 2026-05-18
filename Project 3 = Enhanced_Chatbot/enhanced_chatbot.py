import re, random
import time
import colorama
from colorama import Fore, Style
from datetime import datetime

colorama.init(autoreset=True)

convo_history = []

# Lists and Dictionaries:
destinations = {
    "beaches": ["Bali", "Maldives"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": [],
    "trending destinations": ["Singapore", "Bangkok", "Tokyo", "Paris", "Kuala Lumpur", "London", "Phuket"] 
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]


# FUNCTION 1: Getting the valid name
def valid_name():
    c = 0
    while True:
        username = input(f"{Fore.LIGHTRED_EX}Please enter your name to continue: {Fore.YELLOW}")
        print()
        
        if " " in username:
            x = username.split()

            for ic in x:
                if ic.isalpha():
                    c += 1
                else:
                    c += 0


            if c == len(x):
                print(f"{Fore.GREEN} Welcome aboard, {username.upper()}! What are we looking for today?")
                return username
            else:
                print(f"{Fore.RED}Beep! Beep! Looks like you've entered your name incorrectly. Kindly do not use any symbols or numbers in your username.")
                continue
            
        else:
            x = username
            if x.isalpha():
                print(f"{Fore.GREEN} Welcome aboard, {username.upper()}! What are we looking for today?")
                return username
            else:
                print(f"{Fore.RED}Hmm... Looks like you've entered your name incorrectly. Kindly do not use any symbols or numbers in your username.")
                continue

# FUNCTION 2: Help -> showing features
def help():
    print(f"{Fore.GREEN}What I can do? {Fore.RESET}")
    print("1. Suggest you travel spots!")
    print("2. Offer packing tips!")
    print("3. Provie weather informations for places!")
    print("4. Get you the latest news reports for the places!")
    print("5. Show the local time in different cities!")
    print("6. Even tell you a joke (travel-related)!")
    print()
    print(f"Press {Fore.RED}'bye'{Fore.RESET} or {Fore.RED}'exit'{Fore.RESET} to end.")

# FUNCTION 3: Recommendations 
def recommend(p):
    if "something else" in p or "some other place" in p or "a different place" in p:
        print()
        nex = normalize_input(input("Alright! Beaches, Mountains or other cities? "))

        if nex in destinations:
            suggestion = random.choice(destinations[p])
            print(f"Do you like {suggestion}? (Yes or No)")

            ans = normalize_input(input())

            if ans == "yes":
                print(f"Wonderful! Would you like to know about some local weather updates in {suggestion}? ")
                local_updates = input(">> ")

                if "yes" in local_updates or "sure" in local_updates:
                    weather_info()
                elif local_updates == "no thanks":
                    print(f"Alright, do enjoy your research and a possible holiday in {suggestion}!")
                    help()
                    return suggestion
                else:
                    print("Error!")

            elif ans == "no":
                print("No worries! Let's try another one!")
                recommend()

        else:
            print("Please say Yes or No! Response not considered.")

    elif p in destinations["trending destinations"]:
        if 



    else:
        print("Sorry! I don't have that destination.")

# FUNCTION 4: Packing Tips
def packing_tips():
    print(f"Travel Bot:", end = "") 
    place = normalize_input(input("Where to? "))
    time = normalize_input(input("How many days? "))

    print(f"Packing tips for {time} days in the location {place}")

    print("1. Check the weather forecast.")
    print("2. Pack versatile clothes.")
    print("3. Bring chargers.")

# FUNCTION 5: Jokes
def joke():
    print(f"Travel Bot:", end = "") 
    print(f"{random.choice(jokes)}")

# FUNCTION 6: Normalisation of text
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# FUNCTION 7: Weather Information
def weather_info(inf):

    if inf == "bali":
        print("Bali: Warm and tropical year-round (around 27°C-30°C). Dry season is April to October; wet season is November to March.")
    elif inf == "maldives":
        print("Maldives: Hot and sunny with temperatures averaging 30°C. Best visited between November and April.")
    elif inf == "phuket":
        print("Phuket: Tropical climate averaging 32°C. Monsoon season runs from May to October, while November to April is dry and sunny.")

    elif inf == "swiss alps":
        print("Swiss Alps: Cold and snowy in winter (perfect for skiing), mild and pleasant in summer (ideal for hiking).")
    elif inf == "rocky mountains":
        print("Rocky Mountains: Unpredictable alpine weather. Expect heavy snow in winter and cool, breezy summers with afternoon thunderstorms.")
    elif inf == "himalayas":
        print("Himalayas: Extreme alpine climate. Freezing temperatures and heavy snow at high altitudes, with monsoon rains in the foothills from July to September.")
    
    elif inf == "tokyo":
        print("Tokyo: Four distinct seasons. Beautiful cherry blossoms in spring, hot/humid summers, mild autumns, and cold, dry winters.")
    elif inf == "paris":
        print("Paris: Maritime climate. Mild springs, warm summers, chilly autumns, and cold (but rarely freezing) winters with occasional rain.")
    elif inf == "newyork":
        print("New York: Humid continental climate. Hot, humid summers and cold, snowy winters. Spring and autumn are mild and crisp.")
    else:
        print("Unexpected error! Kindly type the name of the destination/place.")

# FUNCTION 8: Local Time
def local_time():
    now = datetime.now()
    print("Your current local time and date is = ", now)

# FUNCTION 9: Local News Report
def local_news_report():
    lin = normalize_input(input("Which place's news report would you like to see? "))

    # --- Tropical Beaches ---
    if lin == "bali":
        print("\n=== BALI DAILY NEWS ===")
        print("1. [ENVIRONMENT] Sudden policy shift forces local landfills to reject organic waste, causing major garbage cleanup efforts.")
        print("2. [TOURISM] Post-pandemic visitor counts hit an all-time record, straining freshwater resources in the southern belt.")
        print("3. [ECONOMY] Island infrastructure struggle sparks a fresh debate on capping rapid villa and beach club development.")
    
    elif lin == "maldives":
        print("\n=== MALDIVES TODAY ===")
        print("1. [COMMUNITY] Maldives mourns loss of a brave local military rescue diver during a deep-sea recovery mission.")
        print("2. [MARITIME] Tourism Ministry temporarily suspends cruise ship operating license pending a safety investigation.")
        print("3. [CLIMATE] Global marine researchers wrap up their official scientific mission tracking local coral reef biodiversity.")
        
    elif lin == "phuket":
        print("\n=== PHUKET EXPRESS ===")
        print("1. [CRIME] High-profile international weapons suspect arrested in high-stakes joint operation by Thai police.")
        print("2. [REGULATION] Government initiates a major crackdown on illegal commercial land encroachment around Freedom Beach.")
        print("3. [HEALTH] Authorities investigate a mysterious incident after several international tourists collapse at a beachside cafe.")

    # --- Mountains ---
    elif lin == "swissalps":
        print("\n=== ALPINE CHRONICLE ===")
        print("1. [CLIMATE] Swiss glacier retreat speeds up, prompting scientists to demand a massive shift in local conservation policy.")
        print("2. [SPORTS] Record-breaking winter ski season draws to a close as luxury resorts transition into summer hiking hubs.")
        print("3. [INFRASTRUCTURE] Multimillion-dollar upgrade announced for historic mountain railways to handle high-altitude summer crowds.")
        
    elif lin == "rockymountains":
        print("\n=== ROCKY MOUNTAIN POST ===")
        print("1. [WILDLIFE] Conservationists celebrate a massive milestone as regional gray wolf populations stabilize.")
        print("2. [SAFETY] National Park service issues an early wildfire threat warning ahead of an unseasonably dry, hot summer.")
        print("3. [ADVENTURE] Elite mountaineer sets a blazing new speed record across the rugged Continental Divide trail.")
        
    elif lin == "himalayas":
        print("\n=== HIMALAYAN RECORD ===")
        print("1. [EXPEDITION] Chaos on Everest: Massive traffic jams near the summit spark fresh international calls for stricter climbing permits.")
        print("2. [ECO-NEWS] Himalayan village implements an innovative plastic waste-to-currency recycling initiative.")
        print("3. [GEOLOGY] Seismic tracking stations get an advanced, high-tech upgrade to better detect glacial lake outburst floods.")

    # --- Major Cities ---
    elif lin == "tokyo":
        print("\n=== TOKYO METROPOLITAN ===")
        print("1. [SPORTS] 15-year-old gymnastics prodigy Nishiyama Misa clinches a stunning victory to secure an Asian Games ticket.")
        print("2. [ATHLETICS] Track and field superstar Noah Lyles takes center stage at Tokyo's highly anticipated Golden Grand Prix.")
        print("3. [TECH] Local transportation giant rolls out autonomous AI-powered taxi fleets across major downtown districts.")
        
    elif lin == "paris":
        print("\n=== LE JOURNAL DE PARIS ===")
        print("1. [POLITICS] Historic municipal shift as Socialist leader Emmanuel Grégoire is officially elected the new Mayor of Paris.")
        print("2. [HEALTH] Medical teams at Bourget airport mobilize to isolate a suspected rare viral outbreak from an arriving cruise ship.")
        print("3. [SPORTS] The NFL officially schedules its highly anticipated international regular-season debut game in Paris.")
        
    elif lin == "newyork":
        print("\n=== NEW YORK CHRONICLE ===")
        print("1. [CULTURE] Broadway experiences a massive box-office renaissance following an unprecedented sweep of original musical openings.")
        print("2. [HOUSING] City Council passes a historic, landmark tenant protection bill after a lengthy, tense legislative battle.")
        print("3. [TRANSIT] MTA unveils a multi-billion dollar expansion project aimed at modernizing the aging outer-borough subway lines.")

    # --- Error Handling ---
    else:
        print("Unexpected error! Kindly type the name of the destination/place.")


# MAIN FUNCTION: CHATBOT WORKING
def chatbot():
    print(f"{Fore.LIGHTMAGENTA_EX}Welcome aboard on TravoBot! - Your destination for tips on travels, packing, weather and much more!")
    final_name = valid_name()
    print()
    time.sleep(2)
    help()

    while True:
        userinput = input(">>  ")
        convo_history.append(userinput)

        user_input = normalize_input(userinput)

        if 'recommend' in user_input or 'suggest' in user_input:
            print("                        TRENDING DESTINATIONS OF TODAY!")
            print("Singapore  |  Bangkok  |  Tokyo  |  Paris  |  Kuala Lumpur  |  London  |  Phuket")
            p = normalize_input(input("Which place would you like to explore today? The trending ones, or something special?! "))

            recommend(p)
        
        elif 'tips' in user_input or 'packing' in user_input:
            packing_tips()

        elif 'joke' in user_input:
            joke()

        elif 'help' in user_input:
            help()

        elif 'weather' in user_input:
            inf = normalize_input(input("Which place's weather would you like to know about? "))

            weather_info(inf)
        
        elif 'time' or 'localtime' in user_input:
            local_time()

        elif 'news' or 'report' in user_input:
            local_news_report()

        elif 'print' in user_input:
            print(convo_history)

        elif "exit" in user_input:
            print("Alright! It's been great talking to you!")
            x = input("Would you like to save your conversation history? ").lower()

            if "yes" in x:
                filename = f"TravoBot_ChatHistory_{final_name}.txt"

                f = open(filename, 'w')
                f.write(convo_history)

        else:
            print("Unexpected input! Try again.")


if __name__ == "__main__":
    chatbot()