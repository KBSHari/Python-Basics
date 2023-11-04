"""Create a Class Person , Two Objects by taking (name, age, address)
Input from users and print details in the end."""

class Person:
    Name=None
    Age=None
    Address=None

    def deatils(self):
        print(self.Name,self.Age,self.Address)




HP=Person()

HP.Name=input("Enter your name:\n")
HP.Age=input("Enter your age:\n")
HP.Address=input("Enter your address:\n")

HP.deatils()
