from flet import *
from features.flights.flight import Flight
from utils.constants import colours


class FlightCard:
    def __init__(self, flight: Flight, page):
        self.page = page
        self.flight = flight
        self.card = None
        self.destination_page = f"/flights/id={flight.flight_number}"

    def build(self):
        left_section = Column(
            [
                Text(f"{self.flight.origin} → {self.flight.destination}", size=20, weight=FontWeight.BOLD),
            ],
            alignment=MainAxisAlignment.START,
            spacing=5,
        )

        if self.flight.departure_time:
            left_section.controls.append(Text(f"Departure Time: {self.flight.departure_time}", size=16, weight=FontWeight.BOLD))
        if self.flight.arrival_time:
            left_section.controls.append(Text(f"Arrival Time: {self.flight.arrival_time}", size=16, weight=FontWeight.BOLD))

        right_section = Column(
            [
                Text(self.flight.flight_number, size=16, weight=FontWeight.BOLD),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.END,
        )

        if self.flight.expected_departure_time:
            right_section.controls.append(Text(f"Expected Departure: {self.flight.expected_departure_time}", size=14, color=colours["gray_text"]))
        if self.flight.expected_arrival_time:
            right_section.controls.append(Text(f"Expected Arrival: {self.flight.expected_arrival_time}", size=14, color=colours["gray_text"]))
        if self.flight.terminal:
            right_section.controls.append(Text(f"Terminal: {self.flight.terminal}", size=14, color=colours["gray_text"]))
        if self.flight.baggage_reclaim_belt:
            right_section.controls.append(Text(f"Baggage Reclaim: {self.flight.baggage_reclaim_belt}", size=14, color=colours["gray_text"]))
        if self.flight.checkin_gate:
            right_section.controls.append(Text(f"Check-in Gate: {self.flight.checkin_gate}", size=14, color=colours["gray_text"]))
        if self.flight.boarding_gate:
            right_section.controls.append(Text(f"Boarding Gate: {self.flight.boarding_gate}", size=14, color=colours["gray_text"]))

        self.card = OutlinedButton(
            content=Row(
                [
                    left_section,
                    right_section
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            on_click=lambda e: self.page.go(self.destination_page),
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10),
            ),
        )

        return self.card

    def update(self, flight):
        self.flight = flight
        self.build()

    def get_card(self):
        if not self.card:
            self.build()
        return self.card
