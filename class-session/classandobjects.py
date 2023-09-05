class Person():
    name=""
    gender = ""
    email=""
    phone= ""
    details = []
    # constructor - A special method
    # used to instantiate initial a values
    def __init__(self, n, g, e, p):
        self.name = n
        self.gender = g
        self.email = e   
        self.phone = p 
        self.add()

    def add(self):
        self.details.append(self.name)
        self.details.append(self.gender)
        self.details.append(self.email)
        self.details.append(self.phone)

p1 = Person(input("Enter name: "),
            input("Enter gender: "),
            input("enter email: "),
            input("enter phone: "))
# p1.add()
print(p1.details)


        
