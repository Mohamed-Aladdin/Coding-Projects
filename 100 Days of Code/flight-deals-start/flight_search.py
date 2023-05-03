import requests
import datetime
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.KIWI_TOKEN = "Your Token"
        self.KIWI_ENDPOINT = "https://api.tequila.kiwi.com"

        self.kiwi_headers = {
            "apikey": self.KIWI_TOKEN
        }
        self.kiwi_locations_parameters = {
            "location_types": "city",
            "term": ""
        }
        self.kiwi_search_parameters = {
            "fly_from": "CAI",
            "fly_to": "",
            "date_from": (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

    def get_code(self, city):
        self.kiwi_locations_parameters["term"] = city
        response = requests.get(url=f"{self.KIWI_ENDPOINT}/locations/query", headers=self.kiwi_headers, params=self.kiwi_parameters)
        return response.json()["locations"][0]["code"]
    
    def check_flights(self, destination):
        self.kiwi_search_parameters["fly_to"] = destination
        response = requests.get(url=f"{self.KIWI_ENDPOINT}/v2/search", headers=self.kiwi_headers, params=self.kiwi_search_parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            self.kiwi_search_parameters["max_stopovers"] = 2
            response = requests.get(url=f"{self.KIWI_ENDPOINT}/v2/search", headers=self.kiwi_headers, params=self.kiwi_search_parameters)
            data = response.json()["data"][0]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data