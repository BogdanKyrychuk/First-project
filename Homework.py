class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f"Марка: {self.make} \nМодель: {self.model}")
class Car(Vehicle):
    def drive(self):
        print(f"Автомобіль {self.make} {self.model} їде дорогою.")
class Motorcycle(Vehicle):
    def drive(self):
        print(f"Мотоцикл {self.make} {self.model} їде трасою.")
class Bicycle(Vehicle):
    def drive(self):
        print(f"Велосипед {self.make} {self.model} їде стежкою.")

car = Car("Ford", "Fiesta")
motorcycle = Motorcycle("Suzuki", "Hayabusa")
bicycle = Bicycle("Giant", "BMX")

car.display_info()
car.drive()