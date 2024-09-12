class ChotaBheem:
    def __init__(self,num):
        self.num = num
    def __str__(self):
        return f"{self.num}"
    def __add__(self,other):
        return ChotaBheem(self.num + other.num)
    def __sub__(self,other):
        return ChotaBheem(self.num - other.num)
    def __mul__(self,other):
        return ChotaBheem(self.num * other.num)
    def __truediv__(self,other):
        return ChotaBheem(self.num / other.num)
    def __gt__(self,other):
        return ChotaBheem(self.num > other.num)
    # def __lt__(self,other):
    #     return ChotaBheem(self.num < other.num)

bheem = ChotaBheem(100)
chutki = ChotaBheem(90)

print(f"bheem + chutki ----> {bheem + chutki}")
print(f"bheem - chutki ----> {bheem - chutki}")
print(f"bheem * chutki ----> {bheem * chutki}")
print(f"bheem / chutki ----> {bheem / chutki}")
print(f"bheem > chutki ----> {bheem > chutki}")
print(f"bheem < chutki ----> {bheem < chutki}")

""" in the above program if we give a magic method __gt__ (>) then it will also execute
for lessthan(__lt__ , <) without declaring __lt__ method 
and at that moment self will be rightmost object and other will be leftmost one
"""