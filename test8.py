class Exam:
    def __init__(self,name,dob,marks):
        self.name = name
        self.BirthDate = dob
        self.Marks = marks
    
    def Result(self,res):
        self.result = res
        if self.Marks >= 35:
            print("pass")
        else:
            print("fail")
    
    def info(self):  #getter method 
        print(f"Hello my name is {self.name}")
        print(f"My Date of birth is {self.BirthDate}")
        print(f"my marks are {self.Marks} ")


s1 = Exam("saurabh","2 aug",99)
s1.info()

# tommrow -- > how to update instance variable
# and setter methods
# where to access the instance variables 