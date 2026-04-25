class Account:
    def __init__(self):
        self.balance = 1000
        self.transactions = []

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount