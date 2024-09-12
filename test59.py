
# operator overloading
 
''' operator overloading is the programming technique that allows devlopers to
redefine the behaviour of oprators when working with the user defined datatypes 
or class in other words oprator overloading enables to spacify how the operator work in 
your userdefined datatype or objects '''

class Number():
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num
    

a = Number(10)
b = Number(20)
# print(a.num)
# print(b.num)

print(a+b)
# self represent the object before the + oprator 
# and other represent the object after + oprator

    