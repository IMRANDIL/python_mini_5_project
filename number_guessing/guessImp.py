import random

def get_valid_range():
    while True:
        top_of_range = input("Type a number for the range (type 'q' to quit): ")
        if top_of_range.lower() == 'q':
            print("Bye")
            quit()
        if top_of_range.isdigit() and int(top_of_range) > 0:
            return int(top_of_range)
        print("Please enter a valid positive number.")

def get_guess(top_of_range):
    while True:
        guessing_number = input(f'Guess a number between 0 and {top_of_range} (type "q" to quit): ')
        if guessing_number.lower() == 'q':
            print('Bye')
            quit()
        if guessing_number.isdigit() and 0 <= int(guessing_number) <= top_of_range:
            return int(guessing_number)
        print(f"Please enter a valid number between 0 and {top_of_range}.")

def main():
    top_of_range = get_valid_range()
    random_number = random.randint(0, top_of_range)
    attempts_no = 0

    while True:
        attempts_no += 1
        guess = get_guess(top_of_range)
        if guess > random_number:
            print("The number is lower. Try again.")
        elif guess < random_number:
            print("The number is higher. Try again.")
        else:
            print("You got it!")
            break

    print(f"You got it in {attempts_no} {'attempts' if attempts_no > 1 else 'attempt'}.")

if __name__ == "__main__":
    main()
