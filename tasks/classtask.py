# Given a variable temperature with a value of 25°C,
#  write an if statement to check if the temperature is
# above 30°C using the greater than (>) operator.

temp = 25

if temp > 30:
    print("Tempraturere greater than thirty")
else:
    print("Temprature is less than thirty")


# Create a dictionary called stock with items
#  as keys and their quantities as values.
# Write an if-else statement to check if the
# quantity of "apples" is zero using the equality (==) operator.

stock = {"bananas": 100, "apples": 0, "carrots": 45}

if stock["apples"] == 0:
    print("Apples are out of stock")
else:
    print("Apples are in stock")

# Suppose you have a tuple point representing (x, y)
# coordinates. Write an if-elif-else statement to
# determine whether the point lies on the x-axis (y == 0)
# or y-axis (x == 0), or if it's in the origin (both x and y are 0).

cord = (0, 0)

if cord[0] != 0 and cord[1] == 0:
    print("It lies on the x-axis")
elif cord[1] != 0 and cord[0] == 0:
    print("Lies on the y-axis")
else:
    print("Lies in both x and y axis")

# 5.Given a list prices containing prices of products,
# write a code snippet using if statements to check if any
#  product's price is within the range $20 to $50 using the
# logical and operator.

# price = [20, 30, 40]

# if price > 20 and mylist[:] < 50:
#     print("There are prices within the range")
# else:
#     print("No price within the range")

# Imagine you have a list employees containing
# dictionaries with keys "name", "hours_worked",
# and "hourly_rate". Write a code snippet using nested
# if statements to calculate the salary for an employee
#  named "Alice" based on her hours worked and hourly rate.

employees = [
    {"name": "Alice", "hrs_wrkd": 36, "hrly_rate": 300},
    {"name": "Albert", "hrs_wrkd": 26, "hrly_rate": 300},
    {"name": "Alex", "hrs_wrkd": 46, "hrly_rate": 300},
]

if employees[0]["name"] == "Alice":
    print("Alice exists")
else:
    print("Alice doesnt exist")


# Create a dictionary book_ratings with book titles
# as keys and their ratings as values. Write an if-elif-else
# statement to find out if a book "The Adventure" has a
#  rating of 5 or is rated below 2.

book_rat = {"adventure": 5, "comedy": 5, "action": 3.5}

if book_rat["adventure"] == 5:
    print("Has five star rating")
elif book_rat["adventure"] < 2:
    print("Rated below two")
else:
    print("Between a rating of 2 and 5")


# 9.Suppose you have two sets: set_x and set_y.
#  Write a code snippet using conditional statements
# to check if the symmetric difference between the two
#  sets is not empty, using the ^ (symmetric difference) operator


set_x = {"apple", "banana", "mango"}
set_y = {"apple", "banana", "mango"}

if set_x ^ set_y:
    print("Its empty")
else:
    print("It's not empty")
