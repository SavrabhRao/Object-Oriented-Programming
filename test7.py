class test:
    def __init__(self,a,b,c):
        self.val1 = a
        self.val2 = b
        self.val3 = c
        print("object is created and memory is also allocated ")

    def m1(self,d):
        self.val4 = d

t = test(10,20,30)
print(f"before invoking m1: {t.__dict__}")

t.m1(40)
print(f"after invoking m1: {t.__dict__}")

