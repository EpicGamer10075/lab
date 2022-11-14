class Account:
   name = ""
   balance = -1
   def __init__(self, name):
      self.name = name
      self.balance = 0

   def deposit(self, amount):
      if amount > 0:
         self.balance += amount
         return True
      else:
         return False
   
   def withdraw(self, amount):
      if amount > 0 and amount < self.balance:
         self.balance -= amount
         return True
      else:
         return False

   def get_balance(self):
      return self.balance
   
   def get_name(self):
      #print(self.name)
      return self.name