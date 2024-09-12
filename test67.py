class Month:
    def __init__(self,num):
        self.num = num
    def __str__(self):
        return f"{self.num}"
    def __mul__(self,other):
        return Month(self.num * other.num)

class Rent:
    def __init__(self,saurabh):
        self.num = saurabh
    def __str__(self):
        return f"{self.num}"
    def __mul__(self,other):
        return Rent(self.num * other.num)

total_months = Month(12)
rent = Rent(16000)

total_rent = total_months*rent
print(total_rent,type(total_rent))

print("--------------------------------------------")

total_rent = rent*total_months
print(total_rent,type(total_rent))