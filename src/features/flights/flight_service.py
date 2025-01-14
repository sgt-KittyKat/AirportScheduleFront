from daos.flight_dao import FlightDao

class FlightService:

    def __init__(self, flights_dao):
        self.flights_dao = FlightDao()

    def get_flights_by_airports(self):
        return self.flights_dao.get_flights_by_airports()

    def update(self, flight):
        return self.flights_dao.update_flight()
