# Types :
'''
1.Simple Inheritance
2.Multiple Inheritance
3.Multi-level Inheritance
4.Hybrid Inheritance
'''

'''
Multiple Inheritance - the child inherits from more than 1 parent class
'''

class Parent1:
    def assign_string_one(self,str1):
        self.str1 = str1
        
    def show_string_one(self):
        print(self.str1)
        
class Parent2:
    def assign_string_two(self,str2):
        self.str2 = str2
        
    def show_string_two(self):
        print(self.str2)
        

class Derive(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3 = str3
        
    def show_string_three(self):
        print(self.str3)
        
c = Derive()
c.assign_string_one("I'm String of Parent One")
c.assign_string_two("I'm String of Parent Two")
c.assign_string_three("I'm String of child ")

c.show_string_one()
c.show_string_two()
c.show_string_three()