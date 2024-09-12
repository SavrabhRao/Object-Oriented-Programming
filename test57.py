# method overriding

class mother:
    def __init__(self):
        pass
    def marry(self):
        print("my son will marry with seethakka")

class parent:
    def __init__(self):
        pass
    def marry(self):
        print("my son will marry to subbalaxmi")

class child(parent,mother):
    def __init__(self):
        print("dude is landed on the planet")
    def marry(self):
        print("i will marry with applamma")
    
c = child()
c.marry()