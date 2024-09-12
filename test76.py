from abc import ABC , abstractmethod

class parent(ABC): # Abstract base class
    def __init__(self):
        print("abstract base class")

    @abstractmethod
    def AbstractMethod(self):
        pass
    
    @abstractmethod
    def SecndAbstractMethod(self):
        pass


class child(parent):
    def __init__(self):
        print("this is child class")

    def AbstractMethod(self):
        print("this is concrete class")

    def SecndAbstractMethod(self):
        print("this is 2nd abstract class")



c = child()
c.AbstractMethod()
c.SecndAbstractMethod()
