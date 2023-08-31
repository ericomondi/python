# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables.
# Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third numbe: "))

if num1 > num2 and num1 > num3:
    largest = num1
elif num3> num1 and num3 > num2:
    largest = num3
else:
    largest = num2
print("The largest number is: " + str(largest))