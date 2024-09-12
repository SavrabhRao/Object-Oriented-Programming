# create a class employee wuth the attribute of name , age , salary, designation
# and do updation in salary

class Employee:

    company_name = "saurabh solutions"

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

name = input("Enter the name: ")
age = int(input("Enter your age: "))
Salary = eval(input("Enter your salary: "))

e1 = Employee(name,age,Salary)
print(e1.__dict__)
e1.update_designation("PMO")
print(e1.__dict__)

