class Number():
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num * other.sum

class Integer:
    def __init__(self,num):
        self.sum = num

a = Number(10)
b = Integer(20)
print(a+b)
print(b+a)

# it will cheak the __add__method in class a only not in b because a is in left side of 
# + oprator 
# from above program if you give b in left side and a on right then it will
# give us left and right
