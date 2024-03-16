# just a fun project..can't be implemented in production

pwd = input("What is the master password? ")





while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == 'q':
        print("Bye!")
        quit()
        
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Sorry, You have to choose either add or view, try again")
