class Vehicle:
    def __init__(self, brand , model ):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model  ,  engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

# creating Object

car1 = Car("Toyata" , "fortuner" , 7)
print(car1.brand ,  car1.model , car1.seats)

bike1 = Bike("hero" , "xtreme" , 160)
print(bike1.brand, bike1.model , bike1.engine_cc)