# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user 
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” ,
# if so then print  “Login is Successful” and if not print “Invalid username or
#  password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

sav_pass = "Admin@123"
sav_username = "admin@mail.com"

for tries in range(1,4):
    password = input("Enter password: ")
    username = input("Enter username: ")
    if tries == 3:
        print("Account is blocked")
        break
    elif password == sav_pass and username == sav_username:
        print("Login Succesfull")
        
    else:
        print("Invalid username or password, try again!")
