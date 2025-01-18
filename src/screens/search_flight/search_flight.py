import datetime

from flet import *
from flet.core.alignment import center

from components.sing_navigation_bar import SingletonNavBar
from screens.airports import airports_controller
#from screens.search_flight import search_flight_controller
from utils.constants import *


def search_flight_view(page: Page):
    navigation_bar = SingletonNavBar(page).instance

    data = airports_controller.get_airports_data()

    def submit_button_click(e):
        print("do something")

    headline = Container(
        content=Text("Search flights", size=HEAD_FONT_SIZE),
        alignment=alignment.center,
        margin=margin.only(bottom=100),
    )

    departure_tf = TextField(
        label="Departure",
        on_change=lambda e: update_search_results(e.data, departure_results, departure_tf),
    )
    arrival_tf = TextField(
        label="Arrival",
        on_change=lambda e: update_search_results(e.data, arrival_results, arrival_tf),
    )

    date_pick_button = ElevatedButton(
        "Pick date",
        icon=Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            DatePicker(
                first_date=datetime.datetime.now(),
                last_date=datetime.datetime.now(),
            )
        ),
    )

    submit_button = ElevatedButton(
        "Search flights",
        on_click=submit_button_click,
    )

    # Separate search results containers for departure and arrival fields
    departure_results = Container(
        content=Column(spacing=5),
        border=border.all(1, colors.GREY),
        border_radius=5,
        padding=5,
        width=300,
        visible=False,
        bgcolor=colors.WHITE,
        #elevation=5,
    )

    arrival_results = Container(
        content=Column(spacing=5),
        border=border.all(1, colors.GREY),
        border_radius=5,
        padding=5,
        width=300,
        visible=False,
        bgcolor=colors.WHITE,
        #elevation=5,
    )

    def update_search_results(query, results_container, search_tf):
        results_container.content.controls.clear()
        results_container.visible = False

        if query.strip():
            results_container.visible = True

            # Filter results: search only at the beginning of entries
            filtered_results = [
                f"{str(item[0])}, {str(item[1])}, {str(item[2])}"
                for item in data
                if str(item[0]).lower().startswith(query.lower())
                or str(item[1]).lower().startswith(query.lower())
                or str(item[2]).lower().startswith(query.lower())
            ]

            for result in filtered_results:
                results_container.content.controls.append(
                    TextButton(
                        text=result,
                        on_click=lambda e, r=result: select_result(r, search_tf, results_container),
                    )
                )
        page.update()

    def select_result(selected_item, search_tf, results_container):
        search_tf.value = selected_item
        results_container.content.controls.clear()
        results_container.visible = False
        page.update()

    return View(
        route="/add_flight/search_your_journey",
        controls=[
            Container(
                bgcolor=colours["background"],
                width=WINDOW_WIDTH,
                height=WINDOW_HEIGHT,
                border=border.all(1, color=colours["gray_text"]),
                border_radius=35,
                content=Column(
                    controls=[
                        Container(
                            content=Stack(
                                controls=[
                                    # Main content
                                    Column(
                                        controls=[
                                            headline,
                                            Container(departure_tf),
                                            departure_results,  # Dropdown for departure
                                            Container(arrival_tf),
                                            arrival_results,  # Dropdown for arrival
                                            date_pick_button,
                                            submit_button,
                                        ],
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=30,
                                    ),
                                ]
                            ),
                            padding=20,
                            expand=True,
                        ),
                        navigation_bar,
                    ]
                ),
            )
        ],
    )
