import pandas as pd
from flet.core.page import Page

from features.flights.flight_service import FlightService


class SearchFlightController:
    def __init__(self, page:Page, service: FlightService):
        self.page = page
        self.service = service


    def send_flight_search_request(self, origin, destination):
        return
