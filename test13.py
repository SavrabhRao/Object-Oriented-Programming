
# how to declare class method                                   
# to declare class method we use a decorator called @classmethod
# and its first argumentv is cls                                
# this method is also known as factory method                   
                                                                
# how to cll classmethod ?                                      
# to call classmethod we can use objectref.methodname()         
# and we can also call it using classname.classmethodname()     
# but recomended is to use classmethod.classname()               


'''

whatever variabes are there in classmethod
with cls.varaname = val they will be stored in class object

'''

class test:

    def __init__(self):
        print("object is created")

    @classmethod
    def clsmethod(cls):
        print(id(cls))
        cls.a = 10
    
t = test()
t.clsmethod()
print(id(test))