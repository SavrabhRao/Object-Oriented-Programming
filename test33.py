# single inheritance

class neha:
    def __init__(self):
        print("nehas 2 kids")
    def info(self):
        print("hi this is neha")

class nehasson(neha):
    def __init__(self,vagheshentry):
        print("hello this is neha")
        if vagheshentry.lower() == "yes":
            super().__init__()
        else:
            print("neha have no kids")
    def intro(self):
        print("hi i am neha and vag**sh's kid")

saurabh = nehasson("yes")
saurabh.intro()
saurabh.info()