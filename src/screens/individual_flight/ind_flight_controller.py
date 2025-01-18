from flask import request

from features.flights import flight_service
from app import navigation
from flet import *

import requests
from features.flights.flight_service import FlightService
from screens.individual_flight import individual_flight
from utils.constants import SERVER_LINK


class IndividualFlightController:
    def __init__(self, page:Page , service: FlightService):
        self.page = page
        self.service = service
        return

    def get_flight_data(self, code):
        return self.service.get_flight_data_by_flight_code(code)

    def generate_flight_page(self, code):
        flight = self.get_flight_data(code)
        return individual_flight.flight_template_view(self.page, flight)