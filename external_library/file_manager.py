import csv


def write_results(selected_date, status):
    with open("results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([selected_date, status])


def read_results():
    with open("results.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


