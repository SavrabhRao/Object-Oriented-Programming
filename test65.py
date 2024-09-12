# performing the addition multiplication and division between two objects of 
# datatype Doremon
# even after printing the object we should get the value of that object 
# and type should be Doremon

class Doremon(object):
    def __init__(self,n):
        self.num = n
    def __str__(self):
        return f"{self.num}"
    def __add__(self,other):
        return Doremon(self.num * other.num)

d = Doremon(10)
e = Doremon(20)
f = Doremon(50)
s = d+e+f
print(s)
print(type(s))

