from sys import getsizeof

dow_tuple = days = ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
dow_list = days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(getsizeof(dow_list))
print(getsizeof(dow_tuple))

mytup = (45)
print(type(mytup))