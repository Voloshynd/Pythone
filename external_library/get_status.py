def get_rain_status(data: dict) -> str:
    try:
        rain = data["daily"]["rain_sum"][0]

        if rain > 0.0:
            return "Będzie padać"
        elif rain == 0.0:
            return "Nie będzie padać"
        else:
            return "Nie wiem"
    except ValueError:
        return "Nie wiem"
