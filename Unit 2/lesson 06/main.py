from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, balance = 0, interest_rate = 0):
        self.owner = owner
        self.__balance = balance
        self.__interest_rate = interest_rate

    @property
    def balance(self):
        return self.__balance
    
    @property
    def interest_rate(self):
        interest = self.__balance * self.__interest_rate
        return interest
    
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    @interest_rate.setter
    def interest_rate(self, rate):
        if rate >= 0:
            self.__interest_rate = rate
        else:
            print("Interest rate cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. Current balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. Current balance: {self.__balance}")
        else:
            print("Withdrawal amount exceeds balance or is invalid.")

    @abstractmethod
    def display_account_details(self):
        pass
    
class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance, 0.05)

    def display_account_details(self):
        print('\n============================')
        print('SAVINGS ACCOUNT')
        print(f'Account owner: {self.owner}')
        print(f'Balance: 💵 {self.balance}')
        print(f'Interest: 📈 {self.interest_rate}')
        return 

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def display_account_details(self):
        print('\n============================')
        print('CHECK ACCOUNT')
        print(f"Checking Account Owner: {self.owner}")
        print(f"Balance: 💵 {self.balance}")
        print(f"Interest Rate: 📈 {self.interest_rate}")


# Example usage
paula = SavingAccount('Paula', 1000)
paula.deposit(500)
paula.display_account_details()

sam = CheckingAccount('Sam', 1500)
sam.display_account_details()
sam.deposit(90)
sam.display_account_details()
sam.withdraw(50)
sam.display_account_details()