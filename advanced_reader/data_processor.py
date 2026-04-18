import csv

class DataProcessor:
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

