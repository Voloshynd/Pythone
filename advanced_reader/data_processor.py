import json
import csv
import pickle


class Processor:
    def __init__(self, data: list, changes: list) -> None:
        self.data = data
        self.changes = changes

    def apply_changes(self) -> None:
        for change in self.changes:
            parts = change.split(",")
            if len(parts) != 3:
                continue

            x, y, value = parts
            x, y = int(x), int(y)

            if y < len(self.data) and x < len(self.data[y]):
                self.data[y][x] = value

    def show(self) -> None:
        for row in self.data:
            print(", ".join(map(str, row)))

    def save_csv(self, path: str) -> None:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


class BaseHandler:
    def __init__(self, file_in: str) -> None:
        self.file_in = file_in

    def read_file(self) -> list:
        with open(self.file_in, "r", encoding="utf-8") as f:
            content = f.read()
            data = [line.split(",") for line in content.split("\n")]
            return data


class CSVHandler(BaseHandler):
    def read_file(self) -> list:
        with open(self.file_in, newline="", encoding="utf-8") as f:
            data_list = list(csv.reader(f))
            data = [[item.strip() for item in row] for row in data_list]
            return data


class JSONHandler(BaseHandler):
    def read_file(self) -> list:
        with open(self.file_in, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data


class PKLHandler(BaseHandler):
    def read_file(self) -> list:
        with open(self.file_in, "rb") as f:
            data = pickle.load(f)
            return data
