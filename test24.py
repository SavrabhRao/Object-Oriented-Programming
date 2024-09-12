class Manager:
    def __init__(self , name , salary , position):
        self.name = name
        self.salary = salary
        self.position = position
   
    def GetSalary(self):
        print(f"salary of {self.name} is {self.salary} ")

class Teamlead:
    def __init__(self , name , salary , position):
        self.name = name
        self.salary = salary 
        self.position = position
   
    def GetSalary(self):
        print(f"salary of {self.name} is {self.salary} ")

class devloper:
    def __init__(self , name , salary , position):
        self.name = name
        self.salary = salary
        self.position = position
   
    def GetSalary(self):
        print(f"salary of {self.name} is {self.salary} ")

class Promotion:

    @staticmethod
    def Post(obj,new_designation):
        obj.position = new_designation

    @staticmethod
    def IncSalary(obj,amount):
        obj.salary = obj.salary + amount


julie = Manager("Julie",20000,"Manager")
maitri = Teamlead("Maitri",40000,"Teaml Lead")
neha = devloper("Neha",70000,"SQL-Python devloper")

Promotion.Post(julie,"CEO")
print(julie.position)
Promotion.IncSalary(julie,3000000)
julie.GetSalary()


Promotion.Post(neha,"Architect")
print(neha.position)
Promotion.IncSalary(neha,30000)
neha.GetSalary()