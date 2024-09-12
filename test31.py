# inheritance
# this is is-a relation

# in has a relationship we either create the object of one class inside another class 
# or use the object of one class inside another class 

# but here in is a relationship you have no need to do anyting like this if you want
# to use the properties of a class inside b class then make a class as a parent class and 
# b as child class 

# if you do it then all the propertys and attributes of class a will be also available for 
# class b 

class parent:
    pass

class child(parent):
    pass

c = child() 

# here you can access all the properties and attributes of parent class in child 
# class

class parent:
    a = 100
    def name(self):
        print("parent name is saurabh")

class child(parent):
    pass

c = child()
c.name()
print(child.a)
print(parent.a)

# print(help(parent))
print(help(child))

""" Inheritance is like a parent's to child relationship. Parent class member will be
 available to the child class. if the child class is inherited with parent's class In 
 child class. You can. reuse and extend the functionalities of parent class. by defining
 new members in child class. """

''' If child class and parent class both are having constructors, then. by default,
 interpritor will search constructor in. child class. If. available, then execute the constructor
 of child class only and hence It will not search in parent class but if the constructor is not
 available in child class then it will search it in parent class. '''