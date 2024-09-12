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
           inside classmethod  you can call the static and classmethod of parent class by
           using cls.methodname() or super().methodname()
           but you cannot access the instance method inside classmethod as like instance 
           variables
           
           if the method is present in child class with same name as parent class method then 
           calling with cls.methodname()    ---> child class method will execute
           calling with super().methodname() ---> parent class method will execute
        '''
        
    @classmethod
    def clsmtd(cls):
        super().staticmethod()
        super().classmethod()  

    def instance(self):
        print("this is instance method of child class")

    @classmethod
    def classmethod(cls):
        print("this is class method of child class")

    @staticmethod
    def staticmethod():
        print("this is static method of child class")
child.clsmtd()
