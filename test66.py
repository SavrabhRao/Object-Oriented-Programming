
class Doremon(object):
    def __init__(self,n):
        self.num = n
    def __str__(self):
        return f"{self.num}"
    def __add__(self,other):
        return Doremon(self.num * other.num) # a + b

class Shizuka:
    def __init__(self,n1):
        self.num = n1
    def __str__(self):
        return f"{self.num}"
    def __add__(self,other):
        return Shizuka(self.num * other.num)


d = Doremon(10)    
s = Shizuka(20) 
res = d+s
print(res,type(res)," for the d+s ")
res = s+d
print(res,type(res)," for the s+d ")

# it will cheak __add__ methiod inside doremon only as its left side of + not in shizuka

# datatype of month and rent 