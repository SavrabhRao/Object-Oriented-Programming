from abc import ABC , abstractmethod

class parent(ABC): # Abstract base class
    def __init__(self):
        print("abstract base class")

    @abstractmethod
    def AbstractMethod(self):
        print("this is concrete class")

class child(parent):
    def __init__(self):
        print("this is child class")
    
c = child()

# we havent given declaration to the abstract method in child class which is inherited with
# parent class which is abstract class and that parentclass has abstract method 
# and you havent gave implementation to it hence it will give error 

# TypeError: Can't instantiate abstract class child without an implementation for
# abstract method 'AbstractMethod'