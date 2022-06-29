# With Inheritance one class can derive the properties of another class

# 1.Simple Inheritance

class Vehicle:
    def __init__(self,milage,cost):
        self.milage = milage           
        self.cost = cost
        
    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Milage of Vehicle is ",self.milage)
        print("Cost of Vehicle is ",self.cost)
        
        
v1 = Vehicle(69, 56789)
v1.show_vehicle_details()
    
    
class Car(Vehicle):
    def show_car_details(self):
        print("I am a Car")
        
c = Car(78, 56789)
print("\nDetails using Inheritance :\n")
c.show_vehicle_details()

c.show_car_details()

