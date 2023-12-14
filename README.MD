# weatherallapi

Библиотека для получения данных о погоде.

## Установка

pip install weatherallapi

##Использование

weatherallapi использует openweathermap

##Пример

from weatherallapi import WeatherAPI

# Создайте экземпляр класса
weatherallapi = WeatherAPI()

# Укажите город (в данном случае, Кривой Рог)
weatherallapi.city = "Кривой Рог"

# Получите данные о погоде
weather_response = weatherallapi.get_weather()

# Выведите результат
print(f"Погода в Кривом Роге: {weather_response}")# all-weather-api
