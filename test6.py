class test:
    def __init__(self,a,b,c):
        self.val1 = a
        self.val2 = b
        self.val3 = c
        print("object is created and memory is also allocated ")

t = test(10,20,30)
m = test(80,90,100)

t.val4 = "blue tick"

del t.val2 , m.val2

print(t.__dict__)
print(m.__dict__)