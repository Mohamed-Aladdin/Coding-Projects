import smtplib
import datetime as dt
import random

now = dt.datetime.now()
week = now.weekday()

if week == 0:
  with open("quotes.txt") as file:
    quotes_list = file.readlines()

  quote = random.choice(quotes_list)

  my_email = "someemail@gmail.com"
  my_password = "somepassword"

  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
      from_addr="quotemail@yahoo.com",
      to_addrs=my_email,
      msg=f"Subject:Quote of the Day\n\n{quote}"
      )