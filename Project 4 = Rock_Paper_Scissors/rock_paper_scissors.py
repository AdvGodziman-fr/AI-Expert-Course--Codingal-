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

player_moves = []

def pattern_check():
    print("AI is deciding it's move", end=" ")

    for l in range(1,4): 
        print('.', end="")
        time.sleep(1)

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

        print("                AI has decided. Please wait for a few seconds...")
        print()
        time.sleep(3)
        roll()

        print(ai_move)

        return ai_move

    else: 
        ai_move = random.choice(possible_moves)
        print("                AI has decided. Please wait for a few seconds...")
        print()
        time.sleep(3)
        roll()

        print(ai_move)
        
        return ai_move

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
    print()
    print("RULES OF THE GAME")
    print("1. Please type the complete name of your move, with the first letter in capital (eg. 'Rock', instead of 'rock' or 'roc')")
    print("2. Do not add multiple moves into the prompt. Decide on 1 move and type it in correctly!")
    print("3. ")
    print()
    print("Type ")
    time.sleep(2)



def main_game():
    print("Welcome to 'Rock, Paper, Scissors!'")
    username = input("Please enter your name to continue: ")

    if username == "" or username == " ":
        print()
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
            player_moves.append(player_choice.capitalize())

            time.sleep(1)
            pattern_check()
            time.sleep(2)

            win_check(player_choice, ai_move)
            print()
            ask = input("Do you wanna play again? ")

            if 'yes' in ask or 'ya' in ask or 'sure' in ask or 'alright' in ask:
                continue
            else:
                break


        elif 'no' in i or 'nah' in i or 'nope' in i:
            print("Oh! It's sad to see this end up so soon!")
            chance_2 = input("Do you really wanna leave so soon? ")

            if 'yes' in chance_2 or 'ya' in chance_2 or 'sure' in chance_2 or 'alright' in chance_2:
                print()

            elif 'no' in chance_2 or 'nah' in chance_2 or 'nope' in chance_2:
                print("Do feel free to play in anytime you're free!")
                break

        else:
            print("Error!")


if __name__ == "__main__":
    main_game()  
