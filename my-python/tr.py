command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("start the car")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("car stoped")
    elif command == "help":
       print("""
start - To start the car
stop - to stop the car
quit -To quit
             """)
    elif command == quit:
        break
    else:
        print("Sorry i dont understand this")