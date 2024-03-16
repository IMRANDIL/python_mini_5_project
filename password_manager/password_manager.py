# just a fun project..can't be implemented in production

master_pwd = input("What is the master password? ")



def view():
    with open('passwds.txt', 'r') as f:
        for line in f.readline:
            print(line)




def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open('passwds.txt', 'a') as f:
        f.write(f"{name} | {password}")

    print("Added in the file :)")





while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == 'q':
        print("Bye!")
        quit()
        
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Sorry, You have to choose either add or view, try again")
        continue
