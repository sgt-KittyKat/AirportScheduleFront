from flet import *

from screens.add_flight.add_flight import add_flight_view
from screens.airports.airports import airports_view
from screens.search_flight.search_flight import search_flight_view
from screens.upload_ticket.upload_ticket import upload_ticket_view
from screens.your_flights.your_flights import your_flights_view


class Navigator:
    def __init__(self, page):
        self.page = page
        self.pages = {
        "/your_flights": View(
            route="/your_flights",
            controls=[
                your_flights_view(page)  # Invoke the function to return Flet controls
            ]
        ),

        "/add_flight": View(
            route="/add_flight",
            controls=[
                add_flight_view(page)
            ]
        ),
        "/add_flight/upload_a_ticket": View(
            route = "/add_flight/upload_a_ticket",
            controls = [
                upload_ticket_view(page)
            ]
        ),
        "/add_flight/search_your_journey": View(
            route = "/add_flight/search_your_journey",
            controls = [
                search_flight_view(page)
            ]
        ),
        "/airports": View(
            route="/airports",
            controls=[
                airports_view(page)
            ]
        ),
    }

    def route_change(self, route):
        # Clear the views and update the current route content
        self.page.views.clear()
        self.page.views.append(
            self.pages[self.page.route]
        )
        self.page.update()
        print("Route has changed:", route)