
class BalanceManager:
    def __init__(self):
        self.balance_file = "data/balance.txt"

    def load_balance(self):
        with open(self.balance_file) as f:
            return float(f.read())

    def save_balance(self, value):
        with open(self.balance_file, "w") as f:
            f.write(str(value))