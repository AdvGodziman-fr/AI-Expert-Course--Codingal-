from colorama import Fore, Style
from datetime import time

i = 0

def animation_time():
    for i in range(0, 3):
        print(".", end = "")
        time.sleep(1)

def name_check():
    while True:
        username = input(f"{Fore.CYAN}Please enter your name: {Fore.GREEN}").strip()

        print(f"{Fore.RESET}Verifying username", end="")
        animation_time()

        if username.isalpha():
            return username
            
        else:
            print("There has been an error! Please try again!")
            print()
            continue
            

def main_convo():
    print(f"{Fore.LIGHTMAGENTA_EX}Welcome to {Fore.LIGHTGREEN_EX}MOVIE-RECO.com{Fore.LIGHTMAGENTA_EX}, where you can get personalised suggestions regarding movies!{Style.RESET_ALL}")
    print()
    final_name = name_check()

    print(f"{Fore.LIGHTMAGENTA_EX}Greetings, {Fore.LIGHTBLUE_EX}{final_name}{Fore.LIGHTMAGENTA_EX}!{Fore.RESET}")

    


main_convo()
