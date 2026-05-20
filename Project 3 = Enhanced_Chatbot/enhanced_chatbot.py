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
    "cities": ["Tokyo", "Paris", "New York"], 
    "trending destinations": ["singapore", "bangkok", "tokyo", "paris", "kuala lumpur", "london", "phuket"] 
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
                print(f"{Fore.GREEN} Welcome aboard, {Fore.YELLOW}{username.upper()}{Fore.GREEN}! What are we looking for today?")
                return username
            else:
                print(f"{Fore.RED}Beep! Beep! Looks like you've entered your name incorrectly. Kindly do not use any symbols or numbers in your username.")
                continue
            
        else:
            x = username
            if x.isalpha():
                print(f"{Fore.GREEN} Welcome aboard, {Fore.YELLOW}{username.upper()}{Fore.GREEN}! What are we looking for today?")
                return username
            else:
                print(f"{Fore.RED}Hmm... Looks like you've entered your name incorrectly. Kindly do not use any symbols or numbers in your username.")
                continue

# FUNCTION 2: Help -> showing features
def help():
    print(f"{Fore.GREEN}{Style.BRIGHT}What I can do? {Fore.RESET}")
    print(f"{Fore.CYAN}1. Suggest you travel spots!")
    print(f"{Fore.CYAN}2. Offer packing tips!")
    print(f"{Fore.CYAN}3. Provide weather information for places!")
    print(f"{Fore.CYAN}4. Get you the latest news reports for the places!")
    print(f"{Fore.CYAN}5. Show the local time in different cities!")
    print(f"{Fore.CYAN}6. Even tell you a joke (travel-related)!")
    print()
    print(f"Press {Fore.RED}'bye'{Fore.RESET} or {Fore.RED}'exit'{Fore.RESET} to end.")

# FUNCTION 3: Recommendations 
def recommend(p):
    if "something else" in p or "some other place" in p or "a different place" in p or p in ["beaches", "mountains", "cities"]:
        print()
        if p in ["beaches", "mountains", "cities"]:
            category = p
        else:
            category = normalize_input(input(f"{Fore.CYAN}Alright! Beaches, Mountains or cities? {Fore.YELLOW}"))

        if category in destinations and destinations[category]:
            suggestion = random.choice(destinations[category])
            print(f"{Fore.GREEN}Do you like {Fore.YELLOW}{suggestion}{Fore.GREEN}? (Yes or No)")

            ans = normalize_input(input())

            if ans == "yes":
                print(f"{Fore.GREEN}Wonderful! Would you like to know about some local weather updates in {Fore.YELLOW}{suggestion}{Fore.GREEN}? ")
                local_updates = normalize_input(input(">> "))

                if "yes" in local_updates or "sure" in local_updates:
                    weather_info(normalize_input(suggestion))
                elif local_updates == "no" or "no thanks" in local_updates:
                    print(f"{Fore.CYAN}Alright, do enjoy your research and a possible holiday in {suggestion}!")
                    help()
                    return suggestion
                else:
                    print(f"{Fore.RED}Error!")

            elif ans == "no":
                print(f"{Fore.LIGHTBLACK_EX}No worries! Let's try another one!")
                recommend(category)

        else:
            print(f"{Fore.RED}Please choose a valid destination type next time! Response not considered.")

    elif p in destinations["trending destinations"]:
        print(f"{Fore.GREEN}Excellent choice! {Fore.YELLOW}{p.capitalize()}{Fore.GREEN} is highly trending right now.")
        print(f"{Fore.GREEN}Would you like to know about local {Fore.CYAN}weather{Fore.GREEN} updates or recent {Fore.CYAN}news{Fore.GREEN} updates for {p.capitalize()}?")
        trending_ans = normalize_input(input(">> "))
        
        if "weather" in trending_ans:
            weather_info(p)
        elif "news" in trending_ans or "report" in trending_ans:
            print(f"\n{Fore.LIGHTBLACK_EX}Fetching news for {p.capitalize()}...")
            global forced_news_dest
            forced_news_dest = p
            local_news_report(auto=True)
        else:
            print(f"{Fore.GREEN}Sounds good! Keep {Fore.YELLOW}{p.capitalize()}{Fore.GREEN} on your bucket list!")

    else:
        print(f"{Fore.RED}Sorry! I don't have that destination.")

