# soney 1
# soney 2
# soney 3
# soney 4

class soney1:
    def s1property(self):
        print("colour tv")

class soney2(soney1):
    def s2property(self):
        print("LCD Tv")

class soney3(soney2):
    def s3property(self):
        print("LED tv")

class soney4(soney3):
    def s4property(self):
        print("OLED Display")

poor = soney1()
middleclass = soney2()
neha = soney3()
saurabh = soney4()

saurabh.s4property()
saurabh.s3property()
saurabh.s2property()
saurabh.s1property()

# neha.s4property()