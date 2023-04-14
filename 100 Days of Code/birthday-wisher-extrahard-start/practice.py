import smtplib
import datetime as dt

# my_email = "someemail@gmail.com"
# my_password = "somepassword"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#   connection.starttls()
#   connection.login(user=my_email, password=my_password)
#   connection.sendmail(from_addr=my_email, to_addrs="someotheremail@yahoo.com", msg="Subject:Testing\n\nThis is a test mail sent by Python.")

# ---------------------------------------------------------------------------- #

now = dt.datetime.now()

year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

birthday = dt.datetime(year=1996, month=3, day=10, hour=4)
print(birthday)