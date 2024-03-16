import random

def get_user_choice():
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input in ['rock', 'paper', 'scissors', 'q']:
            return user_input
        print("Please choose among 'Rock', 'Paper', 'Scissors', or 'Q' to quit.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You won!'
    else:
        return 'You lost!'

def main():
    user_wins = 0
    computer_wins = 0
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            print("Bye")
            break

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == 'You won!':
            user_wins += 1
        elif result == 'You lost!':
            computer_wins += 1

    print(f"You won {user_wins} times.")
    print(f"The computer won {computer_wins} times.")

if __name__ == "__main__":
    main()
