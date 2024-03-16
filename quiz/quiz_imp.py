from loadJson import require_json
import random

# Load quiz data
quiz_data = require_json('quiz_data.json')

def ask_question(question_data):
    user_answer = input(f'{question_data["Question"]} ').strip().lower()
    if user_answer == question_data['Answer'].lower():
        print("Correct!")
        return question_data['Points']
    else:
        print(f"Wrong! The correct answer is: {question_data['Answer']}")
        return 0

def play_quiz(questions, shuffle=True):
    score = 0
    if shuffle:
        random.shuffle(questions)
    print("Let's Play the Quiz")
    for question_data in questions:
        score += ask_question(question_data)
    return score

# Play the quiz
total_score = play_quiz(quiz_data)
print(f'You Scored {total_score}.\nThank You')
