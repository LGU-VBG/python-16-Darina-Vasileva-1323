class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("не может быть -")
        self._balance = value
        

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма  должна быть +")
        self.balance += amount  
 
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма должна быть +")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount  
        
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)
    
    @property
    def get_balance(self):
        return self.balance

    
#1
account = BankAccount() 
 
print(account.get_balance) 
account.deposit(100) 
print(account.get_balance) 
account.withdraw(50) 
print(account.get_balance)
#2
account = BankAccount(100) 
 
try: 
    account.withdraw(150) 
except ValueError as e: 
    print(e)
    
#3
account1 = BankAccount(100) 
account2 = BankAccount(200) 
 
account1.transfer(account2, 50) 
print(account1.get_balance) 
print(account2.get_balance)
#4
account1 = BankAccount(100) 
account2 = BankAccount(200) 
 
try: 
    account1.transfer(account2, 150) 
except ValueError as e: 
    print(e)