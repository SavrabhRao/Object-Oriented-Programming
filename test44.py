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
           inside constructor or static method you can call the method of parent class by
           using self.methodname() or super().methodname()
           
           if the method is present in child class with same name as parent class method then 
           calling with self.methodname()    ---> child class method will execute
           calling with super().methodname() ---> parent class method will execute
        '''
        self.instance()
        self.staticmethod()
        self.classmethod()

c = child()
