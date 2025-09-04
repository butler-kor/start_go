import requests
import json

weather_apikey = '8aeac4a34033dddda3560c8df1873c4b'
url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={weather_apikey}"

response = requests.get(url).json()
print(response["weather"])
print(type(response["weather"][0]["main"]))
lang = "kr"
country = "icheon-si"

weather_api = f"""https://api.openweathermap.org/\
data/2.5/weather?q={country}&appid={weather_apikey}&lang={lang}"""


response = requests.get(weather_api).json()
print(response)

# https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=8aeac4a34033dddda3560c8df1873c4b