from utils.constants import *
import requests

class AirportService:
    def __init__(self):
        return

    def get_airport_by_iata(self, iata):
        for airport in airports:
            if airport.get('iata_code') == iata_code:
                return airport
        return None  # Return None if not found



    def get_airport_data_by_icao(self, icao):
        response = requests.get(SERVER_LINK + "/airport-iata/1")
        data = response.json()
        print(data)
        arrivals = data["arrivals"]
        departures = data["departures"]
        return arrivals, departures