# FUNCTION 4: Packing Tips
def packing_tips():
    print(f"{Fore.MAGENTA}Travel Bot: {Style.RESET_ALL}", end = "") 
    place = normalize_input(input("Where to? "))
    days = normalize_input(input("How many days? "))

    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Packing tips for {days} days in the location {place.capitalize()}:")
    print(f"{Fore.CYAN}1. Check the weather forecast.")
    print(f"{Fore.CYAN}2. Pack versatile clothes.")
    print(f"{Fore.CYAN}3. Bring chargers.")

# FUNCTION 5: Jokes
def joke():
    print(f"{Fore.MAGENTA}Travel Bot: {Fore.YELLOW}{random.choice(jokes)}")

# FUNCTION 6: Normalisation of text
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# FUNCTION 7: Weather Information
def weather_info(inf):
    inf = normalize_input(inf).replace(" ", "")

    print(f"\n{Fore.YELLOW}=== WEATHER REPORT ===")
    if inf == "bali":
        print(f"{Fore.CYAN}Bali: Warm and tropical year-round (around 27°C-30°C). Dry season is April to October; wet season is November to March.")
    elif inf == "maldives":
        print(f"{Fore.CYAN}Maldives: Hot and sunny with temperatures averaging 30°C. Best visited between November and April.")
    elif inf == "phuket":
        print(f"{Fore.CYAN}Phuket: Tropical climate averaging 32°C. Monsoon season runs from May to October, while November to April is dry and sunny.")
    elif inf == "swissalps":
        print(f"{Fore.CYAN}Swiss Alps: Cold and snowy in winter (perfect for skiing), mild and pleasant in summer (ideal for hiking).")
    elif inf == "rockymountains":
        print(f"{Fore.CYAN}Rocky Mountains: Unpredictable alpine weather. Expect heavy snow in winter and cool, breezy summers with afternoon thunderstorms.")
    elif inf == "himalayas":
        print(f"{Fore.CYAN}Himalayas: Extreme alpine climate. Freezing temperatures and heavy snow at high altitudes, with monsoon rains in the foothills from July to September.")
    elif inf == "tokyo":
        print(f"{Fore.CYAN}Tokyo: Four distinct seasons. Beautiful cherry blossoms in spring, hot/humid summers, mild autumns, and cold, dry winters.")
    elif inf == "paris":
        print(f"{Fore.CYAN}Paris: Maritime climate. Mild springs, warm summers, chilly autumns, and cold (but rarely freezing) winters with occasional rain.")
    elif inf == "newyork":
        print(f"{Fore.CYAN}New York: Humid continental climate. Hot, humid summers and cold, snowy winters. Spring and autumn are mild and crisp.")
    else:
        print(f"{Fore.RED}Unexpected error! Kindly type the name of the destination/place.")

# FUNCTION 8: Local Time
def local_time():
    now = datetime.now()
    print(f"{Fore.GREEN}Your current local time and date is = {Fore.YELLOW}{now.strftime('%Y-%m-%d %H:%M:%S')}")

# Global handle for fallback redirection automation
forced_news_dest = None

