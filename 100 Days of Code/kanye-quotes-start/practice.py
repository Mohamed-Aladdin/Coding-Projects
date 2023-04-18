import requests
from datetime import datetime

# url = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url)
# response.raise_for_status()

# data = response.json()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_coordinates = (longitude, latitude)
# print(iss_coordinates)

url = "https://api.sunrise-sunset.org/json"

MY_LAT = 30.044420
MY_LNG = 31.235712

parameters = {
  "lat": MY_LAT,
  "lng": MY_LNG,
  "formatted": 0
}

response = requests.get(url, params=parameters)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

now = datetime.now()
print(now.hour)