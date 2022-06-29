#Overriding Init Method

class Vehicle:
    def __init__(self,milage,cost):
        self.milage = milage           
        self.cost = cost
        
    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Milage of Vehicle is ",self.milage)
        print("Cost of Vehicle is ",self.cost)
        
        
v1 = Vehicle(69, 56789)
    
class Car(Vehicle):
    def __init__(self, milage, cost,tyres,hp):
        super().__init__(milage,cost)
        self.tyres = tyres
        self.hp = hp
        
    def show_car_details(self):
        print("I am a Car")
        print("No of Tyres in Car ",self.tyres)
        print("Horse Power of Car ",self.hp)
        
        
c1 = Car(90, 56789,6,999)
c1.show_vehicle_details()

c1.show_car_details()
