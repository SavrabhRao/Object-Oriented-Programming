# method overloading
# metod overriding
# operator overloading

# poly = multiple
# morph = forms  

# method overloadind 
# in method overloading inside the same class we use the same method with same name
# for multiple times with different number of arguments
## in python method method overloading is not supported

class test:
    
    def __init__(self):
        print("object is created ")
    def m1(self):
        print("instance method")
    def m1(self,a):
        print("method with single argument")
    def m1(self,a,*b):
        print("method with different argument: ")

t = test()
t.m1()
# error m1 needs 3 argumenys passed 1