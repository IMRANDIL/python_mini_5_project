import random

user_wins = 0
computer_wins = 0
choices = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("Bye")
        break
    computer_choice = choices[random.randint(0, len(choices)-1)].lower()
    print('computer choice>>>>>>>>>>>>>>>', computer_choice)
    if user_input in choices:
        if user_input == 'Rock'.lower() and computer_choice == 'Paper'.lower():
            print('You won!')
            user_wins += 1
            continue
        elif user_input == 'Rock'.lower() and computer_choice == 'Scissors'.lower():
            print('You won!')
            user_wins += 1
            continue
        elif user_input == 'Rock'.lower() and computer_choice == 'Rock'.lower():
            print("It's a tie!")
            continue
        
        else:
            print('You lost!')
            computer_wins += 1
            continue
           
    else:
        print("Please choose amongst 'Rock' or 'Paper' or 'Scissors'")
        continue
       
    
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")