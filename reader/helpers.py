import csv
import sys
import os


def read_csv(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def write_csv(path: str, data: list) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def check_path(path: str, message: str) -> None:
    if not os.path.exists(path):
        print(message)
        sys.exit(1)


def show_changes(data: list) -> None:
    for row in data:
        print("".join(row).replace(",", " "))


def apply_changes(data: list, changes: list) -> list:
    for change in changes:
        if len(change.split(",")) < 3:
            continue
        else:
            x, y, value = change.split(",")
            x, y, = int(x), int(y)

            row = data[y][0]
            row_list = row.split(",")
            row_list[x] = value
            row_list = [",".join(str(val) for val in row_list)]
            data[y] = row_list

    return data
