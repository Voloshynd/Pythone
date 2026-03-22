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


def check_path(path):
    return os.path.exists(path)


def show_changes(data):
    for row in data:
        print("".join(row).replace(",", " "))


def apply_changes(data, changes):
    for change in changes:
        if len(change.split(",")) < 3:
            continue
        else:
            x, y, value = change.split(",")
            x, y = int(x), int(y)

            line = data[x]
            line = ",".join(line).split(",")
            line[y] = value
            line = [",".join(str(val) for val in line)]
            data[x] = line

    return data


def main():
    if len(sys.argv) < 3:
        print(
            "Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiany...>")
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

    is_exist = check_path(path_file_out)

    if  not is_exist:
        os.open(path_file_out, os.O_CREAT | os.O_WRONLY)
    write_csv(path_file_out, data)

if __name__ == "__main__":
    main()
