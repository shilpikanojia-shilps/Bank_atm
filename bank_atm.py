class BalanceException(Exception):
    pass


class Bankaccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"\nAccount '{self.name}'created. \nbalance = '{self.balance:.2f}")
        
    def getbalance(self):
        print(f"\nAccount'{self.name}' \nBalance '{self.balance}'") 
        
    def deposit(self, amount):
        self.balance += amount
        print("Deposite complete")
        self.getbalance()
        
    def viabletransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nAccount '{self.name}' only has the balance'{self.balance}'")
                
    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance -= amount
            print("Withdraw complete")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw Interupted {error}") 
        
    def transfer(self, amount, account):
        try:
            print('\n************\n\nBeginning Transfer..🚀')     
            self.viabletransaction(amount)
            self.withdraw(amount)    
            account.deposit(amount)   
            print("Transfer completed..✔")
        except BalanceException as error:
            print(f"Transfer Interrupted**********❎ {error} ")
            
            
class InterestRewardAccount(Bankaccount):
    
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("Deposit complete")
        self.getbalance()
        
class SavingsAccount(InterestRewardAccount):
    
    def __init__(self, initialamount, acctname):
        super().__init__(initialamount, acctname)
        self.fee = 5
        
    def withdraw (self, amount):
        try:
            self.viabletransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\n Withdraw complete")
            self.getbalance( )
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
        
