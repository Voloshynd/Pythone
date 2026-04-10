from weather_forecast import WeatherForecast
from pathlib import Path
from date_validator import DateValidator
from variables import OPERATIONS, FILE_PATH


def main():
    weather_forecast = WeatherForecast()
    validator = DateValidator()
    searched_date = None
    app_is_running = True
    data_file = Path(FILE_PATH)

    print("Dostępne operacje:")
    print("\n".join(f"- {operation}" for operation in OPERATIONS))

    while app_is_running:
        user_option = input("Proszę wprowadzić komendę: ").lower().strip()

        while user_option not in OPERATIONS:
            user_option = input(
                "Niepoprawna komenda. Spróbuj ponownie: ").lower().strip()

        match user_option:
            case "get":
                print("Podaj datę dla jakiej należy sprawdzić pogodę")
                while True:
                    user_date = input(
                        "Datę należy podać w formacie YYYY-MM-DD (np. 2022-11-03): "
                    ).strip()

                    if not user_date:
                        searched_date = validator.empty_date()
                    else:
                        is_valid, message = validator.validate_format_date(
                            user_date)

                        if not is_valid:
                            print(message)
                            continue

                        searched_date = user_date

                    data = weather_forecast.read_file()

                    if searched_date in data:
                        print(
                            f"Szukana data - {searched_date} znajduje się w pliku")
                        print("=" * 30)
                        print(f"{searched_date} - {data[searched_date]}")
                        break

                    response = weather_forecast[searched_date]

                    if response is None:
                        print("Spróbuj podać inną datę.")
                        continue

                    date, weather = response
                    print(f"{date} - {weather}")
                    break

            case "iterate":
                data = list(weather_forecast)
                if not len(data):
                    print("Na razie nie ma zapisów w pliku")
                else:
                    print("Wszystkie daty, dla których znana jest pogoda:")
                    for date in weather_forecast:
                        print(date)

            case "items":
                if not list(weather_forecast):
                    print("Na razie nie ma zapisów w pliku")
                else:
                    for date, weather in weather_forecast.items():
                        print(date, weather)

            case "end":
                print("Aplikacja została pomyślnie zamknięta")
                break


main()
