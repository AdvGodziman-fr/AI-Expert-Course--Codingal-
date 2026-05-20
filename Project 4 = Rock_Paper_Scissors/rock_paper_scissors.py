import random
from colorama import init, Fore, Style
import time 

init(autoreset=True)

ai_win = 0
player_win = 0

# LISTS USED
possible_moves = ['Rock', 'Paper', 'Scissors'] 
winning_combos_player = [
    ('Rock','Scissors'),('Paper', 'Rock'),('Scissors', 'Paper')
]

winning_combos_ai = [
    ('Rock', 'Paper'), ('Paper', 'Scissors'), ('Scissors', 'Rock')
]

tie_combo = [
    ('Rock', 'Rock'), ('Paper', 'Paper'), ('Scissors', 'Scissors')
]

player_moves = []

game_history = []

# FUNCTION 1: Checking Pattern in Player moves
def pattern_check():
    print(f"{Fore.CYAN}AI is deciding it's move{Style.RESET_ALL}", end="")

    for l in range(1,4): 
        print(f"{Fore.CYAN}.", end="")
        time.sleep(1)

    print()

    if len(player_moves) > 5:
        rock_count = player_moves.count('Rock')
        paper_count = player_moves.count('Paper')
        scissor_count = player_moves.count('Scissors')

        if rock_count > scissor_count and rock_count > paper_count:
            ai_move = 'Paper'

        elif paper_count > rock_count and paper_count > scissor_count:
            ai_move = 'Scissors'

        elif scissor_count > rock_count and scissor_count > paper_count:
            ai_move = 'Rock'

        print(f"{Fore.CYAN}AI has decided. Please wait for a few seconds{Style.RESET_ALL}", end = "")
        for l in range(1,4): 
            print(f"{Fore.CYAN}.", end="")
            time.sleep(1)

        print()
        time.sleep(3)

        # Calling F3 in F1
        roll()

        print(f"{Fore.YELLOW}{Style.BRIGHT}{ai_move}")
        return ai_move

    else: 
        ai_move = random.choice(possible_moves)
        print(f"{Fore.CYAN}AI has decided. Please wait for a few seconds{Style.RESET_ALL}", end = "")
        for l in range(1,4): 
            print(f"{Fore.CYAN}.", end="")
            time.sleep(1)        
            
        print()
        time.sleep(3)

        # Calling F3 in F1
        roll()

        print(f"{Fore.YELLOW}{Style.BRIGHT}{ai_move}")
        return ai_move


# FUNCTION 2: Checking wins
def win_check(move1, move2):
    ai_wins = 0
    player_wins = 0

    if (move1, move2) in winning_combos_player:
        print(f"{Fore.GREEN}{Style.BRIGHT}Aw shucks! You win this one!")
        player_wins += 1
        result = "Player wins!"
    elif (move1, move2) in winning_combos_ai:
        print(f"{Fore.RED}{Style.BRIGHT}Well, looks like you lost!")
        ai_wins += 1
        result = "AI wins!"
    elif (move1, move2) in tie_combo:
        print(f"{Fore.YELLOW}Oh! It's a tie!")
        result = "Tie!"
    else:
        print(f"{Fore.RED}Error detected! Please re-run the program")

    game_history.append({f"AI Point": ai_wins, "Player Point": player_wins, "Result": result})  
    return ai_wins, player_wins

# FUNCTION 3: Calling "Rock, Paper, Scissors"
def roll():
    print(f"{Fore.RED}ROCK...        {Style.RESET_ALL}", end = " ")
    time.sleep(1)
    print(f"{Fore.YELLOW}PAPER...        {Style.RESET_ALL}", end = " ")
    time.sleep(1)
    print(f"{Fore.GREEN}SCISSORS...        {Style.RESET_ALL}", end = " ")
    time.sleep(1)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}SHOOT!")

#FUNCTION 4: Printing Rules
def rules():
    print()
    print(f"{Fore.BLUE}{Style.BRIGHT}RULES OF THE GAME")
    print(f"{Fore.BLUE}1. Please type the complete name of your move, with the first letter in capital (eg. 'Rock', instead of 'rock' or 'roc')")
    print(f"{Fore.BLUE}2. Do not add multiple moves into the prompt. Decide on 1 move and type it in correctly!")
    print(f"{Fore.BLUE}3. If you want to exit, you can type 'No' when asked if you wanna play again.")
    print()
    time.sleep(2)