# FUNCTION 9: Local News Report
def local_news_report(auto=False):
    global forced_news_dest
    if auto and forced_news_dest:
        lin = normalize_input(forced_news_dest).replace(" ", "")
        forced_news_dest = None
    else:
        lin = normalize_input(input(f"{Fore.CYAN}Which place's news report would you like to see? {Fore.YELLOW}")).replace(" ", "")

    # --- Tropical Beaches ---
    if lin == "bali":
        print(f"\n{Fore.RED}=== BALI DAILY NEWS ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [ENVIRONMENT] Sudden policy shift forces local landfills to reject organic waste, causing major garbage cleanup efforts.")
        print(f"{Fore.LIGHTBLACK_EX}2. [TOURISM] Post-pandemic visitor counts hit an all-time record, straining freshwater resources in the southern belt.")
        print(f"{Fore.LIGHTBLACK_EX}3. [ECONOMY] Island infrastructure struggle sparks a fresh debate on capping rapid villa and beach club development.")
    
    elif lin == "maldives":
        print(f"\n{Fore.RED}=== MALDIVES TODAY ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [COMMUNITY] Maldives mourns loss of a brave local military rescue diver during a deep-sea recovery mission.")
        print(f"{Fore.LIGHTBLACK_EX}2. [MARITIME] Tourism Ministry temporarily suspends cruise ship operating license pending a safety investigation.")
        print(f"{Fore.LIGHTBLACK_EX}3. [CLIMATE] Global marine researchers wrap up their official scientific mission tracking local coral reef biodiversity.")
        
    elif lin == "phuket":
        print(f"\n{Fore.RED}=== PHUKET EXPRESS ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [CRIME] High-profile international weapons suspect arrested in high-stakes joint operation by Thai police.")
        print(f"{Fore.LIGHTBLACK_EX}2. [REGULATION] Government initiates a major crackdown on illegal commercial land encroachment around Freedom Beach.")
        print(f"{Fore.LIGHTBLACK_EX}3. [HEALTH] Authorities investigate a mysterious incident after several international tourists collapse at a beachside cafe.")

    # --- Mountains ---
    elif lin == "swissalps":
        print(f"\n{Fore.RED}=== ALPINE CHRONICLE ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [CLIMATE] Swiss glacier retreat speeds up, prompting scientists to demand a massive shift in local conservation policy.")
        print(f"{Fore.LIGHTBLACK_EX}2. [SPORTS] Record-breaking winter ski season draws to a close as luxury resorts transition into summer hiking hubs.")
        print(f"{Fore.LIGHTBLACK_EX}3. [INFRASTRUCTURE] Multimillion-dollar upgrade announced for historic mountain railways to handle high-altitude summer crowds.")
        
    elif lin == "rockymountains":
        print(f"\n{Fore.RED}=== ROCKY MOUNTAIN POST ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [WILDLIFE] Conservationists celebrate a massive milestone as regional gray wolf populations stabilize.")
        print(f"{Fore.LIGHTBLACK_EX}2. [SAFETY] National Park service issues an early wildfire threat warning ahead of an unseasonably dry, hot summer.")
        print(f"{Fore.LIGHTBLACK_EX}3. [ADVENTURE] Elite mountaineer sets a blazing new speed record across the rugged Continental Divide trail.")
        
    elif lin == "himalayas":
        print(f"\n{Fore.RED}=== HIMALAYAN RECORD ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [EXPEDITION] Chaos on Everest: Massive traffic jams near the summit spark fresh international calls for stricter climbing permits.")
        print(f"{Fore.LIGHTBLACK_EX}2. [ECO-NEWS] Himalayan village implements an innovative plastic waste-to-currency recycling initiative.")
        print(f"{Fore.LIGHTBLACK_EX}3. [GEOLOGY] Seismic tracking stations get an advanced, high-tech upgrade to better detect glacial lake outburst floods.")

    # --- Major Cities ---
    elif lin == "tokyo":
        print(f"\n{Fore.RED}=== TOKYO METROPOLITAN ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [SPORTS] 15-year-old gymnastics prodigy Nishiyama Misa clinches a stunning victory to secure an Asian Games ticket.")
        print(f"{Fore.LIGHTBLACK_EX}2. [ATHLETICS] Track and field superstar Noah Lyles takes center stage at Tokyo's highly anticipated Golden Grand Prix.")
        print(f"{Fore.LIGHTBLACK_EX}3. [TECH] Local transportation giant rolls out autonomous AI-powered taxi fleets across major downtown districts.")
        
    elif lin == "paris":
        print(f"\n{Fore.RED}=== LE JOURNAL DE PARIS ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [POLITICS] Historic municipal shift as Socialist leader Emmanuel Grégoire is officially elected the new Mayor of Paris.")
        print(f"{Fore.LIGHTBLACK_EX}2. [HEALTH] Medical teams at Bourget airport mobilize to isolate a suspected rare viral outbreak from an arriving cruise ship.")
        print(f"{Fore.LIGHTBLACK_EX}3. [SPORTS] The NFL officially schedules its highly anticipated international regular-season debut game in Paris.")
        
    elif lin == "newyork":
        print(f"\n{Fore.RED}=== NEW YORK CHRONICLE ===")
        print(f"{Fore.LIGHTBLACK_EX}1. [CULTURE] Broadway experiences a massive box-office renaissance following an unprecedented sweep of original musical openings.")
        print(f"{Fore.LIGHTBLACK_EX}2. [HOUSING] City Council passes a historic, landmark tenant protection bill after a lengthy, tense legislative battle.")
        print(f"{Fore.LIGHTBLACK_EX}3. [TRANSIT] MTA unveils a multi-billion dollar expansion project aimed at modernizing the aging outer-borough subway lines.")

    # --- Error Handling ---
    else:
        print(f"{Fore.RED}Unexpected error! Kindly type the name of the destination/place.")


