limit = float(input("Enter speed limit: "))
speed = float(input("Enter vehicle speed: "))

if speed > limit:
    print("Vehicle exceeded the speed limit!")
else:
    print("Vehicle is within the speed limit.")
