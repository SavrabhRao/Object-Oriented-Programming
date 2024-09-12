class parent:
    def instance(self):
        print("this is instance method of parent class")

    @classmethod
    def classmethod(cls):
        print("this is class method of parent class")

    @staticmethod
    def staticmethod():
        print("this is static method of parent class")

class child(parent):

    def __init__(self):
        
        '''
        inside static method you can not access methods using any argument or super you 
        need to acces the method using that class name only 

        here also you can not access the instance methdos as like instance variables 
        '''
        
    @staticmethod
    def staticmethodmtd():
        child.staticmethod()
        child.classmethod()  

    def instance(self):
        print("this is instance method of child class")

    @classmethod
    def classmethod(cls):
        print("this is class method of child class")

    @staticmethod
    def staticmethod():
        print("this is static method of child class")

child.staticmethodmtd()