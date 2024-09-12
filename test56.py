
# write down method in which we can take 2,3,4 number of arguments and find their additio
# method overloading
class test:
    
    def __init__(self):
        print("object is created ")
    def m1(self,a=None,b=None,c=None,d=None):
        if a is None and b is None and c is None and d is None:
            print("this is m1 method")
        elif a is not None and b is None and c is None and d is None:
            print(f"single argument {a}")
        elif a is not None and b is not None and c is None and d is None:
            print(a+b)
        elif a is not None and b is not None and c is not None and d is None:
            print(a+b+c)
        else:
            print(a+b+c+d)
t = test()
# t.m1()
# t.m1(10)
t.m1(10,20,30,40)

# this is how we can achive the method overloadind in python 

# polymorphism :it is the quality of an objet or method to work in multiple forms as 
# depending on its use it allows the flexiblity and manipulatipn in our code for various
# predefined functions and operatprs