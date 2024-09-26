from bank_atm import *

Sunil = Bankaccount("Sunil", 2000)
Preeti = Bankaccount("Preeti", 2000)


# Sunil.getbalance()
# Preeti.getbalance()


# Sunil.withdraw(500)
# Sunil.getbalance()
# Preeti.deposit(1250)
# Preeti.getbalance()
# Preeti.viabletransaction(200)
# Preeti.withdraw(99)
# Preeti.transfer(2200,Sunil)
# Preeti.getbalance()


# Jim = InterestRewardAccount('Jim', 1000)
# Jim.getbalance()
# Jim.deposit(1000)

# Jim.transfer(200, Sunil)
# Sunil.getbalance()
# Jim.getbalance()


David = SavingsAccount( 'David', 1000)
David.getbalance()
# David.deposit(5000)
# David.transfer(2009, Sunil)
David.withdraw(5001)