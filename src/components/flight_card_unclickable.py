from components.flight_card import FlightCard
from features.flights.flight import Flight
from flet import *
from utils.constants import colours


class FlightCardUnclickable(FlightCard):
    def __init__(self, flight: Flight, page: Page):
        super().__init__(flight, page)

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

        self.card = Container(
            content=Row(
                [
                    left_section,
                    right_section
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            alignment=alignment.center,
            border=border.all(1, color=colours["gray_text"]),
            border_radius=10,
            padding=padding.only(left=20, right=20, top=5, bottom=5),
        )
        return self.card
