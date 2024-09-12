# types of inheritance
''' 
1] single inheritance
2] multilevel inheritancehierar
3] hierarchical inheritance
4] multiple inheritance
5] Hybrid inheritance

''' 

''' 1] single inheritance 
    only one parent class and 1 child class
'''

class papa:
    def property(self):
        print("saurabhs papas property")

class son(papa):
    def __init__(self):
        print("hii am saurabh")
    def Info(self):
        print("i am son of my papa")

saurabh = son()
saurabh.property()
saurabh.Info()