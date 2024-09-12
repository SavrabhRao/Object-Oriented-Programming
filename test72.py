from abc import ABC , abstractmethod

class test(): 
    def __init__(self):
        print("abstract base class")

    @abstractmethod
    def AbstractMethod(self):
        print("this is concrete class")

t = test()

# in this class there is abstract method but the class is not
# inherited with ABC henc its not abstract class and we can create object 