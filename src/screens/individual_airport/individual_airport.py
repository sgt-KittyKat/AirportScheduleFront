from flet import *
from flet.core.alignment import center

from features.airports.airport_service import AirportService
from features.users.user_service import UserService
from screens.individual_airport import ind_airport_controller
from screens.login_page.login_page_controller import LoginPageController
from utils import constants
from components.airport_card import AirportCard
from components.sing_navigation_bar import SingletonNavBar
from features.airports.airport import Airport
from utils.constants import *
from screens.airports import airports_controller

def airport_template_view(page: Page, airport: Airport):

    navigation_bar = SingletonNavBar(page).instance
    controller = ind_airport_controller.IndividualAirportController(page, AirportService())
    arrivals_data, departures_data = controller.get_airport_data(airport)
    arrivals_list = ListView(
        controls=arrivals_data,
        visible=True,
        auto_scroll=True,
        spacing=5
    )
    departures_list = ListView(
        controls=departures_data,
        visible=False,
        auto_scroll = True,
        spacing = 5
    )

    # Function to toggle visibility
    def show_arrivals(e):
        arrivals_list.visible = True
        departures_list.visible = False
        page.update()

    def show_departures(e):
        arrivals_list.visible = False
        departures_list.visible = True
        page.update()

    arrivals_button = ElevatedButton(text="Arrivals", on_click=show_arrivals)
    departures_button = ElevatedButton(text="Departures", on_click=show_departures)

    # Row to hold buttons
    buttons_row = Row(
        controls=[arrivals_button, departures_button],
        alignment = MainAxisAlignment.CENTER
                      )

    # Main container
    departures_arrivals_switch = Container(
        content=Column(
            controls=[
                buttons_row,
                arrivals_list,
                departures_list,
            ],
            auto_scroll=True,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    return View(
            route = page.route,
            controls = [
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
                                    content=Text(airport.name, size=HEAD_FONT_SIZE),
                                    alignment=alignment.center,
                                    margin = margin.only(bottom = 50)
                                ),
                                departures_arrivals_switch
                            ],
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            expand=True,
                        ),
                        navigation_bar,
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                )
            )
        ]
    )