class engine:
    power = "100hp"
    def EngineInfo(self):
        print("engine installed successfully")
        print(f"power of this engine is {engine.power}")

class tyer:
    def TyerInfo(self):
        print("Tyer installed successfully")

class car:
    def __init__(self):
        self.engine = engine()
        self.tyer = tyer()

    def getinfo(self):
        self.engine.EngineInfo()
        self.tyer.TyerInfo()
c = car()
c.getinfo()
    
