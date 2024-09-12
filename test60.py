
class Number():
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num * other.num
        
a = Number(10)
b = Number(20)
print(a+b)

# when i will write print(a+b) it will call the __add__ method then 
# self will represent the a object and other to b
# and then it will perform the given operation between them 
# this how we can perform the oprator oveloading