from flet import *

from features.airports.airport_service import AirportService
from features.flights.flight_service import FlightService
from screens.add_flight.add_flight import add_flight_view
from screens.airports.airports import airports_view
from screens.individual_flight.ind_flight_controller import IndividualFlightController
from screens.login_page.login_page import login_view
from screens.register_page.register_page import register_view
from screens.search_flight.search_flight import search_flight_view
from screens.upload_ticket.upload_ticket import upload_ticket_view
from screens.your_flights.your_flights import your_flights_view
from utils.constants import *
from screens.individual_airport.ind_airport_controller import IndividualAirportController


class Navigator:
    def __init__(self, page):
        self.page = page
        self.pages = {
        "/your_flights": your_flights_view(page),
        "/add_flight": add_flight_view(page),
        "/add_flight/upload_a_ticket": upload_ticket_view(page),
        "/add_flight/search_your_journey": search_flight_view(page),
        "/airports": airports_view(page),
        "/login_page" : login_view(page),
        "/register_page": register_view(page)
    }

    def route_change(self, route):
        # Clear the views and update the current route content
        airports_controller = IndividualAirportController(self.page, AirportService())
        flight_controller = IndividualFlightController(self.page, FlightService())
        self.page.views.clear()
        #print(route)
        if route.route in self.pages:
            self.page.views.append(
                self.pages[self.page.route]
            )
        elif "airport" in route.route:
            parts = route.route.split("/")
            code = ""
            for part in parts:
                if part.startswith("id="):
                    code = str(part.split("=")[1])
                    break

            self.page.views.append(airports_controller.generate_airport_page(code))
        elif "flights" in route.route:
            parts = route.route.split("/")
            id_value = 0
            for part in parts:
                if part.startswith("id="):
                    id_value = int(part.split("=")[1])
                    break

            self.page.views.append(flight_controller.generate_flight_page())
        self.page.update()
        print("Route has changed:", route)