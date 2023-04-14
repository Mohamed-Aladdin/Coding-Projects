##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random
# 1. Update the birthdays.csv

letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")
print(birthdays_dict)

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
day = now.day
month = now.month

for entry in birthdays_dict:
  if entry["day"] == day and entry["month"] == month:
    chosen_letter = random.choice(letters_list)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

    with open(f"letter_templates/{chosen_letter}") as file:
      letter_contents = file.read()
    new_letter_contents = letter_contents.replace("[NAME]", entry["name"])

# 4. Send the letter generated in step 3 to that person's email address.

    my_email = "someemail@gmail.com"
    my_password = "somepassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(user=my_email, password=my_password)
      connection.sendmail(
        from_addr=my_email,
        to_addrs=entry["email"],
        msg=f"Subject:HappyBirthday!\n\n{new_letter_contents}"
      )




