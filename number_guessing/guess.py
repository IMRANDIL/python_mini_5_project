import random

top_of_range = input("Type a number range: ")

attempts_no = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
    
random_number = random.randint(0, top_of_range)


while True:
    guessing_number = input('Please guess a number between the range (press "q" to exit) ')
    if guessing_number == 'q':
        print('Bye')
        quit()
    if guessing_number.isdigit():
        if int(guessing_number) > top_of_range:
            print(f"Please guess a number within the range '0' to '{top_of_range}' you provided earlier")
            continue
        attempts_no += 1
        if int(guessing_number) > random_number:
            print(f"The number is greater, try again")
            continue
        if int(guessing_number) < random_number:
            print(f"The number is lower, try again")
            continue
        
        if random_number == int(guessing_number):
            print("You got it")
            break
        else:
            continue
    else:
        print('Please type a number next time.')
        continue
    
    
print(f"You got it in {attempts_no} {'attempts' if attempts_no > 1 else 'attempt'}.")
    