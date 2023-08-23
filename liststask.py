trainees = ["John", [2,["James", "Mary"]]]

# Display 2 using index, from the list
print(trainees[1][0])

# Output James using index from the list
print(trainees[1][1][0])

# Using a method add 56 at the end of the list
trainees.append(56)
print(trainees)

# Using a method add the name mike between James and Mary
trainees[1][1].insert(1, "Mike")
print(trainees)

# Change the value of 2 to 8
trainees[1][0] = 8
print(trainees)

# Remove John and Mary from the list
trainees.remove("John")
trainees.remove("Mary")

# Using a function, determione the lenght of this list
print(len(trainees))



