# python managment_csv.py in.csv out.csv 0,0,gitara 3,1,kubek

import csv
import sys
import os


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def write_csv(path, data):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def show_changes(data):
    for row in data:
        print(" | ".join(row))


def apply_changes(data, changes):
    for change in changes:
        x, y, value = change.split(",")
        x, y = int(x), int(y)

        if not x or not y or not value:
            continue
        else:
            line = data[x]
            line= ",".join(line).split(",")
            line[y] = value
            line = [",".join(str(val) for val in line)]
            data[x] = line

    return data


def main():
    if len(sys.argv) < 3:
        print("Użycie: python managment_csv.py <plik_wejsciowy> <plik_wyjsciowy> <zmiany...>")
        sys.exit(1)

    path_file_in = sys.argv[1]
    path_file_out = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.exists(path_file_in):
        print(f"Plik '{path_file_in}' nie istnieje.")
        sys.exit(1)

    if not path_file_out.endswith(".csv"):
        path_file_out = "out.csv"

    data = read_csv(path_file_in)
    data = apply_changes(data, changes)
    show_changes(data)
    write_csv(path_file_out, data)


if __name__ == "__main__":
    main()