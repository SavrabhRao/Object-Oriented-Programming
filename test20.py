
class test:

    def __init__(self,a,b,c):
        print("object is created")
        self.age = a
        self.dob = b
        self.exp = c

    def method(self):
        print("any other method") 


neha = test(25,24,4) # object is created 
# neha.method(100) # TypeError: test.method() takes 1 positional argument but 2 were given
del neha.age
print(neha.age)
# if you are calling the instance method with object referance and passing value of self
# it will give error that extra argument is passed like below
# TypeError: test.method() takes 1 positional argument but 2 were given

# neha = test(25,24,4) 
# neha.method() # any other method | considerd as instance method
# test.method(982) # any other method | considerd as static method

# test.method() # error | considerd as static method
