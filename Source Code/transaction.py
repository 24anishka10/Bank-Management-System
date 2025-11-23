from datetime import datetime

class Transaction:
    def __init__(self, acc_num, trans_type, amount, date=None):
        self.acc_num = int(acc_num)
        self.trans_type = trans_type
        self.amount = float(amount)
        # Use current time if date is not provided
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.acc_num},{self.trans_type},{self.amount},{self.date}"
