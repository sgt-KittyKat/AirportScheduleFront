from components.flight_card import FlightCard
from features.flights.flight import Flight
from flet import *

from utils.constants import colours


class FlightCardUnclickable(FlightCard):
    def __init__(self, flight: Flight, page):
        super().__init__(flight, page)

    def build(self):
        self.card = Container(
            content=Row(
                [
                    # Left Section: Outbound, Destination, Time
                    Column(
                        [
                            Text(f"{self.flight.origin} → {self.flight.destination}",
                                 size=20, weight=FontWeight.BOLD),
                            Text(f"{self.flight.departure_time} - {self.flight.arrival_time}", size=16,
                                 weight=FontWeight.BOLD),
                            #Text(self.flight.departure_date, size=16, weight=FontWeight.BOLD),
                        ],
                        alignment=MainAxisAlignment.START,
                        spacing=5,
                    ),
                    # Right Section: Date and Flight Number
                    Column(
                        [
                            Text(self.flight.flight_number, size=16, weight=FontWeight.BOLD),
                            #Text(self.flight.airline, size=14, color=colors.GREY_600),
                            #Text(self.flight.aircraft, size=14, color=colors.GREY_600),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.END,
                    )
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
             alignment=alignment.center,
             border=border.all(1, color=colours["gray_text"]),
             border_radius=10,
             padding=padding.only(left=20, right=20, top=5, bottom=5)
        )
        return self.card
