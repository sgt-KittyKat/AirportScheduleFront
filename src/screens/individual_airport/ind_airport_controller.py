from components.flight_card_unclickable import FlightCardUnclickable
from features.airports.airport import Airport
from features.airports.airport_service import AirportService
from app import navigation
from flet import *

from features.flights.flight import Flight
from screens.individual_airport import individual_airport

class IndividualAirportController:
    def __init__(self, page:Page , service: AirportService):
        self.page = page
        self.service = service
        return

    def request_airport_data_by_code(self, code:str):
        return

    def generate_airport_page(self, id):
        airport = self.service.get_airport_by_id(id)
        return individual_airport.airport_template_view(self.page, airport)

    def get_airport_data(self, airport:Airport):
        icao = airport.icao
        arrivals, departures = self.service.get_airport_data_by_icao(icao)
        arrival_flight_cards = [FlightCardUnclickable(Flight(**arrival), self.page).get_card() for arrival in arrivals]
        departure_flight_cards = [FlightCardUnclickable(Flight(**departure), self.page).get_card() for departure in departures]
        return arrival_flight_cards, departure_flight_cards


