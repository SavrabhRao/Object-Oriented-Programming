from abc import ABC , abstractmethod

class test(ABC): # Abstract base class
    def __init__(self):
        print("abstract base class")

    @abstractmethod
    def AbstractMethod(self):
        print("this is concrete class")

t = test()

# as its abstract class and having abstract method in it so we cannot create object
# of this class

# TypeError: Can't instantiate abstract class test without an implementation for 
# abstract method 'AbstractMethod'
