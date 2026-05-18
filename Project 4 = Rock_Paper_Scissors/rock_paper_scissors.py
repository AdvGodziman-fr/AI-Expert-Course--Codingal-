import random
from colorama import init, Fore, Style
import time 

init(autoreset=True)

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



def win_check(move1, move2):
    if (move1, move2) in winning_combos_player:
        print("Aw shucks! You win this one!")
    elif (move1, move2) in winning_combos_ai:
        print("Well, looks like you lost!")
    elif (move1, move2) in tie_combo:
        print("Oh! It's a tie!")
    else:
        print("Error detected! Please re-run the program")



def roll():
    print("ROCK...        ", end = " ")
    time.sleep(2)
    print("PAPER...        ", end = " ")
    time.sleep(2)
    print("SCISSORS...        ", end = " ")
    time.sleep(2)
    print("SHOOT!")



def rules():
    print("RULES OF THE GAME")
    print("1. ")
    print("2. ")
    print("3. ")
    time.sleep(2)



def main_game():
    print("Welcome to 'Rock, Paper, Scissors!'")
    username = input("Please enter your name to continue: ")

    if username == "" or username == " ":
        print("Alright! Your name is 'Player 1'.")
    else:
        print(f"Alrighty! Welcome to the game, {username}!")

    # Rules of the Game
    rules()

    while True:
        i = input("Are you ready for the game? ").lower()

        if 'yes' in i or 'ya' in i or 'sure' in i or 'alright' in i:
            print("LET'S GET THIS SHOW ON THE ROAD!")
            print()
            print("What would be your move? Rock, Paper or Scissors? 'FYI: AI cannot have access to your move before the game! Your privacy is secured (for now)!'")
            player_choice = input(">> ")

            time.sleep(1)
            print("AI is deciding it's move", end="")
            ai_move = random.choice(possible_moves)

            for l in range(1,4):
                m = '.' * l
                print(m, end="")
                time.sleep(1)


            print("AI has decided. Please wait for a few seconds...")
            print()
            time.sleep(3)
            roll()
            print(ai_move)

            time.sleep(2)

            win_check(player_choice, ai_move)
            print()
            ask = input("Do you wanna play again?")

            if 'yes' in i or 'ya' in i or 'sure' in i or 'alright' in i:
                continue
            else:
                break


        elif 'no' in i or 'nah' in i or 'nope' in i:
            print("Oh! It's sad to see this end up so soon!")
            print("Do feel free to play in anytime you're free!")
            break




    
