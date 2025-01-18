from daos.flight_dao import FlightDao
from utils.constants import ADMIN


class FlightService:

    def __init__(self):
        #self.flights_dao = FlightDao()
        return

    def get_flights_by_airports(self):
        return ADMIN.upcoming_flights[0]



