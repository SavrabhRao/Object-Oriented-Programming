
class parent:
    def __init__(self,a):
        self.__var = a

    def var(self):
        print(f"private variable {self.__var}")
    
    def __privatemethod(self):
        print("this is the private method")

class child(parent):
    def __init__(self):
        print(f"this is child class constructor")
        # super().__privatemethod() # AttributeError 'super' object has no attribute 
                                  # '_child__privatemethod'
    def instance(self,a):
        super().__init__(a)
        # print(self.__var) # AttributeError: 'child' object has no attribute '_child__var'

c = child()
c.instance(10)

# but you can access it using name mangling
p = parent(10)
p._parent__privatemethod() # name mangling thisis also loophole
print(p._parent__var) # name mangling thisis also loophole
print("---------------- full stop ---------------------")

