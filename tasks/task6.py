# Write a program input a password. 
# Give them only 4 attempts to check the
# passwords entered against “admin@123”. 
# If the password is correct access is granted.
# After you show them a message , the account is blocked.

s_pass = "admin@123"

for i in range(1,5):
    password = input("Enter password: ")
    if i == 4:
        print("The account is blocked")
        break
    elif password == s_pass:
        print("Access granted")
        break
    else:
        print("Try again")