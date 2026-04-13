import sys
import os
from file_service import JSONHandler, CSVHandler, PKLHandler, TXTHandler


class FileUtiles:

    @staticmethod
    def check_arguments(arguments_list: list) -> None:
        if len(arguments_list) < 3:
            print(
                "Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiany...>")
            sys.exit(1)

    @staticmethod
    def check_path(path: str, message: str) -> None:
        if not os.path.exists(path):
            print(message)
            sys.exit(1)

    @staticmethod
    def get_handler(file_format: str, file_in: str) -> list | None:
        match file_format:
            case "csv":
                handler = CSVHandler(file_in)
                return handler.read_file()
            case "json":
                handler = JSONHandler(file_in)
                return handler.read_file()
            case "pkl":
                handler = PKLHandler(file_in)
                return handler.read_file()
            case "txt":
                handler = TXTHandler(file_in)
                return handler.read_file()
            case _:
                print("Nieznany format pliku")
                return None
