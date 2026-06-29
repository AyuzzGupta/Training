n=6
last =6
for i in range (0,n+1):
    if i%3==0:
        print("  ",end="")
    else:
        print("*",end="")
print()
for i in range(0,n+1):
    if i%3==0:
        print("*",end="")
    else:
        print("  ",end="")
print()
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (n - i) - 1):
        if j == 0 or j == 2 * (n - i) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
 