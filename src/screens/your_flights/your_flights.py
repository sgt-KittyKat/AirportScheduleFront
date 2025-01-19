from flet import *

from components.flight_card import FlightCard
from components.sing_navigation_bar import SingletonNavBar
from features.users.user import User
from screens.your_flights.your_flights_controller import FlightController
from features.flights.flight import Flight
from features.flights.flight_service import FlightService
from utils import constants
from utils.constants import colours, HEAD_FONT_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT
from daos.flight_dao import FlightDao

def your_flights_view(page: Page):
    #flight_service = FlightService(FlightDao())
    user = constants.ADMIN
    flight_controller = FlightController()

    flights = flight_controller.get_user_flights(user)
    flight_cards = [FlightCard(flight, page).get_card() for flight in flights]

    navigation_bar = SingletonNavBar(page).instance

    flights_page = Column(

    )

    return View(
        route = "/your_flights",
        controls = [Container(
                bgcolor=colours["background"],
                expand = True,
                border=border.all(1, color=colours["gray_text"]),
                border_radius=35,
                content=Column(
                    controls=[
                        Column(
                    [
                                Container(
                                    content=Text("Your Flights", size=HEAD_FONT_SIZE),
                                    alignment=alignment.center
                                ),
                                Column(
                                    controls=flight_cards,
                                    spacing=10
                                    ),
                            ],
                            alignment=MainAxisAlignment.START,
                            expand=True,
                        ),
                    navigation_bar
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                )
            )
        ]
    )