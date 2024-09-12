class student:
    "this is student class created by saurabh"
    def __init__(self):
        print("object is created") 
        print(id(self))
        self.name = "saurabh"
        self.rollno = 136
        self.age = 21

    def talk(self):
        print(f"my name is {self.name}")
        print(f"my roll number is {self.rollno}")
        print(f"my age is {self.age}")

s = student()
print(id(s))
print()
s1 = student()
print(id(s1))