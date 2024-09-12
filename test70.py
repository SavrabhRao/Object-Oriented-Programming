from abc import abstractmethod , ABC

# abstract class
class test(ABC):
    def __init__(self):
        print("test class")

    @abstractmethod
    def abstmtd(self):
        pass

t = test() # TypeError: Can't instantiate abstract class test without an implementation 
           # for abstract method 'abstmtd'