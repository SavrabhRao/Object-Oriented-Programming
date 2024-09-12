class Student:
    def __init__(self,marks,rollnumber):
        self.marks = marks
        self.rollnumber = rollnumber
    def __str__(self):
        return f"marks are : {self.marks}\nroll number is : {self.rollnumber}"

s = Student(10,51)
print(Student(1000,400))
