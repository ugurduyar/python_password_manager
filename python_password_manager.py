master_pwd = input("What is the master password? ")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            print(line)

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