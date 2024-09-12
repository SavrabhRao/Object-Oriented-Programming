# Class methods are not bounded with the instance of the class in python They are accessed
# Using classname.methodname
# They are defined using decorator 
# First argument in a class method is always cls
# Class method is also called as a factory method
# We can access all the static variables inside class method and also modify them but 
# we can not access any instance variable in class method or modify them

class test:
    count = 0
    def __init__(self):
        test.count = test.count + 1
    
    @classmethod
    def getcount(cls):
        return cls.count

res = test.getcount()
print(f"number of objects created are: {res}")

t = test()
res = test.getcount()
print(f"number of objects created are: {res}")

u = test()
res = test.getcount()
print(f"number of objects created are: {res}")

v = test()
res = test.getcount()
print(f"number of objects created are: {res}")

w = test()
res = test.getcount()
print(f"number of objects created are: {res}")