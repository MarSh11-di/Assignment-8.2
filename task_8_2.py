
class  Account:
   def __init__(self, account_number:str, holder_name:str, balance:float):
      self.account_number = account_number
      self.balance = self._is_valid_balans(balance)
      self.holder_name = holder_name

   def  _is_valid_balans(self, balance):
      if balance < 0:
         raise ValueError ("The balance cannot be negative")
      return balance

      
   def depositing_money(self, amount:float):
      if amount < 0:
         raise ValueError ("Please enter a positive amount")
      self.balance+=amount

   def withdrawing_money(self, amount:float):
      if self.balance < amount:
         raise ValueError ("insufficient funds")
      self.balance -= amount
   
   def __str__(self):
      raise NotImplementedError()
   

class CurrentAccount(Account):
   type_account = "Current account"

   def __str__(self):
      return f"type of account: {self.type_account}; \n account number: {self.account_number}; \n remaining balance: {self.balance}"

class SavingsAccount(Account):
   type_account = "Savings account"


   def __init__(self, account_number:str, balance:float, holder_name:str, interest_rate:int):
      super().__init__(account_number, balance, holder_name)
      self.interest_rate = interest_rate

   def add_interest(self): 
      self.balance += (self.balance*self.interest_rate)/100

   def __str__(self):
      return f"type of account: {self.type_account}; \n account number: {self.account_number}; \n  interest rate:{self.interest_rate}; \n remaining balance:{self.balance}"

amo = Account("36454727223","Ivanov", 1000.00)
# print(amo)
cur = CurrentAccount("1111111111","Shevchenko", 5000.00, )
sav = SavingsAccount("2222222222", "Shevchenko", 2000.00, 10)

array_acount =[]
array_acount.append(cur)
array_acount.append(sav)
for i, count in enumerate(array_acount):
   if isinstance(count, CurrentAccount):
      count.depositing_money(5000.00)
      count.withdrawing_money(2000.00)
   if isinstance(count, SavingsAccount):
      count.depositing_money(5000.00)
      count.withdrawing_money(2000.00)
      count.add_interest()
   print(count)


