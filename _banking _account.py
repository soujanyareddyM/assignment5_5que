class Account:
    def _init_(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance
    def getBalance(self):
        print("your balance is :")
        return self.Balance
    def deposit(self,amount):
        self.amount=amount
        self.Balance=self.Balance+self.amount
        print("Balance after deposited is :")
        return self.Balance

    def withdrawal(self,amount):
        self.amount=amount
        self.Balance=self.Balance-self.amount
        print("Balance after withdrawn is : ")
        return self.Balance
    
    
class SavingsAccount(Account):
    def _init_(self,title=None,Balance=0,interestRate=0):
        super()._init_(title,Balance) 
        
        self.interestRate= interestRate 
    def InterestAmount(self):
        print("interest amount is: ")
        return ((self.interestRate*self.Balance)//100)
    def display(self):
   
        return  f"{self.title} has balance {self.Balance} in account  and interest is: {self.interestRate} "
    

    
obj=SavingsAccount("sia",5000,2)
print(obj.display())
print(obj.InterestAmount())

print(obj.getBalance())
print(obj.deposit(88))
print(obj.withdrawal(10))