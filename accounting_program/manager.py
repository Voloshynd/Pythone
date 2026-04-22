class Manager:
    def __init__(self):
        self.account = 0
        self.transaction_history = []
        self.warehouse = []
        self.commands = {}
        self.account_before_operation = self.account
        self.available_operations = ["balance", "sell", "buy", "account",
                                     "list",
                                     "inventory", "review", "end"]

    def assign(self, name):
        def decorate(callback):
            self.commands[name] = callback

        return decorate

    def execute(self, name):
        if name not in self.commands:
            print(f"Nieznana komenda: {name}")
            return None

        return self.commands[name](self)
