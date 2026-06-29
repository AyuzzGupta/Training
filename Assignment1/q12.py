books = ["Math", "Science", "English", "History", "Art"]
due_dates = [5, -2, 3, -7, 0]

overdue = 0

for i in range(len(books)):
    if due_dates[i] < 0:
        print(books[i], "is overdue by", abs(due_dates[i]), "days")
        overdue = overdue + 1

print("\nTotal overdue books:", overdue)
