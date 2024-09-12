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

class son(child):
    def SecndAbstractMethod(self):
        print("second abstract class")

c = son()
c.AbstractMethod()
c.SecndAbstractMethod()

# if you didnt give implementation to all the method of abstract class in child method
# then you can not create object of child class 
# but you create one more class which will be inherited with child class and give execution
# to remqining methods in it then you can create object of that class and also access all
# the methods 