# FUNCTION 5: Counting wins
def counting_wins():
    global ai_win, player_win

    for u in game_history:
        if u["AI Point"] == 1:
            ai_win += 1
        elif u["Player Point"] == 1:
            player_win += 1
        else:
            ai_win += 0
            player_win += 0
    
    return ai_win, player_win

# FUNCTION 6: Scoreboard display
def scoreboard(name, p1, p2):
    print(f"{Fore.MAGENTA}{Style.BRIGHT}FINAL SCOREBOARD")
    print(f"{Fore.CYAN}AI Points: {Fore.YELLOW}{p1}{Fore.CYAN}  |  {Fore.GREEN}{name}{Fore.CYAN} Points: {Fore.YELLOW}{p2}")

# FUNCTION 7: Correcting Input
def correct_input():
    putin = True
    while putin:
        player_choice = input(">> ")
        if 'rock' in player_choice.lower() or 'paper' in player_choice.lower() or 'scissors' in player_choice.lower():
            print(f"{Fore.LIGHTBLACK_EX}Processing...")
            print(f"{Fore.GREEN}V", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}a", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}l", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}i", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}d", end="")
            time.sleep(0.1)
            print(" ", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}i", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}n", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}p", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}u", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}t", end="")
            time.sleep(0.1)
            print(f"{Fore.GREEN}!")
            
            return player_choice

        else:
            print(f"{Fore.LIGHTBLACK_EX}Processing...")
            print(f"{Fore.RED}I", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}n", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}v", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}a", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}l", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}i", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}d", end="")
            time.sleep(0.1)
            print(" ", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}i", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}n", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}p", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}u", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}t", end="")
            time.sleep(0.1)
            print(f"{Fore.RED}!")
            print()
            print(f"{Fore.YELLOW}Kindly enter 'Rock', 'Paper' or 'Scissors' please.")
            putin = True


# MAIN FUNCTION: The game flow
def main_game():

    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to 'Rock, Paper, Scissors!'")
    username = input("Please enter your name to continue: ")

    if username == "" or username == " ":
        print()
        print(f"Alright! Your name is '{Fore.YELLOW}Player 1{Style.RESET_ALL}'.")
    else:
        print(f"Alrighty! Welcome to the game, {Fore.GREEN}{username}{Style.RESET_ALL}!")

    # Calling F4
    rules()

    # Initialising variables
    tom = True
    global c

    while tom:
        print(f"{Fore.LIGHTBLACK_EX}-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        i = input("Are you ready for the game? ").lower()

        if 'yes' in i or 'ya' in i or 'sure' in i or 'alright' in i:
            print()
            print(f"What would be your move? {Fore.YELLOW}Rock{Style.RESET_ALL}, {Fore.YELLOW}Paper{Style.RESET_ALL} or {Fore.YELLOW}Scissors{Style.RESET_ALL}? '{Fore.MAGENTA}FYI: AI cannot have access to your move before the game! Your privacy is secured (for now)!{Style.RESET_ALL}'")

            # Calling F6
            player_choice = correct_input()
            print()

            player_moves.append(player_choice.capitalize())
            time.sleep(1)

            # Calling F1
            ai_move = pattern_check()
            time.sleep(2)

            # Calling F2
            win_check(player_choice, ai_move)
            print()

            ask = input("Do you wanna play again? ").lower()

            if 'yes' in ask or 'ya' in ask or 'sure' in ask or 'alright' in ask:
                tom = True
            else:
                print(f"{Fore.CYAN}Alright! Do feel free to play in anytime you're free!")
                print()
                ai_wins, player_wins = counting_wins()

                print(scoreboard(username, ai_wins, player_wins))
                tom = False

                game_history.clear()

        elif 'no' in i or 'nah' in i or 'nope' in i:
            print(f"{Fore.RED}Oh! It's sad to see this end up so soon!")
            chance_2 = input("Do you really wanna leave so soon? ").lower()

            if 'yes' in chance_2 or 'ya' in chance_2 or 'sure' in chance_2 or 'alright' in chance_2:
                print()
                print(f"{Fore.CYAN}Do feel free to play in anytime you're free!")
                tom = False

            elif 'no' in chance_2 or 'nah' in chance_2 or 'nope' in chance_2:
                print()
                tom = True

        else:
            print(f"{Fore.RED}Error!")


if __name__ == "__main__":
    main_game()