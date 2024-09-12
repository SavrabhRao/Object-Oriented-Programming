# accessing the methods of the parent class inside child class 
class parent:
    def m1(self):
        print("this is the m1 of PARENT")

class child(parent):
    def m1(self):
        print("child class")
        super().m1()

c = child()
c.m1()