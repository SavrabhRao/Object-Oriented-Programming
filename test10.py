class test:

    def __init__(self,a = 0 , b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c

    def set_variables(self,x,y,z):
        self.a = x
        self.b = y
        self.c = z

    def getter(self):
        print(self.a)
        print(self.b)
        print(self.c)
    
t = test()
print(t.__dict__)

t = test(50,60,70)
print(t.__dict__)

t.set_variables(20,30,40)
print(t.__dict__)

t.getter()

# what is encapsulation --> combination of methods and data in a single class is
# called encapsulation 
# Encapsulation is just implementation of a class with property and beghaviours