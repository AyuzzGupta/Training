saved_user = "admin"
saved_pass = "1234"

user = input("Enter username: ")
pas = input("Enter password: ")

if user == saved_user and pas == saved_pass:
    print("Login successful!")
else:
    print("Invalid username or password.")
