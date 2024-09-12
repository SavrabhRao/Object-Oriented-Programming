# i want to access the constructor of parent class inside child class so how and where 
# can i access it like in which methods

# As constructor is instant method so we can access it only inside constructor 
# of child class or inside the instance method of child class using super().__init__()
# no need to pass the self

class parent:
    def __init__(self,name):
        print("parent class constructor")
        self.name = name
    def getparentname(self):
        print(f"parent name is {self.name}")

class child(parent):
    def __init__(self,name,childname):
        super().__init__(name)
        self.childname = childname
    def childinfo(self):
        print(f"child name is {self.childname}")
        super().getparentname()

saurabh = child("balsaheb","saurabh")
saurabh.childinfo()