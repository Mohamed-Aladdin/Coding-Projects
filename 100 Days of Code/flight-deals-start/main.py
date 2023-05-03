#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_search = FlightSearch()
data = DataManager()
notification_manager = NotificationManager()
sheet_data = data.get_price_sheet()

for row in sheet_data["prices"]:
    if not row["iataCode"]:
        row["iataCode"] = flight_search.get_code(row["city"])
        data.set_price_sheet_params(row)
        data.put_price_sheet(row["id"])
    
    flight = flight_search.check_flights(row["iataCode"])
    
    if flight is None:
        continue

    if flight.price < row["lowestPrice"]:
        msg=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_sms(msg) 
        user_entries = data.get_users_sheet()["users"]

        for entry in user_entries:
            notification_manager.send_email(entry["email"], msg)