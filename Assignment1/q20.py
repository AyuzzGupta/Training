records = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    records[roll] = {"name": name, "marks": marks}

print("\n--- Student Records ---")
for roll in records:
    print("Roll No:", roll)
    print("Name:", records[roll]["name"])
    print("Marks:", records[roll]["marks"])
    print()

search = input("Enter roll number to search: ")
if search in records:
    print("Found:", records[search]["name"], "- Marks:", records[search]["marks"])
else:
    print("Student not found.")
