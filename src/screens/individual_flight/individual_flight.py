from flet import *
from flet.core.alignment import center

from features.users.user_service import UserService
from screens.login_page.login_page_controller import LoginPageController
from utils import constants
from components.airport_card import AirportCard
from components.sing_navigation_bar import SingletonNavBar
from features.airports.airport import Airport
from utils.constants import *
from screens.airports import airports_controller

from flet import *
from flet.core.alignment import center
from components.sing_navigation_bar import SingletonNavBar
from utils.constants import colours, WINDOW_WIDTH, WINDOW_HEIGHT, HEAD_FONT_SIZE


def flight_template_view(page: Page, flight: Flight):
    navigation_bar = SingletonNavBar(page).instance

    # Circular "GO TO GATE" widget
    go_to_gate_circle = Container(
        width=300,
        height=300,
        border_radius=150,
        bgcolor=colours["login_text"],  # Blue background for the circle
        alignment=alignment.center,
        content=Container(
            width = 200,
            height = 200,
            border_radius=100,
            bgcolor= colors.WHITE,
            alignment=alignment.center,
            content = Text(
                flight.status,
                size=20,
                weight="bold",
                #color=colours["background"],  # White text
            ),
            #margin=margin.only(bottom=30),
        )
    )

    # Flight information card
    flight_info_card = Container(
        content=Column(
            controls=[
                Text("Flight information", size=16,),
                Text(f"Flight: {flight.origin} -> {flight.destination} {flight.flight_number}"),
                Text(f"Time: {flight.departure_time} - {flight.arrival_time}"),
                Text(f"Airline: {flight.airline}"),
                Text(f"Aircraft: {flight.aircraft}"),
            ],
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
                width=WINDOW_WIDTH,
                height=WINDOW_HEIGHT,
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
                                go_to_gate_circle,  # Add circular widget here
                                flight_info_card,  # Add flight info card here
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
