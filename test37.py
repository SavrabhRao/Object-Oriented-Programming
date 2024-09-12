# multiple inheritance 
# languages like java and cpp donot support this inheritance 
# in this inheritance multipal parents and single child 

class p1:
    def p1m(self):
        print("method of p1")
class p2:
    def p2m(self):
        print("method of p2")

class c1(p1,p2):
    def c1m(self):
        print("method of c1")

c = c1()
c.c1m()
c.p1m()
c.p2m()