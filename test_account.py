#import unittest
import account

'''class TestStringMethods(unittest.TestCase):

   def test_init(self):
      testAcc = account.Account("Test Name")
      assert testAcc.get_name() == "Test Name"
      assert testAcc.get_balance() == 0
   
   def test_despoist(self):
      testAcc = account.Account("Test Name")
      assert testAcc.deposit(500) == True
      assert testAcc.get_balance() == 500

      assert testAcc.deposit(-200) == False
      assert testAcc.get_balance() == 500

      assert testAcc.deposit(0) == False
      assert testAcc.get_balance() == 500
   
   def test_withdraw(self):
      testAcc = account.Account("Test Name")
      testAcc.deposit(700)

      assert testAcc.withdraw(300) == True
      assert testAcc.get_balance() == 400

      assert testAcc.withdraw(-100) == False
      assert testAcc.get_balance() == 400

      assert testAcc.withdraw(0) == False
      assert testAcc.get_balance() == 400

      assert testAcc.withdraw(600) == False
      assert testAcc.get_balance() == 400'''

def test_init(self):
   testAcc = account.Account("Test Name")
   assert testAcc.get_name() == "Test Name"
   assert testAcc.get_balance() == 0

#if __name__ == '__main__':
   #unittest.main()