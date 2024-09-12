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

    def AbstractMethod(self):
        pass
    
c = child()

# here we follow all the rules hence we are able to create object of this class 
# this is child class