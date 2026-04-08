from validators import empty_date, validate_format_date
from api_service import make_request
import os
from file_manager import read_results


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


def start_app():
    print("Podaj datę dla jakiej należy sprawdzić pogodę")

    searched_date = None

    while True:

        date_input = input("Podaj datę (YYYY-MM-DD): ").strip()

        if not date_input:
            searched_date = empty_date().strftime("%Y-%m-%d")
        else:
            is_valid, message = validate_format_date(date_input)
            if not is_valid:
                print(message)
                continue
            searched_date = date_input

        result = get_date(searched_date)

        if result:
            print_result(result, searched_date)
            break

        success = make_request(searched_date)

        if success:
            break


start_app()
