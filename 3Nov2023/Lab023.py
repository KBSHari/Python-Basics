#Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods


class Car:
    Brand="TATA"
    Model=2023
    Colour="Black"
    Seat=5
    Gear=6

    def brand(self):
        print("Your car brand: ",self.Brand)
    def model(self):
        print("Your card model: ",self.Model)
    def colour(self):
        print("Your car colour: ",self.Colour)
    def seat(self):
        print("Your seat capacity: ",self.Seat)
    def gear(self):
        print("Total number of gear: ",self.Gear)



H_car=Car()
H_car.brand()
H_car.model()
H_car.colour()
H_car.seat()
H_car.gear()


B_car=Car()

B_car.Brand="Hyundai"
B_car.Model=2022
B_car.Colour="white"
B_car.Seat=8
B_car.Gear=5


B_car.brand()
B_car.model()
B_car.colour()
B_car.seat()
B_car.gear()



