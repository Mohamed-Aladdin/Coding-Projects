import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.SHEET_TOKEN = "Your Token"
        self.PRICE_SHEET_ENDPOINT = "Your Sheet's Endpoint"
        self.USERS_SHEET_ENDPOINT = "Your Sheet's Endpoint"
        
        self.sheet_headers = {
        'Authorization': f"Bearer {self.SHEET_TOKEN}"
        }
        self.prices_parameters = {
            "price": {}
        }
        self.users_parameters = {
            "user": {}
        }

    def set_price_sheet_params(self, params):
        self.prices_parameters["price"] = params

    def get_price_sheet(self):
        response = requests.get(url=self.PRICE_SHEET_ENDPOINT, headers=self.sheet_headers)
        return response.json()
    
    def put_price_sheet(self, id):
        response = requests.put(url=f"{self.PRICE_SHEET_ENDPOINT}/{id}", headers=self.sheet_headers, json=self.prices_parameters)
        print(response.text)
    
    def set_user_sheet_params(self, params):
        self.users_parameters["user"] = params

    def get_users_sheet(self):
        response = requests.get(url=self.USERS_SHEET_ENDPOINT, headers=self.sheet_headers)
        return response.json()
    
    def post_users_sheet(self):
        response = requests.post(url=self.USERS_SHEET_ENDPOINT, headers=self.sheet_headers, json=self.users_parameters)
        print(response.text)