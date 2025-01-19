import json

import requests

from daos.flight_dao import FlightDao
from features.flights.flight import Flight
from utils.constants import ADMIN, SERVER_LINK


class FlightService:

    def __init__(self):
        #self.flights_dao = FlightDao()
        return


    def get_flights_by_airports(self, origin_iata, destination_iata):
        print(origin_iata, destination_iata)
        data = {"origin": origin_iata, "destination": destination_iata}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(SERVER_LINK + "/flights", json.dumps(data), headers=headers)
        print(r.status_code)
        data = r.json()["flights"]
        flights_list = []
        for flight in data:
            print(flight)
            flights_list.append(Flight(**flight))
        return flights_list


    def get_flight_data_by_flight_code(self, code):
        data = {"flight_number": code}
        #print(data)
        headers = {'Content-type': 'application/json', 'Accept': '*'}
        response = requests.post(SERVER_LINK + "/flight", json.dumps(data), headers=headers)
        #print(response.content)
        data = response.json()
        #print(data)
        return data
