# create a class employee wuth the attribute of name , age , salary, designation
# and do updation in salary

class Employee:

    def __init__(self,name,age,salary,designation="Beginner"):

        self.Name = name
        self.Age = age
        self.Salary = salary
        self.Designation = designation
        print("employee object is created")

    def update_salary(self,NewSalary):

        self.Salary += NewSalary
        # self.Salary = self.Salary + NewSalary
        print(f"Congrats your salary is updated by {NewSalary}")

    def update_designation(self,NewDesignation):
        self.Designation = NewDesignation
        print(f"You are promoted to {NewDesignation}")
    
    def Employee_Info(self):
        print(f"Emp name is {self.Name} and salary is {self.Salary}")


l = []
n = int(input("how many employees you want to hire: "))

for i in range(n):

    name = input("Enter the name: ")
    age = int(input("Enter your age: "))
    Salary = eval(input("Enter your salary: "))

    emp = Employee(name,age,Salary)
    l.append(emp)

def DiaplayEmployees():
    for i in l:
        i.Employee_Info()

DiaplayEmployees()