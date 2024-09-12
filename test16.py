class test:

    a = "test project"

    def __init__(self):
        a = 10   # local variable
        print(a)
    
    @staticmethod
    def staticmtd(a,b):
        val1 = a # local variable
        val2 = b # local variable
        return val1 + val2          

t = test()
res = test.staticmtd(10,20)
print(res)
print(test.a)


