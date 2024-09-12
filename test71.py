from abc import ABC , abstractmethod

class test(ABC): # Now the abc is abstract base class
    def __init__(self):
        print("abstract base class")

    def ConcretMethod(self):
        print("this is concrete class")

t = test()
# in this abstract class there is no abstract method so we can create object

