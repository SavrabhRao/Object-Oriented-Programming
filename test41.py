class a:
    def m1(self):
        print("class a")

class b(a):
    def m1(self):
        print("class b")

class c(a):
    def m1(self):
        print("class c")

class d(b,c):
    
    def m1(self):
        print("class d")

objd = d()
objd.m1()

print(d.mro())