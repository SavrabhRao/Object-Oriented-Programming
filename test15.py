# where to be declare static variable

class test:
    a = 100

    def __init__(self):
        test.b = 200

    def instance(self):
        test.c = 300

    @classmethod
    def classmetd(cls):
        cls.d = 400
        test.z = 900

    @staticmethod
    def staticmtd():
        test.e = 500

# outside class how to declare this static variable ?
test.f = 600
print(test.f)
# to call print val of a how can i do it
print(test.a)

# 2] create the object of the class and then call it with obrefvar but its not recomended
t = test()
print(t.a) # not recomended
print(t.b) # not recomended

print(test.b)

# # to access the c 
# test.instance() #error
t = test()
t.instance()
print(test.c)

test.classmetd() #recomended
print(test.d) #recomended

# # # you can invoke classmethod using objrct ref var also but its not frecomended
s = test()
s.classmetd() # not recomended
print(s.d) # not recomended
print(test.z)

u = test()
u.staticmtd() # not recomended
test.staticmtd() # recomended

test.staticmtd()
print(test.e)