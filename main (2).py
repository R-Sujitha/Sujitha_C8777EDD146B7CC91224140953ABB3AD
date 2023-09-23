class Bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance = 0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance += amount
      print("deposited ₹{}.  New Balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid Deposit Amount")
  def Withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw ₹{}.  New Balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid Withdrawal Amount or Insufficient balance.")

  def display_balance(self):
    print("Account Balance for {}(account #{}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))



account = Bankaccount(account_number ="8870812345",  account_holder_name ="Sujatha",  initial_balance = 1000.0)



account.display_balance()
account.deposit(500.00)
account.Withdraw(200.0)
account.Withdraw(1500.0)
account.display_balance()
