from bank_accounts import *

Rahul = BankAccount(1000, "Rahul")
Sara = BankAccount(2000, "Sara")

Rahul.get_balance()
Sara.get_balance()

Sara.deposit(500)

Rahul.withdraw(10000)
Rahul.withdraw(10)

Rahul.transfer(10000, Sara)
Rahul.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100,Rahul)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)