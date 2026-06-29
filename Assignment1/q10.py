menu = ["Burger", "Pizza", "Pasta", "Fries", "Coffee"]

while True:
    print("\n--- Food Menu ---")
    for i in range(len(menu)):
        print(i + 1, "-", menu[i])
    print(len(menu) + 1, "- Exit")

    choice = int(input("Enter your choice: "))

    if choice == len(menu) + 1:
        print("Thank you! Visit again.")
        break
    elif choice >= 1 and choice <= len(menu):
        print("You selected:", menu[choice - 1])
    else:
        print("Invalid choice. Try again.")
