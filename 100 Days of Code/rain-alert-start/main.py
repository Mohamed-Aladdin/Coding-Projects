import requests

MY_LAT = 30.044420
MY_LONG = 31.235712
API_KEY = "7b194fbbfcefacc4bec7c9d6a16427fd"

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in range(0, 3):
    hourly_condition = int(weather_data["list"][hour]["weather"][0]["id"])
    
    if hourly_condition < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")