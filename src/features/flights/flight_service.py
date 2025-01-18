import requests

from daos.flight_dao import FlightDao
from utils.constants import ADMIN, SERVER_LINK


class FlightService:

    def __init__(self):
        #self.flights_dao = FlightDao()
        return

    def get_flights_by_airports(self):
        return ADMIN.upcoming_flights[0]

    def get_flight_data_by_flight_code(self, code):
        response = requests.get(SERVER_LINK, "")
        data = response.json()
        print(data)
        return data



