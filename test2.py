class student:
    "this is student class created by saurabh"
    def __init__(self): 
        print("student object is created")
        self._name = "saurabh"
        self.rollno = 136
        self.age = 21

    def talk(self):
        print("takl method is called")
        print(f"my name is {self._name}")
        print(f"my roll number is {self.rollno}")
        print(f"my age is {self.age}")

class fresher(student):
    def info(self):
        print(f"name is {self._name}")
        print(f"rol no is {self.rollno}")
        print(f"age is {self.age}")

# encapsulation
s = student()
f = fresher()
f.info()
print(type(s))