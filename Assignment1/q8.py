m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
avg = total / 5

print("Total marks:", total)
print("Average:", avg)

if avg >= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
elif avg >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
