class BalanceManager:
    def __init__(self, balance_file):
        self.balance_file = balance_file

    def load_balance(self):
        try:
            with open(self.balance_file) as f:
                return float(f.read())
        except FileNotFoundError:
            with open(self.balance_file, "w") as f:
                f.write("00.00")
            return None

    def save_balance(self, value):
        with open(self.balance_file, "w") as f:
            f.write(str(value))