my_ds = [23, "Jane", (560),["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]

print(my_ds)

# Print KES
print(my_ds[3][2]["currency"])

# Print 560
print(my_ds[2])

# print Maths
print(my_ds[3][1])

# In the dictiuonary with the key currency
#  add another key "amount" with the value "90"

my_ds[3][2]["amount"]= "90"
print(my_ds)

# Reverse 987 to 789 without using an inbulit-method
# or assigning it manually


edit = my_ds[4]
editrev = str(edit)[::-1]
editint = int(editrev)
my_ds[4] = editint

print(my_ds)




# Changing the name "John" to "Jane"
my_ds[1]= "John"
print(my_ds)



