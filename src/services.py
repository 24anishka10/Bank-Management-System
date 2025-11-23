import json
import os
from models import Account
from utils import hash_password, verify_password, logger

DATA_FILE = 'data/users.json'

class BankService:
    def __init__(self):
        self.accounts = self._load_data()

    def _load_data(self):
        if not os.path.exists(DATA_FILE):
            return {}
        try:
            with open(DATA_FILE, 'r') as f:
                # Check if file is empty before loading
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return empty dict if file is missing or corrupt
            return {}

    def _save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.accounts, f, indent=4)

    # Functional Module 1: User Creation (Register)
    def create_account(self, name, pin):
        import random
        acc_num = str(random.randint(10000, 99999))
        if acc_num in self.accounts:
            return self.create_account(name, pin) # Retry if duplicate
        
        new_acc = Account(acc_num, name, hash_password(pin))
        self.accounts[acc_num] = new_acc.to_dict()
        self._save_data()
        logger.info(f"New account created: {acc_num}")
        return acc_num

    # Functional Module 2: Authentication
    def login(self, acc_num, pin):
        if acc_num in self.accounts:
            stored_data = self.accounts[acc_num]
            if verify_password(stored_data['pin_hash'], pin):
                logger.info(f"User logged in: {acc_num}")
                return Account(**stored_data)
        logger.warning(f"Failed login attempt: {acc_num}")
        return None

    # Functional Module 3: Transaction Processing [cite: 26]
    def perform_transaction(self, account, amount, txn_type):
        try:
            if txn_type == 'deposit':
                account.balance += amount
            elif txn_type == 'withdraw':
                if account.balance >= amount:
                    account.balance -= amount
                else:
                    return False, "Insufficient Funds"
            
            # Update history
            account.history.append(f"{txn_type.upper()}: {amount}")
            
            # Persistence
            self.accounts[account.account_number] = account.to_dict()
            self._save_data()
            logger.info(f"Transaction {txn_type} on {account.account_number}: {amount}")
            return True, "Success"
        except Exception as e:
            logger.error(f"Error in transaction: {str(e)}")
            return False, "System Error"
