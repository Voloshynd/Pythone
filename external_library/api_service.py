import requests
from urllib.parse import urlparse, parse_qs
from api_url import api_url as url
from geopy.geocoders import Nominatim
from get_status import get_rain_status
from file_manager import write_results
from deep_translator import GoogleTranslator


def fetch_weather_data(searched_date: str):
    city = None
    latitude = None
    longitude = None

    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)

    for key, value in params.items():
        if key == "timezone":
            zone = value[0]
            idx = zone.find("/")
            city = zone[idx + 1:].strip()
            break

    geolocator = Nominatim(user_agent="external_library")
    location = geolocator.geocode(city)

    if not location:
        print("Nie znaleziono miasta")
        return None

    latitude = location.latitude
    longitude = location.longitude

    correct_url = url.format(
        latitude=latitude,
        longitude=longitude,
        searched_date=searched_date
    )

    try:
        response = requests.get(correct_url)
        return response.json()
    except Exception as e:
        print("Błąd połączenia z API:", e)
        return None


def make_request(searched_date: str):
    data = fetch_weather_data(searched_date)

    if not data:
        return

    if data.get('error'):
        msg = data.get('reason')
        translation = GoogleTranslator(source='auto', target='pl').translate(
            msg)
        print(translation)
        return

    try:
        daily = data.get('daily')
        selected_date = daily['time'][0]
        status = get_rain_status(data)

        write_results(selected_date, status)
        print(selected_date + " - " + status)

    except (KeyError, IndexError, TypeError):
        print("Brak danych pogodowych")
