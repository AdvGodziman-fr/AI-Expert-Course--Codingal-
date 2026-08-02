# Trivia API 
import requests
import random
import html

API_URL = "https://opentdb.com/api.php?amount=6&category=18&type=multiple"


def fetch_questions():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        #print(data)

        # 0 => Success, 1 => No Results
        if data['response_code'] == 0 and data['results']:
            return data['results']
        
    return None


def main():
    questions = fetch_questions()

    if not questions:
        print("Error! Failed to fetch questions from API.")
        exit()

    score = 0

    print("Welcome to the Quiz Game!\n")

    for qno, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrect = [html.unescape(a) for a in q['incorrect_answers']]

        options = incorrect + [correct]
        random.shuffle(options)

        #Display the Question Text
        print(f"Question {qno}: {question}")
        print()
        print("Options: ")

        for ind, j in enumerate(options, 1):
            print(ind, j.capitalize())

        while True:
            choice = int(input("Your answer (1, 4): "))
            if 1 <= choice <= 4:
                break

            print("Invalid choice! Enter 1 - 4.")

        if options[choice-1] == correct:
            print("Correct Answer!")
            score += 1
            print()

        else:
            print("Incorrect Answer!")
            print()


    print("Final Score: ", score)
    print("Number of questions: ", len(questions))
    print(f"Correct percentage: {((score/len(questions))*100):.2f}%")


if __name__ == "__main__":
    main()