# Hybrid inheritance 
# combination of multiple inheritances is called hybrid inheritance

# example from the diagram

class a:
    def m1(self):
        print("this is class a")
class b:
    def m2(self):
        print("this is class b")
class c:
    def m3(self):
        print("this is class c")

class d(a,b,c):
    def m4(self):
        print("this is class d")

class e(d):
    def m5(self):
        print("this is class e")
class f(e):
    def m6(self):
        print("this is class f")
class g(f):
    def m7(self):
        print("this is class g")
class h(f):
    def m8(self):
        print("this is class h")
    
objh = h()
objh.m1()
objh.m2()
objh.m3()
objh.m6()
objh.m8()
# objh.m7()
print(h.mro())
print(help(h))