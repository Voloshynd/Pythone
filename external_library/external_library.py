from validators import empty_date, validate_format_date
from api_service import make_request
import os
from file_manager import read_results

def start_app():
    print("Podaj datę dla jakiej należy sprawdzić pogodę")

    searched_date = None

    while True:
        date_input = input(
            "Podaj datę w formacie YYYY-MM-DD (np. 2022-11-03): ").strip()

        if not date_input:
            searched_date = empty_date().strftime("%Y-%m-%d").strip()
            break

        is_valid, message = validate_format_date(date_input)

        if is_valid:
            searched_date = date_input.strip()
            break
        else:
            print(message)


    def get_date(date: str) -> list | None:
        if not os.path.exists("results.csv"):
            return None

        results = read_results()

        for row in results:
            if row[0].strip() == date.strip():
                return row

        return None


    def print_result(record: list, date: str) -> None:
        print(f"Szukana data - {date} znajduje się w pliku")
        print("=" * 30)
        print(record[0] + " - " + record[1])

    result = get_date(searched_date)


    if result:
        print_result(result, searched_date)
    else:
        make_request(searched_date)

start_app()