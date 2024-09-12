class samantha:
    def beauty(self):
        print("samanthas beauty")
class saurabh:
    def brain(self):
        print("saurabh's brain")

class vikramaditya(samantha , saurabh):
    def __init__(self):
        print("hello am just now born")

v = vikramaditya()
v.brain()
v.beauty()

# this inheritance is only supported in python
# in java and cpp its not there 
