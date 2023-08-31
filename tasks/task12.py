# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in 
# from a user. Assume that the user would not enter any two 
# numbers which are the same.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the last number: "))

if num1 > num2 and num1 > num3 and num1> num4:
    islarge= "The largest number is: "+ str(num1)
elif num2 > num1 and num2>num3 and num2>num4:
    islarge= "The largest number is: "+ str(num2)
elif num3 >num1 and num3> num2 and num3>num4:
    islarge= "The largest number is: "+ str(num3)
else:
    islarge= "The largest number is: "+ str(num4)

print(islarge)