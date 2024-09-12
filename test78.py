# interface -: what is this interface
# Interface is like SRS report
# Software Requirement Specification 
# this is like most important methods which the client must want in out program 
# for that in java we have interface but in python there is no implecite support
# for interface 

# but we can achieve interface by using the abstract methods inside abstract class 
# in python what is interface -: the abstract method without comcrete method and only
# with the abstract methods called interface in python we have to inherite it with 
# ABC module
#
#  a reference type that groups related methods and constants together, and is used 
#  to achieve abstraction and security 

# we can not create object of interface 
from abc import *
class Interface(ABC): # interface

    @abstractmethod
    def AbstractMethod(self):
        pass
    
    @abstractmethod
    def SecndAbstractMethod(self):
        pass

class implementation(Interface):

    def AbstractMethod(self):
        print("this is the implementation for AbstractMethod ")
    
    def SecndAbstractMethod(self):
        print("this is the implementation for SecndAbstractMethod ")


i = implementation()
i.AbstractMethod()
i.SecndAbstractMethod()