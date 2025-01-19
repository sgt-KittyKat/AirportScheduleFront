from components.flight_card import FlightCard
from flet import *

from features.flights.flight import Flight
from utils.constants import colours


class FlightCardAddable(FlightCard):
    def __init__(self, flight: Flight, page: Page):
        super().__init__(flight, page)

    #def add_to_upcoming_flights(self):


    def build(self):
        self.card = OutlinedButton(
            content=Row(
                [
                    # Left Section: Outbound, Destination, Time
                    Column(
                        [
                            Text(f"{self.flight.origin} → {self.flight.destination}",
                                 size=20, weight=FontWeight.BOLD),
                            Text(f"{self.flight.departure_time} - {self.flight.arrival_time}", size=16,
                                 weight=FontWeight.BOLD),
                            # Text(self.flight.departure_date, size=16, weight=FontWeight.BOLD),
                        ],
                        alignment=MainAxisAlignment.START,
                        spacing=5,
                    ),
                    # Right Section: Date and Flight Number
                    Column(
                        [
                            Text(self.flight.flight_number, size=16, weight=FontWeight.BOLD),
                            # Text(self.flight.airline, size=14, color=colors.GREY_600),
                            # Text(self.flight.aircraft, size=14, color=colors.GREY_600),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.END,
                    )
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            on_click=lambda e: self.page.go(self.destination_page)
            # alignment=alignment.center,
            # border=border.all(1, color=colours["gray_text"]),
            # border_radius=10,
            # padding=padding.only(left=20, right=20, top=5, bottom=5)
        )
        return self.card

