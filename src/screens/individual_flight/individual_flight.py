from flet import *
from flet.core.alignment import center
from components.sing_navigation_bar import SingletonNavBar
from features.flights.flight import Flight
from utils.constants import colours, WINDOW_WIDTH, WINDOW_HEIGHT, HEAD_FONT_SIZE


def flight_template_view(page: Page, flight: Flight):
    navigation_bar = SingletonNavBar(page).instance


    go_to_gate_circle = Container(
        width=300,
        height=300,
        border_radius=150,
        bgcolor=colours["login_text"],
        alignment=alignment.center,
        content=Container(
            width=200,
            height=200,
            border_radius=100,
            bgcolor=colors.WHITE,
            alignment=alignment.center,
            content=Text(
                flight.status,
                size=20,
                weight="bold",
            ),
        ),
    )


    flight_details = [
        Text(f"Flight: {flight.origin} -> {flight.destination} ({flight.flight_number})"),
        Text(f"Time: {flight.departure_time} - {flight.arrival_time}"),
    ]

    # Add optional fields if they are not None
    if flight.expected_departure_time:
        flight_details.append(Text(f"Expected Departure: {flight.expected_departure_time}"))
    if flight.expected_arrival_time:
        flight_details.append(Text(f"Expected Arrival: {flight.expected_arrival_time}"))
    if flight.terminal:
        flight_details.append(Text(f"Terminal: {flight.terminal}"))
    if flight.baggage_reclaim_belt:
        flight_details.append(Text(f"Baggage Reclaim Belt: {flight.baggage_reclaim_belt}"))
    if flight.checkin_gate:
        flight_details.append(Text(f"Check-in Gate: {flight.checkin_gate}"))
    if flight.boarding_gate:
        flight_details.append(Text(f"Boarding Gate: {flight.boarding_gate}"))


    flight_info_card = Container(
        content=Column(
            controls=[Text("Flight Information", size=16, weight="bold")] + flight_details,
            spacing=5,
        ),
        padding=15,
        border_radius=10,
        border=border.all(1, colours["gray_text"]),
        margin=margin.only(bottom=30),
    )

    return View(
        route=page.route,
        controls=[
            Container(
                bgcolor=colours["background"],
                expand=True,
                border=border.all(1, color=colours["gray_text"]),
                border_radius=35,
                content=Column(
                    controls=[
                        Column(
                            [
                                Container(
                                    content=Text(
                                        f"{flight.origin} -> {flight.destination}",
                                        size=HEAD_FONT_SIZE,
                                    ),
                                    alignment=alignment.center,
                                    margin=margin.only(bottom=30),
                                ),
                                go_to_gate_circle,
                                flight_info_card,
                            ],
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            expand=True,
                        ),
                        navigation_bar,
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
            )
        ],
    )
