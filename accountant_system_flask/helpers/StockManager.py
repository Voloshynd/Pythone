import json

class StockManager:
    def __init__(self):
        self.stock_file = "data/stock.json"

    def load_stock(self):
        try:
            with open(self.stock_file) as f:
                return json.load(f)
        except:
            return {}

    @staticmethod
    def save_stock(self, data):
        with open(self.stock_file, "w") as f:
            json.dump(data, f)