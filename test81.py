# private modifiers
# in private modifiers they are accessible inside the declared class only 
# not available for even child class and outside the class
# syntax to declare it is __varname (double underscore)

class parent:
    def __init__(self,a):
        self.__var = a
    def var(self):
        print(f"private variable {self.__var}")
    
    def __privatemethod(self):
        print("this is the private method")

p = parent(10)
p.var()
print(p.__var) # AttributeError error
p.__privatemethod() # AttributeError error