# for loops

for i in range(0, 100):
    if i % 2 == 0:
        print(i)

# while loops
i = 0
while i < 30:
    print("less " + str(i))
    i += 1


# a for loop to print from 1-5
for i in range(1,6):
    print(i)

# sum all the elements in a list using for loop

numbers = [2,3,4,5,6,7,8,9]
total = 0
for i in range(0,len(numbers)):
   total =total + numbers[i]
   print(total)

# Sum the sum of all the elements in range 0-90

# 99% of loops will be used to acces values insidea list/tuple

# store first 10 odd numbers btn 0 and 50

odd_num = []

for i in range(0,51):
    if i % 2 != 0:
        odd_num.append(i)
        if len(odd_num)==10:
            break
    else:
        pass
print(odd_num)




    