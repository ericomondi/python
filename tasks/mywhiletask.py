# Imagine you have a list employees containing
# dictionaries with keys "name", "hours_worked",
# and "hourly_rate". Write a code snippet using nested
# if statements to calculate the salary for an employee
#  named "Alice" based on her hours worked and hourly rate.

employees = [
    {"name": "Alice", "hrs_wrkd": 36, "hrly_rate": 300},
    {"name": "Albert", "hrs_wrkd": 26, "hrly_rate": 300},
    {"name": "Alex", "hrs_wrkd": 46, "hrly_rate": 300},
    {"name": "Eric", "hrs_wrkd": 72, "hrly_rate": 300}
]
# Calculate Alice's salary

for i in range(0, len(employees)):
    if employees[i]["name"] == "Alice":
        salary = employees[i]["hrs_wrkd"] * employees[i]["hrly_rate"]
        print("Alice's net salary is: " + str(salary))


# Print the salary from all the employees

for i in range(0, len(employees)):
    salary = employees[i]["hrs_wrkd"] * employees[i]["hrly_rate"]
    print(employees[i]["name"] + " salary is: " + str(salary))


# 5.Given a list prices containing prices of products,
# write a code snippet using if statements to check if any
#  product's price is within the range $20 to $50 using the
# logical and operator.

price = [10,20,45,56,24,21,45,34,32]

for x in range(0,len(price)):
    if price[x] > 20 and price[x] <50:
        print(str(price[x])+ " is within the range")
    else:
        print(str(price[x])+" is not within the range")
