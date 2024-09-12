# accessing the methods of the parent class inside child class 

class parent:
    def m1(self):
        print("this is m1 of parent")
    def m2(self):
        print("--------inside m2--------")
        self.m1()

p = parent()
p.m1()
p.m2()

