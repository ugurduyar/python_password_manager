pwd = input("What is the master password?")

def add():
    pass
def view():
    pass

while True:
    mode = input("type add for add a new password or type view for view a password").lower()
    if mode == "add":
        view()
    elif mode == "view":
        view()
    else:
        print("Invalid Input")
        continue