name = input("Type your name: ")

print(f"Welcome {name} to this adventure!")


answer = input(f"{name} you are on a dirt road, it has come to an end and you can go left or right, which way you want to go? ").lower()

if answer == 'left':
    answer = input(f"You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer == 'walk':
        print(f"")
    else:
        print('')
    
elif answer == 'right':
    print('hi')
    
else:
    print(f"Invalid option {name}, You lost!")