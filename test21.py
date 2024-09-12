# we directly pass the object as argument of a function 

""" Duck Typing """

# if it looks ike duck
# if it swims like duck
# if its sounds like duck 
# then it is duck

class dog:
    def sound(self):
        print("Whao Whao! ")
    
class duck:
    def sound(self):
        print("Quack Quack! ")

class cat:
    def sound(self):
        print("Mew Mew! ")

def SoundGetter(obj):
    obj.sound()
    
dog = dog()
duck = duck()
cat = cat()

SoundGetter(dog) # Whao Whao!
SoundGetter(duck) # Quack Quack!
SoundGetter(cat) # Mew Mew!

    

# example there is a duck , cat , dog  --> # behaviour method
# so if object is having those all the behaviors which we want then no need to cheak the 
# class of that object we can analyse it by looking at its behaviour 

# here in ducktyping you have no need to cheak the class of object only object and a 
# required method is needed 

# if object is having that method on which you want to perform operation then you can
# do ductyping here 

# ducktyping should be done in static method which is most prefferable 

