from loadJson import require_json

# Usage example
quiz_data = require_json('quiz_data.json')
score_count = 0
print("Let's Play the Quiz")
for quest_data in quiz_data:
    quest_answer = input(f'{quest_data['Question']} ').lower()
    if(quest_answer == quest_data['Answer'].lower()):
        score_count += quest_data['Points']
    else:
        continue

print(f'You Scored {score_count}.\nThank You')

# print(quiz_data)

# print(len(quiz_data))