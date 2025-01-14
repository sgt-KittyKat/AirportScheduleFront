import datetime

from flet import *
from flet.core.alignment import center

from components.sing_navigation_bar import SingletonNavBar
#from screens.search_flight import search_flight_controller
from utils.constants import *


def search_flight_view(page: Page):
    navigation_bar = SingletonNavBar(page).instance

#    data = search_flight_controller.get_airports_data()

    def submit_button_click(e):
        print("do something")

    headline = Container(
        content = Text("Search flights", size=HEAD_FONT_SIZE),
        alignment = alignment.center,
        margin = margin.only(bottom = 100)
    )

    departure_tf = TextField(
        label = "Departure",
    )
    arrival_tf = TextField (
        label = "Arrival"
    )
    date_pick_button = ElevatedButton(
            "Pick date",
            icon=Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                DatePicker(
                    first_date=datetime.datetime.now(),
                    last_date=datetime.datetime.now(),
                    #on_change=handle_change,
                    #on_dismiss=handle_dismissal,
                )
            ),
        )
    submit_button = ElevatedButton(
        "Search flights",
        on_click = submit_button_click,
    )

    return Container(
        bgcolor=colours["background"],
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        border=border.all(1, color=colours["gray_text"]),
        border_radius=35,
        content = Column(
            controls = [
                Container(
                    content= Column(
                        controls = [
                            headline,
                            departure_tf,
                            arrival_tf,
                            date_pick_button,
                            submit_button
                        ],
                        horizontal_alignment = CrossAxisAlignment.CENTER,
                        spacing = 30
                    ),
                    padding=20,
                    #border_radius=10,
                    #border=border.all(1, colors.LIGHT_GREEN),
                    expand=True
                ),
                navigation_bar
            ]
        )
    )