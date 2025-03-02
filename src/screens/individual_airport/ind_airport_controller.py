from datetime import datetime

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
            print(airport[0])
            if airport[0] == iata_code:  # The first element is iata_code
                return {"iata": airport[0], "name": airport[1], "city": airport[2]}
        return None  # Return None if not found


    def generate_airport_page(self, iata):
        airport = Airport(**self.find_airport_by_iata(iata))
        return individual_airport.airport_template_view(self.page, airport)


    def get_airport_data(self, airport:Airport):
        iata = airport.iata
        current_time = datetime.now().strftime("%H:%M")
        arrivals, departures = self.service.get_airport_data_by_iata(iata)
        arrival_flight_cards = [FlightCardUnclickable(Flight(**arrival), self.page).get_card() for arrival in arrivals if arrival["arrival_time"] is not None and arrival["arrival_time"] > current_time]
        departure_flight_cards = [FlightCardUnclickable(Flight(**departure), self.page).get_card() for departure in departures if departure["departure_time"] is not None and departure["departure_time"] > current_time]
        return arrival_flight_cards, departure_flight_cards


