# Hierarchical Inheritance 
# multiple child class inheriting the property of a single parent class called hierarchical
# Inheritance

class grandpa:
    @classmethod
    def property(cls):
        print("grandpas property")

class papa(grandpa):
    def papaprop(self):
        print("papas property")
class uncle(grandpa):
    def uncleprop(self):
        print("uncle property")

class son(papa):
    def sonprop(self):
        print("son property")

class cousin(uncle):
    def propsousin(self):
        print("cousin property")

saurabh = son()
saurabh.papaprop()
son.property()
# son.uncleprop() # error

vishal = cousin()
vishal.property()