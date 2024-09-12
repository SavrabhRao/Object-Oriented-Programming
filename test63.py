class object:
    def __str__(self):
        return "this is object class at this location"

class Number(object):
    def __init__(self,a):
        self.a = a
    def __str__(self):
        return f"{self.a}"


n = Number(10)
print(n)
