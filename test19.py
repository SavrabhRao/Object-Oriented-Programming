# instance method is a bitt different methdo
class test:

    def method(self):
        print("any other method") 

t = test()
# test.method(10) 
# print(help(test))
t.method()

# if you call the instance method by referance of class name by passing argumnent
# for self then the method will be treated as static method 

# if you want to declare the static method without its decorator then you can access
# it only using the class name . method name and pass value for each argument