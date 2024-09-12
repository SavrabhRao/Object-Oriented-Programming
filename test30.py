# composition - strongly bounded 
# aggregation - weak related
"-----------------------------------------------------------------------------------"

#composition 
class engine:
    power = "100hp"
    def __init__(self):
        print("engine object is created")

    def EngineInfo(self):
        print("engine installed succesfully")
        print(f"power of engine is {engine.power}")

class car:
    def __init__(self,model):
        print("car is created")
        self.engine = engine()
        self.model = model
    def CarInfo(self):
        print(f"this is {self.model} car")
        self.engine.EngineInfo()
    
c = car("Vitara Brezza")
c.CarInfo()

# Aggregation
class teacher:
    def __init__(self , name):
        self.name = name
    def Info(self):
        print(f"teacher name is {self.name}")

saurabh = teacher("saurabh")
neha = teacher("neha")

class collage:
    def __init__(self,ob):
        self.trainer = ob
    def TeacherInfo(self):
        self.trainer.Info()

c = collage(saurabh)
c.TeacherInfo()

# the objective ob has a relation is to use the methods and variables of another class
# inside current class