# MAIN FUNCTION: CHATBOT WORKING
def chatbot():
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Welcome aboard on TravoBot! - Your destination for tips on travels, packing, weather and much more!")
    final_name = valid_name()
    print()
    time.sleep(2)
    help()

    while True:
        userinput = input(f"\n{Fore.WHITE}>>  ")
        convo_history.append(userinput)

        user_input = normalize_input(userinput)

        if 'recommend' in user_input or 'suggest' in user_input:
            print(f"\n{Fore.MAGENTA}{Style.BRIGHT}                    TRENDING DESTINATIONS OF TODAY!")
            print(f"{Fore.YELLOW}Singapore  |  Bangkok  |  Tokyo  |  Paris  |  Kuala Lumpur  |  London  |  Phuket")
            p = normalize_input(input(f"{Fore.CYAN}Which place would you like to explore today? The trending ones, or something special?! {Fore.YELLOW}"))

            recommend(p)
        
        elif 'tips' in user_input or 'packing' in user_input:
            packing_tips()

        elif 'joke' in user_input:
            joke()

        elif 'help' in user_input:
            help()

        elif 'weather' in user_input:
            inf = normalize_input(input(f"{Fore.CYAN}Which place's weather would you like to know about? {Fore.YELLOW}"))
            weather_info(inf)
        
        elif 'time' in user_input or 'localtime' in user_input:
            local_time()

        elif 'news' in user_input or 'report' in user_input:
            local_news_report()

        elif 'print' in user_input:
            print(f"{Fore.LIGHTBLACK_EX}{convo_history}")

        elif "exit" in user_input or "bye" in user_input:
            print(f"{Fore.CYAN}Alright! It's been great talking to you!")
            x = input(f"{Fore.GREEN}Would you like to save your conversation history? ").lower()

            if "yes" in x:
                filename = f"TravoBot_ChatHistory_{final_name}.txt"
                with open(filename, 'w') as f:
                    for record in convo_history:
                        f.write(f"{record}\n")
                print(f"{Fore.GREEN}History successfully exported to {Fore.YELLOW}{filename}!")
            break 

        else:
            print(f"{Fore.RED}Unexpected input! Try again.")


if __name__ == "__main__":
    chatbot()