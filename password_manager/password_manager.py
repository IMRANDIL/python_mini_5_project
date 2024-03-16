# just a fun project..can't be implemented in production
# used third party module ----> cryptography
from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)


write_key()
'''

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() +  master_pwd.encode()

fer = Fernet(key)



def view():
    with open('passwds.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print(f"user: {user}, password: {fer.decrypt(passw.encode())}")




def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open('passwds.txt', 'a') as f:
        f.write(f"{name} | {fer.encrypt(password.encode()).decode()}\n")

    print("Added in the file :)")




def main():  
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


if __name__ == "__main__":
    main()