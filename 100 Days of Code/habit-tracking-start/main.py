import requests
from datetime import datetime

USERNAME = "My Username"
TOKEN = "My Token"
GRAPH_ID = "My Graph ID"

def create_user():
    pixela_api = "https://pixe.la/v1/users"

    user_parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_api, json=user_parameters)
    print(response.text)

def create_graph():
    pixela_api = f"https://pixe.la/v1/users/{USERNAME}/graphs"

    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    graph_parameters = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "minutes",
        "type": "float",
        "color": "sora",
        "timezone": "Africa/Cairo"
    }

    response = requests.post(url=pixela_api, json=graph_parameters, headers=graph_headers)
    print(response.text)

def post_pixel():
    pixel_api = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    graph_parameters = {
        "date": "20230428",
        "quantity": "360"
    }

    response = requests.post(url=pixel_api, json=graph_parameters, headers=graph_headers)
    print(response.text)

def update_pixel():
    pixel_api = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20230429"

    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    graph_parameters = {
        "quantity": "300"
    }

    response = requests.put(url=pixel_api, json=graph_parameters, headers=graph_headers)
    print(response.text)

def delete_pixel():
    pixel_api = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20230428"

    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=pixel_api, headers=graph_headers)
    print(response.text)