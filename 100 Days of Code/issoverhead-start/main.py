import requests
from datetime import datetime
import smtplib
import time

def is_nearby():
    global MY_LAT, MY_LONG
    MY_LAT = 30.044420
    MY_LONG = 31.235712

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunrise <= time_now.hour <= sunset:
        return False

def main():
    while True:
        time.sleep(60)
        if is_nearby and is_dark:
            my_email = "someemail@gmail.com"
            my_password = "somepassword"

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="myself@mail.com",
                    msg="Subject:Look up!\n\nThe ISS is above you in the sky"
                )

main()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.