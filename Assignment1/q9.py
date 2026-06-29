saved_user = "admin"
saved_pass = "1234"
tries = 0

while tries < 3:
    user = input("Enter username: ")
    pas = input("Enter password: ")

    if user == saved_user and pas == saved_pass:
        print("Login successful!")
        break
    else:
        tries = tries + 1
        print("Wrong credentials. Attempts left:", 3 - tries)

if tries == 3:
    print("Account locked. Too many failed attempts.")
