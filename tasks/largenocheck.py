x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
z = int(input("enter the last number: "))

if x > y and x > z:
    print("X-"+str(x) + " is the largest number")
elif y > x and y > z:
    print("Y-" + str(y) + " is the largest number")
else:
    print("X-" + str(z) + " is the largest number")
