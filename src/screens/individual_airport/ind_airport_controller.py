from components.flight_card_unclickable import FlightCardUnclickable
from features.airports.airport import Airport
from features.airports.airport_service import AirportService
from app import navigation
from flet import *

from features.flights.flight import Flight
from screens.individual_airport import individual_airport
from utils import constants


class IndividualAirportController:
    def __init__(self, page:Page , service: AirportService):
        self.page = page
        self.service = service
        return

    #def request_airport_data_by_code(self, code:str):

     #   return

    def find_airport_by_iata(self, iata_code):
        airports = constants.AIRPORTS_DATA
        for airport in airports:
            if airport.get('iata_code') == iata_code:
                return airport
        return None  # Return None if not found


    def generate_airport_page(self, iata):
        airport = Airport(**self.find_airport_by_iata(iata))
        return individual_airport.airport_template_view(self.page, airport)


    def get_airport_data(self, airport:Airport):
        icao = airport.icao
        arrivals, departures = self.service.get_airport_data_by_icao(icao)
        arrival_flight_cards = [FlightCardUnclickable(Flight(**arrival), self.page).get_card() for arrival in arrivals]
        departure_flight_cards = [FlightCardUnclickable(Flight(**departure), self.page).get_card() for departure in departures]
        return arrival_flight_cards, departure_flight_cards


