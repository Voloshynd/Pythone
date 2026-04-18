import json
import csv
import pickle


class BaseReader:
    def __init__(self, file_in: str) -> None:
        self.file_in = file_in

    def read_file(self) -> list:
        with open(self.file_in, "r", encoding="utf-8") as f:
            content = f.read()
            data = [line.split(",") for line in content.split("\n")]
            return data


class CSVReader(BaseReader):
    def read_file(self) -> list:
        with open(self.file_in, newline="", encoding="utf-8") as f:
            data_list = list(csv.reader(f))
            data = [[item.strip() for item in row] for row in data_list]
            return data


class JSONReader(BaseReader):
    def read_file(self) -> list:
        with open(self.file_in, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data['data']


class PKLReader(BaseReader):
    def read_file(self) -> list:
        with open(self.file_in, "rb") as f:
            data = pickle.load(f)
            return data
