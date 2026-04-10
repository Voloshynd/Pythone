from datetime import datetime, timedelta
from weather_forecast import WeatherForecast


class DateValidator:

    def __init__(self):
        self.weather = WeatherForecast()
        self.today = datetime.now().date()

    def empty_date(self) -> str:
        return (self.today + timedelta(days=1)).strftime("%Y-%m-%d")

    def validate_range(self, month: str, day: str) -> tuple[bool, str | None]:
        if int(month) < 1 or int(month) > 12:
            return False, "Miesiąc musi być w zakresie 01-12."

        if int(day) < 1 or int(day) > 31:
            return False, "Dzień musi być w zakresie 01-31."

        return True, None

    def validate_format_date(self, date: str) -> tuple[bool, str | None]:

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

        is_valid, message = self.validate_range(month, day)
        if not is_valid:
            return is_valid, message

        return True, None
