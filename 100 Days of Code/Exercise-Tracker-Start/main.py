import requests
from datetime import datetime
import os

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 175
AGE = 27

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
query = str(input("Tell me which exercises you did: ")).lower()

APP_ID = "Your ID"
API_KEY = "Your API Key"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Nutritionix API Call
nutri_response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_parameters)
exercises = nutri_response.json()["exercises"]

# Adding date and time
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")


# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "Your Sheet's Name (Singular)"
sheet_endpoint = "Your API Endpoint"
SHEETY_TOKEN = "Your Token"

sheet_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in exercises:
    sheet_parameters = {
        GOOGLE_SHEET_NAME: {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Sheety API Call & Authentication
    sheet_response = requests.post(url=sheet_endpoint, headers=sheet_headers, json=sheet_parameters)
    print(sheet_response.text)