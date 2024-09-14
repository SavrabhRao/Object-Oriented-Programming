# Access modifiers 

# Public
# Private
# Protected

# Public    :- these variables or methods are accessible everywhere 

# Protected :- These are the variables and methods which can be accessible either inside 
# class itself or inside the child class but cant access outside the class 
# but in python its not implemented on language level so you can access protected 
# variables in python like public variables only
# protected are declared by using _varname syntax

# protected variables
class Parent:
    def __init__(self,a):
        self._var1 = a
    def m2(self):
        print(self._var1)

class Child(Parent):
    def m3(self):
        print(self._var1)

c = Child(10)
c.m3()
print(''' this is the loop hole here we can access protected variable 
outside class with obj ''',c._var1)