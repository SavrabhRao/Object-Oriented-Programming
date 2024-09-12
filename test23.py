# Shoping Cart

l = [{"T-shirt":500},{"Shoes":799},{"mobiles":14999},{"Laptop":50000},{"Ipad":40000}]

class Ecart:

    id_generator = 2024100

    def __init__(self,name,pwd):
        Ecart.id_generator = Ecart.id_generator + 1
        self.name = name
        self.id = Ecart.id_generator
        self.password= pwd
        self.total_items = []
        print(f"your id is {self.id} and password is {self.password}")
    
    def add_cart(self,productname):
        for product in l:
            if product.get(productname,None) != None:
                print(f"product name {productname} of rs {product.get(productname)}" )
                self.total_items.append(productname)
                break
        else:
            print("Product not available")
        
    def show_total_items(self):
        print("items in your cart are:",end=" ")
        res = " , ".join(self.total_items)
        print(res)  

    def place_order(self):
            print(f"order placed for items {self.total_items}")

user1 = Ecart("Saurabh",1901)
# your id is 2024101 and password is 1901
user1.add_cart("T-shirt")
user1.add_cart("Shoes")
user1.show_total_items()
user1.place_order()