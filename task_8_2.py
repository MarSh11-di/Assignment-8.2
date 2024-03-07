
class  Account:
   def __init__(self,account_number:str, balans:float, holder_name:str):
      self.account_number = account_number
      self.balans = balans
      self.holder_name = holder_name
      
   def depositing_money(self, amount:float):
      if amount < 0:
         raise ValueError ("Please enter a positive amount")
      self.balans+=amount

   def withdrawing_money(self, amount:float):
      if self.balans<amount:
         raise ValueError ("insufficient funds")
      self.balans -= amount
   
   def __str__(self):
      raise NotImplementedError()
   

class CurrentAccount(Account):
   type_account = "Current account"

   def __str__(self):
      return f"type of account: {self.type_account}; \n account number: {self.account_number}; \n remaining balance: {self.balans}"

class SavingsAccount(Account):
   type_account = "Savings account"


   def __init__(self, account_number:str, balans:float, holder_name:str, interest_rate:int):
      super().__init__(account_number, balans, holder_name)
      self.interest_rate = interest_rate

   def add_interest(self): 
      self.balans += (self.balans*self.interest_rate)/100

   def __str__(self):
      return f"type of account: {self.type_account}; \n account number: {self.account_number}; \n  interest rate:{self.interest_rate}; \n remaining balance:{self.balans}"

amo = Account("36454727223", 1000, "Ivanov")
# print(amo)
cur = CurrentAccount("1111111111", 5000.00, "Shevchenko")
sav = SavingsAccount("2222222222", 2000.00, "Shevchenko", 10)

array_acount =[]
array_acount.append(cur)
array_acount.append(sav)
for i, count in enumerate(array_acount):
   if isinstance(count, CurrentAccount):
      count.depositing_money(5000.00)
      count.withdrawing_money(2000)
   if isinstance(count, SavingsAccount):
      count.depositing_money(5000.00)
      count.withdrawing_money(2000)
      count.add_interest()
   print(count)


