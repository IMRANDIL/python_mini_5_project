import random

user_wins = 0
computer_wins = 0
choices = ['Rock', 'Paper', 'Scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("Bye")
        quit()
    computer_choice = choices[random.randint(0, len(choices))].lower()
    if user_input in choices:
        if user_input == 'Rock'.lower() and computer_choice == 'Paper'.lower():
            print('You won!')
            user_wins += 1
            continue
        if user_input == 'Scissors'.lower() and computer_choice == 'Paper'.lower():
            print('You won!')
            user_wins += 1
            continue
        
        
        
        
    
    
    else:
        print("Please choose amongst 'Rock' or 'Paper' or 'Scissors'")
        continue
    
       
    
    
    
    