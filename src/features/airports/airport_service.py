from utils.constants import *
import requests

class AirportService:
    def __init__(self):
        return

    def get_airport_by_id(self, id):
        #r = requests.post(DB_PATH, data = {"id":id})
        return DUMMY_AIRPORT

    def get_airport_data_by_icao(self, icao):
        response = requests.get(SERVER_LINK + "/airport-iata/1")
        data = response.json()
        print(data)
        arrivals = data["arrivals"]
        departures = data["departures"]
        return arrivals, departures


