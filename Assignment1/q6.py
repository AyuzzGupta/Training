age = int(input("Enter your age: "))

if age <= 12:
    print("Category: Child")
    print("Ticket price: 100")
elif age <= 59:
    print("Category: Adult")
    print("Ticket price: 250")
else:
    print("Category: Senior Citizen")
    print("Ticket price: 150")
