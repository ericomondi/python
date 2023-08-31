# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal.
#  Validates the phone number by checking if it starts with +254.. 
# or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

ph_num = input("Enter phone number: ")

if len(ph_num) == 12 and ph_num.index("254") == 0:
    num= "+" + ph_num
    
elif len(ph_num)== 10 and ph_num.index("07") == 0:
    num = "+254" + ph_num[1:]
elif  len(ph_num) == 9 and ph_num.index("7") == 0:
    num = "+254" + ph_num   
else:
    print("Invalid number")

print(num)