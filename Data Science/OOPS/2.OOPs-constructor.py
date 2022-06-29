class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def show_emp_details(self):
        print("Name of Employee :",self.name)
        print("Age of Employee :",self.age)
        print("Salary of Employee :",self.salary)
        print("Gender of Employee :",self.gender)
        
        
e1 = Employee('shubham',21,23456,'male')
e1.show_emp_details()