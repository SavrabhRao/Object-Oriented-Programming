class employee:
    def __init__(self , name , salary , position):
        self.name = name
        self.salary = salary
        self.position = position
   
    def GetSalary(self):
        print(f"salary of {self.name} is {self.salary} ")

class teamlead:
    def __init__(self , name , salary , position):
        self.name = name
        self.salary = salary
        self.position = position
   
    def GetSalary(self):
        print(f"salary of {self.name} is {self.salary} ")

class srmanager:
    def __init__(self , name , salary , position):
        self.name = name
        self.salary = salary
        self.position = position
   
    def GetSalary(self):
        print(f"salary of {self.name} is {self.salary} ")

class increment:
    def __init__(self,obj , amount):
        obj.salary = obj.salary + amount
    
    def NewSalary(self,obj):
        print("new salary is: ",obj.salary)


emp1 = employee("sautabh" , 10000 , "junior devloper")
tl = teamlead("maitry" , 40000 , "tl")

inc1 = increment(emp1 , 5000)
inc1.NewSalary(emp1)

inc2 = increment(tl , 5000)
inc2.NewSalary(tl)