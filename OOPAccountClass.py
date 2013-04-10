class Account():

    def __init__(self, acct_id):
        self.acct_id = acct_id
        self.balance = 0

    def add_funds(self, amt):
        self.balance += amt

    def withdraw_funds(self, amt):
        self.balance -= amt

    def check_balance(self):
        return self.balance

