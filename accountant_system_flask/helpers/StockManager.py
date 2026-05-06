import json

class StockManager:
    def __init__(self, stock_file):
        self.stock_file = stock_file

    def load_stock(self):
        try:
            with open(self.stock_file, encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    def save_stock(self, data):
        with open(self.stock_file, "w") as f:
            json.dump(data, f, indent=2)