name = input("Type your name: ")

print(f"Welcome {name} to this adventure!")


answer = input(f"{name} you are on a dirt road, it has come to an end and you can go left or right, which way you want to go? ").lower()

if answer == 'left':
    answer = input(f"You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer == 'walk':
        print(f"You walked for many miles, ran out of water and you lost the game.")
    elif answer == 'swim':
        print(f"You swam across and were eaten by an alligator.")
    else:
        print(f"{name}, Invalid option, You lost!")
    
elif answer == 'right':
    answer = input(f"You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print(f"You go back to the main road. Now you can decide to derive forward or backward, You lost!")
    elif answer == 'cross':
        answer = input(f"You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == 'yes':
            print(f"{name}, You passed the puzzle and talked to the stranger and the stranger gives you ton of gold, enjoy!")
        elif answer == 'no':
            print(f"You chose to no, the stranger got offended and cursed you, you lost now!")
        else:
            print(f"{name}, Invalid option, You lost!")
    else:
        print(f"{name}, Invalid option, You lost!")
    
else:
    print(f"Invalid option {name}, You lost!")