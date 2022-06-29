'''
Multi-level - We have Parent, child,grand-child relationship
'''

class Parent:
    def get_name(self,name):
        self.name = name
        
    def show_name(self):
        print(self.name)
        
class Child(Parent):
    def get_age(self,age):
        self.age=age
    
    def show_age(self):
        print(self.age)
        
class GrandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
        
    def show_gender(self):
        print(self.gender)
        

g = GrandChild()

print("Multilvel Inheritance \n")
g.get_gender('Male')
g.show_gender()

g.get_age(21)
g.show_age()

g.get_name("Grand Child")
g.show_name()

'''
c = Child()

c.get_age(45)
c.show_age()

c.get_name("Child")
c.show_name()

p = Parent()

p.get_name("Parent")
p.show_name()
'''