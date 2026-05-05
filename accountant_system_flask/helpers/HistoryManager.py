import json

class HistoryManager:
    def __init__(self):
        self.history_file = "data/history.json"

    def load_history(self):
        try:
            with open(self.history_file) as f:
                return json.load(f)
        except:
            return []

    def save_history(self, data):
        with open(self.history_file, "w") as f:
            json.dump(data, f, indent=2)