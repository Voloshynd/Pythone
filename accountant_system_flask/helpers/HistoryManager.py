import json

class HistoryManager:
    def __init__(self, history_file):
        self.history_file = history_file

    def load_history(self):
        try:
            with open(self.history_file, encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    def save_history(self, data):
        with open(self.history_file, "w") as f:
            json.dump(data, f, indent=2)