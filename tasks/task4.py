# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from 
# terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email = input("Enter email: ")


if email.find("@")>0 and (len(email) - email.find(".") > 1):
    if (email.index(".") - email.index("@")) > 1 :
        print("Valid email")
    else:
        print("Invalid")
else:
    print("Invalid email")


