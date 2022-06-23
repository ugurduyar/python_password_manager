from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username={} Password={}".format(user,passw))

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("type add for add a new password or type view for view a password ").lower()
    if mode == "quit":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Input")
        continue