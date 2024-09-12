class mrutyunjay:
    def __init__(self):
        print("this is mrutyunjay")
    def prise(self):
        print("1000")
class chawa:
    def __init__(self):
        print("this is chawa")
    def prise(self):
        print("100")

m = mrutyunjay()
c = chawa()
class library:
    def __init__(self):
        self.mrutnjy = m
        self.chava = c
    def getinfo(self):
        self.mrutnjy.prise()
        self.chava.prise()

l = library()
l.getinfo()