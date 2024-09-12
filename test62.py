# a+b+c
class Number():
    def __init__(self,num): # operator overriding
        self.num = num
    def __add__(self,other): # operator overriding
        return Number(self.num + other.num)
    def __str__(self): # method overriding
        return f"{self.num}"

a = Number(10)
b = Number(20)
c = Number(70)

d = a+b+c
print(d)
