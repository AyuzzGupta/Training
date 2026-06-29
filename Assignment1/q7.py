a = float(input("Enter first sales figure: "))
b = float(input("Enter second sales figure: "))
c = float(input("Enter third sales figure: "))

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

print("Largest sales figure is:", biggest)
