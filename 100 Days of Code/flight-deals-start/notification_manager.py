import smtplib
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.TWILIO_SID = "Your SID"
        self.TWILIO_TOKEN = "Your Token"
        self.TWILIO_VIRTUAL_NUMBER = "Your Twilio Number"
        self.TWILIO_VERIFIED_NUMBER = "Your Verified Number"
        self.client = Client(self.TWILIO_SID, self.TWILIO_TOKEN)

        self.MY_EMAIL = "email@gmail.com"
        self.MY_PASSWORD = "somepassword"

    def send_sms(self, msg):
        message = self.client.messages.create(
            body = msg,
            from_ = self.TWILIO_VIRTUAL_NUMBER,
            to = self.TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_email(self, email, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASSWORD)
            connection.sendmail(
                from_addr=self.MY_EMAIL,
                to_addrs=email,
                msg=message
            )
