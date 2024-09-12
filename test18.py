# bank application using oops
# generate account number for each and every 
# deposite money
# withdraw

class Bank:

    Bank_Name = "Saurabh International Bank" #static variable
    account_number_generator = 240305124100  #static variable 
    IFSC = "SBIB000075"                      #static variable

    def __init__(self , name , balance = 0): #constructor

        Bank.account_number_generator = Bank.account_number_generator + 1
        self.Name = name
        self.Balance = balance
        self.AccountNumber = Bank.account_number_generator
    
    def deposite(self, amount):
        self.Balance = self.Balance + amount
        print(f"Amount of {amount} is deposited in {self.Name}'s account")
    
    def withdraw(self,amount):
        if self.Balanc >= amount and amount % 100 == 0:
            self.Balance = self.Balance - amount
            print(f"{amount} Rs withdrawl succesfully")

        elif amount % 100 != 0:
            print("Please give amount in multiple of 100")

        else:
            print("insufficent funds")

    def Passbook(self):
        print("Name is: ",self.Name )
        print("Balance is: ",self.Balance )
        print("AccountNumber is: ",self.AccountNumber)

    @classmethod
    def BankInfo(cls):
        print("Bank name is: " , cls.Bank_Name)
        print("Bank IFSC Code: " , cls.IFSC)

Bank.BankInfo()
a = Bank("Maitri")
b = Bank("Vaghesh")
c = Bank("Showik")