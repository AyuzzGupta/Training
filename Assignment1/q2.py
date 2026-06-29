attendance = float(input("Enter attendance percentage: "))
rating = int(input("Enter performance rating (1-10): "))

if attendance >= 90 and rating >= 8:
    print("Employee is eligible for bonus!")
else:
    print("Employee is not eligible for bonus.")
