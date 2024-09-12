class samantha:
    def beauty(self):
        print("samanthas beauty")
    def brain(self):
        print("samanthsa's brain")

class saurabh:
    def brain(self):
        print("saurabh's brain")

class son(samantha , saurabh):
    def __init__(self):
        print("hello am just now born")
    # def brain(self):
    #     print("this is my brain")

s = son()
s.brain()

print(son.mro())