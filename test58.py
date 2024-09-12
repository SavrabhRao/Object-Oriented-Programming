# method overriding

class shape:
    def __init__(self):
        pass
    def area(self):
        pass

class triangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return 0.5*self.length*self.breadth

class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side

t = triangle(10,8)
res = t.area()
print(res) #40
s = square(10)
res = s.area()
print(res) #100
print(help(int))
