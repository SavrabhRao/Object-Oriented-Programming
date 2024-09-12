

''' abstract method -: the method which is not having implementation but just the 
declaration this is called as abstract method 
and method which has complete implementation  called as concrete method
abstraact method is implemented using @abstractmethod decorator from abc module 
these methods are just declaration 
for the good programming practices we should declare it inside abstract class only
'''


''' abstract class: this is the class in which we declare abstract methods it is inherited
with ABC class (abstract base class) this class is just partially declared class 
you can not create the object of this class 
abstract class will be always the child of ABC class else it will not called as abstract 
class
If there is no abstract method inside abstract class, then you can create the object of 
that abstract class. But that abstract class will not be of any use It will just like 
regular classes
But if inside the abstract class there is a single abstract method or more, then you cannot
create the object of that class
'''


''' now when you will create the child class inherited with abstract class at that time 
you have to give implementation to all the abstract methods inside the abstract class 
else your child class will also treated as the abstract class only 
'''


'''
why we need abstract classes 
if there is a very big project and in that project there is compulsary requirment of 
some methods without which there is no use of that project in such cases we use abstract 
method inside abstract class 

as you can not create the object of abstract class so you can write down some essensial 
method inside abstract class without using @abstractmethod decoretor it will be accessible
to child class only as we can not create the object of abstract base class
'''