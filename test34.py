# multilevel inheritance 

# grandpa ---> 10 acr
# .
# .
# .
# father ----> 10 acr from grandpa + his own purchased 5 acr
# .
# .
# .
# son -----> 10 acr from grandpa + father'spurchased 5 acr + his own some

# concepts of inheriting multiple classes from top to bottom one after another called 
# multilevel inheritance
# in mathematical rerms its like transitive relation
# if a is remated to b and b is related to c then a is also related to c
# example

class grandpa:
    def grandpa_property(self):
        print("10 acr")

class father(grandpa):
    def father_property(self):
        print("10 acr from grandpa + 5 its own ")

class son(father):
    def son_property(self):
        print("10 acr from grandpa + 5 from father and his own 3 ")

son = son()
son.father_property()
son.grandpa_property()
son.son_property()