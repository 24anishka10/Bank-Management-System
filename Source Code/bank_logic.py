import random
import persistence
from account import BankAccount
from transaction import Transaction

class BankSystem:
    def __init__(self):
        self.accounts = persistence.load_accounts()

    def create_account(self, name, pin, acc_type):
        # Generate unique ID
        while True:
            acc_num = random.randint(10000, 99999)
            if acc_num not in self.accounts:
                break
        
        new_acc = BankAccount(acc_num, name, pin, acc_type, 0.0)
        self.accounts[acc_num] = new_acc
        
        # Save to file
        persistence.save_accounts(self.accounts)
        return acc_num

    def login(self, acc_num, pin):
        if acc_num in self.accounts:
            if self.accounts[acc_num].pin == pin:
                return self.accounts[acc_num]
        return None

    def deposit(self, acc_obj, amount):
        acc_obj.balance += amount
        persistence.save_accounts(self.accounts)
        
        t = Transaction(acc_obj.acc_num, "Deposit", amount)
        persistence.log_transaction(t)
        return True

    def withdraw(self, acc_obj, amount):
        if amount > acc_obj.balance:
            return False, "Insufficient Funds"
        
        acc_obj.balance -= amount
        persistence.save_accounts(self.accounts)
        
        t = Transaction(acc_obj.acc_num, "Withdraw", amount)
        persistence.log_transaction(t)
        return True, "Success"

    def get_history(self, acc_num):
        return persistence.load_transactions(acc_num)
