days = ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Find wwednesday using an index
print(days[2])

# Using a function find the length of the tuple
print(len(days))

# Replace thursaday with Thur
dayslist =list(days)
dayslist[3] = "Thur"
daystuple = tuple(dayslist)
print(daystuple)

# Check if its still a tuple
print(type(daystuple))

