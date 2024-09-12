class students:
    a = 10
    def __init__(self,name,rollno):
        print(f"new student object is created {rollno}")
        self.name = name
        self.rollno = rollno
        name1 = name
    def talk(self):
        print(f"name is {self.name}")
        print(f"rollno is {self.rollno}")



saurabh = students("saurabh",51)
saurabh.talk()

vishal = students("vishal",37)
vishal.talk()

eesha = students("eesha",62)
eesha.talk()

eesha.name