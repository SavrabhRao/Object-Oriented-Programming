# class product
# class tshirt


# # class product
# productname ,price
# displaydetails method

# # class tshirt
# size cloathtype
# tshirtinfo(instance)
# pritn("Size",cloathtype)
# displaydetails method


class product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def details(self):
        print(f"name is {self.name} and price is {self.price}")
    @classmethod
    def totalproducts(cls):
        print("total number of selected items are: ",cls.count)

        
class tshirt(product):
    def __init__(self,name,price,size):
        super().__init__(name,price)
        product.count = product.count + 1
        self.size = size
    def details(self):
        super().details()
        print(f"size of {self.name} is {self.size} ")

class tv(product):
    def __init__(self,name,price,inches):
        self.inches = inches
        product.count = product.count + 1
        super().__init__(name,price)

    def details(self):
        super().details()
        print(f"size of {self.name} is {self.inches} ")        

class videogames(product):
    def __init__(self,name,price,generation):
        self.generation = generation
        product.count = product.count + 1
        super().__init__(name,price)
    def details(self):
        super().details()
        print(f"generation of  {self.name} is {self.generation} ")

shirt = tshirt("puma",1000,"xl")
shirt.details()
print("----------------------------------------------")
television = tv("sony",45000,"45")
television.details()
print("----------------------------------------------")
game = videogames("GTA",2000,"5")
game.details()
print("----------------------------------------------")
product.totalproducts()

