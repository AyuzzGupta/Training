inventory = ["Python Basics", "Data Science", "Web Development", "Machine Learning", "Java Programming"]

print("Books in inventory:")
for book in inventory:
    print("-", book)

search = input("\nEnter book name to search: ")

found = False
for book in inventory:
    if book.lower() == search.lower():
        found = True
        break

if found:
    print("Yes! The book is available.")
else:
    print("Sorry, the book is not available.")
