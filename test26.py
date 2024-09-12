# inner class / nested classes
class car:
    def __init__(self):
        print("its car")

    class engine:
        def __init__(self):
            print("its engine")

        def start(self):
            print("engine started")

# o = inner()
obj_car = car()
obj_eng = obj_car.engine()
obj_eng.start()