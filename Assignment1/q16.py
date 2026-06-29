marks = []
n = int(input("Enter number of students: "))

for i in range(n):
    m = float(input("Enter marks of student " + str(i + 1) + ": "))
    marks.append(m)

total = 0
for m in marks:
    total = total + m

avg = total / len(marks)

print("All marks:", marks)
print("Average marks:", avg)
