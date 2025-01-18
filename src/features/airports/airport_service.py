from utils.constants import *
import requests

class AirportService:
    def __init__(self):
        return



    def get_airport_data_by_iata(self, iata):
        response = requests.get(SERVER_LINK + "/airport-iata/" + iata)
        data = response.json()
        print(data)
        arrivals = data["arrivals"]
        departures = data["departures"]
        return arrivals, departures


