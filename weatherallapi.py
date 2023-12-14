import requests

class WeatherAPI:
    def __init__(self):
        self.city = ""

    def get_weather(self):
        if not self.city:
            return "Укажите город перед запросом погоды."

        # Здесь ты можешь использовать любое API для получения данных о погоде.
        # Например, используем OpenWeatherMap API в этом примере.
        api_key = "4258ef1b085b4ef9915538bb44eecf5d"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}"

        response = requests.get(url)
        weather_data = response.json()

        return weather_data

# Пример использования
if __name__ == "__main__":
    weatherallapi = WeatherAPI()
    weatherallapi.city = "Киев"
    weather_response = weatherallapi.get_weather()

    print(weather_response)