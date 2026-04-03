from datetime import datetime, timedelta
from api_service import fetch_weather_data

today = datetime.now().date()


def empty_date():
    return today + timedelta(days=1)


def validate_range(month: str, day: str) -> tuple[bool, str | None]:
    if int(month) < 1 or int(month) > 12:
        return False, "Miesiąc musi być w zakresie 01-12."

    if int(day) < 1 or int(day) > 31:
        return False, "Dzień musi być w zakresie 01-31."

    return True, None


def validate_year(searched_date: str) -> tuple[bool, str | None]:
    response = fetch_weather_data(searched_date)

    if response and response.get("error"):
        msg = response.get("reason")

        msg_part = msg.split("from")[1]

        date_from = datetime.strptime(
            msg_part.split("to")[0].strip(), "%Y-%m-%d"
        ).date()

        date_to = datetime.strptime(
            msg_part.split("to")[1].strip(), "%Y-%m-%d"
        ).date()

        user_date = datetime.strptime(searched_date, "%Y-%m-%d").date()

        if not (date_from <= user_date <= date_to):
            return False, f"Data musi być w zakresie {date_from} - {date_to}!"

    return True, None


def validate_format_date(date: str) -> tuple[bool, str | None]:
    parts = date.split("-")

    if len(parts) != 3:
        return False, "Niepoprawny format. Użyj YYYY-MM-DD."

    year, month, day = parts

    if not year.isdigit() or len(year) != 4:
        return False, "Rok musi mieć 4 cyfry."
    if not month.isdigit() or len(month) != 2:
        return False, "Miesiąc musi mieć 2 cyfry."
    if not day.isdigit() or len(day) != 2:
        return False, "Dzień musi mieć 2 cyfry."

    is_valid, message = validate_year(date)
    if not is_valid:
        return is_valid, message

    is_valid, message = validate_range(month, day)
    if not is_valid:
        return is_valid, message

    return True, None
