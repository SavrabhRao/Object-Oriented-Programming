class test:
    def __init__(self,a,b,c):
        self.name = a
        self.marks = b
        self.age = c
        print("constructor is executed")

a = test("saurabh",90,21)
print(a.name)
print(a.marks)
print(a.age)

b = test("neha",92,24)
print(b.name)
print(b.marks)
print(b.age)

a.name = "Divya"
print(a.name)

c = test("vishal",10,20)
c.name = "rahul"
print(c.name)
print(c.marks)
print(c.age)

"instance variables"
# the variables declared with self argument are called as instance variables 
# instance variables are object level variables 
# you can declare it inside constructor and instance methods 