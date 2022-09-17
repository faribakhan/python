class vehicle:
    """Base/parent class for vehicles"""

    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving ", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning ", self.name, " to ", direction)
    def brake(self):
        print(self.name, " is stopping!!")
class Car(vehicle):
    """Car class"""
    def __init__(self,name,manufacturer,color,year):
        super().__init__(name,manufacturer,color)
        self.year=year
        self.wheel=4
        print("A new car has been created. Name: ", self.name)
        print("This car was built in ", self.year)
    def change_gear(self,gear_name):
        """Method for gear changing"""
        print(self.name," is changing gear to ",gear_name)
    def turn(self, direction):
        print("Turning ", self.name, " to ", direction)

if __name__ == "__main__":
    v1 = vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Car("Daneen the best", "Fariba", "Pink","2017")
    v3 = Car("Mustang 5.0 GT Coupe", "Ford","Red","2017")

    v1.drive()
    v2.drive()
    v3.drive()

    v3.turn("left")
    v2.turn("right")

    v3.brake()
    v3.change_gear("d")