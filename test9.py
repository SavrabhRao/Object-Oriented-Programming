class test:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def set_variables(self,x,y,z):
        self.a = x
        self.b = y
        self.c = z

t = test(10,20,30)
print(t.__dict__)

# to update instance variables 
# 1] inside class use instance method --> Setter Method
# 2] outside class using curent object reference variable

t.set_variables(70,80,90)
print(t.__dict__)

t.a = 110
print(t.__dict__)