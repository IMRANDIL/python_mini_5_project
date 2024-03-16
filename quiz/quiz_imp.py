from loadJson import require_json
import random

# Load quiz data
quiz_data = require_json('quiz_data.json')

total_score = 'Zero Point'

def ask_question(question_data, score):
    user_answer = input(f'{question_data["Question"]} (press {'q'} to quit) ').strip().lower()
    if user_answer == 'q':
        print(f'You Scored {score}.\nThank You')
        quit() # exits the program simply
    if user_answer == question_data['Answer'].lower():
        print("Correct!")
        score += question_data['Points']
    else:
        print(f"Wrong! The correct answer is: {question_data['Answer']}")
    return score




def play_quiz(questions, shuffle=True):
    score = 0
    if shuffle:
        random.shuffle(questions)
    print("Let's Play the Quiz")
    for question_data in questions:
        score = ask_question(question_data, score)
    return score


# Play the quiz
total_score = play_quiz(quiz_data)

print(f'You Scored {total_score}.\nThank You')




