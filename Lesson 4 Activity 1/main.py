import random
from colorama import init, Fore, Style
init(autoreset=True)
# =========================================
# CONSTANTS (DO NOT EDIT)
# =========================================
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def display_board(board):
    """Prints the Tic-Tac-Toe board in color."""
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    """Asks player to choose X or O and returns (player_symbol, ai_symbol)."""
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).strip().upper()
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

# ==========================================================
# TODO 1: player_move(board, symbol)
# ==========================================================
def player_move(board, symbol):
    # TODO: Ask for a move (1-9), validate empty spot, then place symbol
    move = -1
    while move not in range(1, 10) or not board[move -1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))

            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")

        except ValueError:
            print("Please enter a number between 1 and 9")

    board[move -1] = symbol

# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):
    # TODO A: Try to win in 1 move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol

            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
            
    # TODO B: Try to block player win in 1 move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol

            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return

    # TODO C: Else, pick a random empty spot
    possible_moves = [i for i in range(9) if board[i].isdigit()]

    move = random.choice(possible_moves)

    board[move] = ai_symbol
    

# ==========================================================
# TODO 3: check_win(board, symbol)
# ==========================================================
def check_win(board, symbol):
    # TODO: Loop through WIN_COMBOS and return True if symbol wins
    for condition in win_conditions:
        if symbol == board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return True
    return False

# ==========================================================
# TODO 4: check_full(board)
# ==========================================================
def check_full(board):
    # TODO: Return True if board has no digits left (all filled)
    return all(not spot.isdigit() for spot in board)

# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    # Ask player's name in green and store it
    # Hint: if empty, default to "Player"
    name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    if not name:
        name = 'Player'

    while True:
        # TODO (MAIN-2): Initialize the board as ["1","2",...,"9"]
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # TODO (MAIN-3): Get symbols using player_choice()
        player_symbol, ai_symbol = player_choice()

        # TODO (MAIN-4): Decide who starts ("Player" or "AI")
        # Simple option: always start with Player
        turn = name
        game_on = True

        while game_on:
            display_board(board)

            if turn == name:
                # TODO (MAIN-5): Call player_move() to place player's symbol
                player_move(board, player_symbol)

                # TODO (MAIN-6): If player wins, print win message with name and break
                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"Congratulations, you have won {name}")
                    game_on = False

                # TODO (MAIN-7): If tie (board full), print tie message and break
                # if check_full(...):
                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    game_on = False

                else:
                # TODO (MAIN-8): Switch turn to "AI"
                    turn = "AI"

            else:
                # TODO (MAIN-9): Call ai_move() to place AI symbol
                ai_move(board, ai_symbol, player_symbol)

                # TODO (MAIN-10): If AI wins, print AI win message and break
                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"AI has won!")
                    game_on = False

                # TODO (MAIN-11): If tie (board full), print tie message and break
                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    game_on = False

                # TODO (MAIN-12): Switch turn to "Player"
                else:
                    turn = name

        # TODO (MAIN-13): Ask "Play again? (yes/no): "
        # If answer is NOT "yes", print thank you and return
        again = input("Do you want to play again? ").lower()

        if "no" in again():
            break

if __name__ == "__main__":
    tic_tac_toe()