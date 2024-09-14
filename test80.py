# protected methods      

class parent:           
    def __init__(self,a):
        self.a = a      
    def _protected(self):
        print(f"this is protected method{self.a}")

class child(parent):
    def __init__(self):
        super().__init__(10)
        super()._protected()


p = child()
p._protected()