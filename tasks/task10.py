# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company 
# from the array/list below if we know that the stock is the last 
# digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

prods = [["omo", "30ksh", "300"],["milk","50ksh","200"],["bread","45ksh", "359"],["coffe","5ksh", "79"]]
total = 0
for i in range(0, len(prods)):
    stock = int(prods[i][-1])
    total = total + stock 
    print(total)