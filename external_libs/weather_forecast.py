from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse, parse_qs
from api_url import API_URL
from geopy.geocoders import Nominatim
import json
from variables import FILE_PATH
from deep_translator import GoogleTranslator
import os


class WeatherForecast:

    def __init__(self):
        self.file_path = FILE_PATH

    def read_file(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def write_file(self, new_data: str, weather: float) -> None:
        status = self.get_rain_status(weather)
        data = self.read_file()
        data[new_data] = status
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def fetch_weather_data(self, searched_date: str) -> None | dict:
        city = None
        latitude = None
        longitude = None

        parsed_url = urlparse(API_URL)
        params = parse_qs(parsed_url.query)

        for key, value in params.items():
            if key == "timezone":
                zone = value[0]
                city = zone.split("/")[-1].replace("_", " ")
                break

        geolocator = Nominatim(user_agent="external_library")
        location = geolocator.geocode(city)

        if not location:
            print("Nie znaleziono miasta")
            return None

        latitude = location.latitude
        longitude = location.longitude

        correct_url = API_URL.format(
            latitude=latitude,
            longitude=longitude,
            searched_date=searched_date
        )

        try:
            response = urlopen(correct_url)
            data = response.read()
            weather = data.decode("utf-8")
            data_weather = json.loads(weather)
            return data_weather
        except HTTPError as e:
            error_data = e.read().decode("utf-8")
            error_json = json.loads(error_data)
            return error_json

    def make_request(self, searched_date: str) -> str | None | tuple:
        data_weather = self.fetch_weather_data(searched_date)

        if data_weather.get('error'):
            msg = data_weather.get('reason')
            translation = GoogleTranslator(source='auto',
                                           target='pl').translate(
                msg)
            print(translation)
            return None

        if data_weather is None:
            return None

        try:
            searched_date = data_weather['daily']['time'][0]
            weather = data_weather['daily']['rain_sum'][0]
            self.__setitem__(searched_date, weather)
            return searched_date, self.get_rain_status(weather)
        except IndexError:
            print("Brak danych pogodowych")
            return None


    def get_rain_status(self, status: float) -> str:
        if status > 0.0:
            return "Będzie padać"
        elif status == 0.0:
            return "Nie będzie padać"
        else:
            return "Nie wiem"


    def __getitem__(self, searched_date: str) -> tuple:
        data = self.read_file()
        if searched_date in data:
            return data[searched_date]

        return self.make_request(searched_date)


    def __setitem__(self, date: str, weather: float) -> None:
        self.write_file(date, weather)


    def __iter__(self):
        data = self.read_file()
        return iter(data or [])


    def items(self):
        data = self.read_file()
        for k, v in data.items():
            yield (k, v)


weather_forecast = WeatherForecast()
