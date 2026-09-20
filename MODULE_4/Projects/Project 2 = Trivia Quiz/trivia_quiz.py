import requests
from threading import Timer
import html
import random
import os

API_URL = "https://opentdb.com/api.php?amount=5&type=multiple"

# Global flag to signal if time ran out
time_up = False

def fetcher():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            if data['response_code'] == 0 and data['results']:
                return data['results']
    except Exception:
        pass
    return None

def rules():
    print("===========================================================")
    print("🚨 QUIZ RULES & GUIDELINES 🚨")
    print()
    print("• Speed Matters: You have exactly 10 seconds per question.")
    print("• Format: Pick numbers 1, 2, 3, or 4 and press Enter.")
    print("• No Pauses: If the timer hits zero, you get 0 points!")
    print("===========================================================")
    print()


def times_up_handler():
    global time_up
    time_up = True
    print()
    print("Time's up! Press ENTER to continue...")

def workflow():
    global time_up
    score = 0
    questions = fetcher()

    if not questions:
        print("Failed to fetch questions. Please check your connection.")
        return

    print("Welcome to Trivia Quiz, where you test your intellectual presence!")
    rules()
    
    username = input("Enter your username: ")
    if not username:
        print("Username not identified.")
        return

    for qno, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrect = [html.unescape(a) for a in q['incorrect_answers']]

        options = incorrect + [correct]
        random.shuffle(options)

        print(f"\nQuestion {qno}: {question}")
        print("Options: ")
        for ind, j in enumerate(options, 1):
            print(f"{ind}. {j}")

        # Reset flag and start a 10-second background timer
        time_up = False
        my_timer = Timer(10.0, times_up_handler)
        my_timer.start()

        # Get user input on the main thread
        choice = None
        while not time_up:
            try:
                user_input = input("Your answer (1-4): ")
                
                # If timer fired while waiting for input
                if time_up:
                    break
                    
                choice = int(user_input)
                if 1 <= choice <= 4:
                    break
                else:
                    print("Invalid choice! Enter 1 - 4.")

            except ValueError:
                if time_up:
                    break
                print("Please enter a valid number.")

        # Cancel the timer immediately if they answered in time
        my_timer.cancel()

        if time_up:
            print(f"Too slow! The correct answer was: {correct}")
            print()
            continue

        # Check answer
        if options[choice-1] == correct:
            print("Correct Answer!")
            score += 1
        else:
            print(f"Incorrect Answer! The correct answer was: {correct}")
        print()

    # Final Summary (Moved outside the loop)
    print("=== FINAL RESULTS ===")
    print("Final Score: ", score)
    print("Number of questions: ", len(questions))
    print(f"Correct percentage: {((score/len(questions))*100):.2f}%")

if __name__ == "__main__":
    workflow()
