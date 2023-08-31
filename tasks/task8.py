# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. Otherwise,
# for every 5 km/s above the speed limit (70), it should give the 
# driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#  If the driver gets more than 12 points, the function should print: “License suspended”.

car_speed = int(input("Enter the car's speed in km/h: "))

if car_speed <= 70:
    print("OK")
else:
    demerit_points = (car_speed-70) / 5
    if demerit_points <= 12:
        print("Demerit points: " + str(demerit_points))
    else:
        print("License suspended")

