import datetime
from re import search

from flet import *
from flet.core.alignment import center

from components.flight_card import FlightCard
from components.sing_navigation_bar import SingletonNavBar
from features.flights.flight_service import FlightService
from screens.airports import airports_controller
from screens.search_flight.search_flight_controller import SearchFlightController
from utils import constants
#from screens.search_flight import search_flight_controller
from utils.constants import *


def search_flight_view(page: Page):
    navigation_bar = SingletonNavBar(page).instance
    search_flight_controller = SearchFlightController(page, FlightService())
    data = airports_controller.get_airports_data()

    flight_cards = []

    complain = Text(
        value = "Please choose airports out of the list",
        color = colors.RED,
        visible = False
    )
    def check_input():
        departure = departure_tf.value.split(", ")
        arrival = arrival_tf.value.split(", ")
        iata_arrival = arrival[0]
        iata_depature = departure[0]
        airports = constants.AIRPORTS_DATA
        complain_d = True
        complain_a = True
        for airport in airports:
            if airport[0] == iata_arrival:  # The first element is iata_code
                complain_a = False
            if airport[0] == iata_depature:
                complain_d = False

        return complain_d or complain_a



    def submit_button_click():
        if check_input():
            complain.visible = True
            page.update()
            return
        else:
            complain.visible = False
            page.update()

        departure = departure_tf.value.split(", ")
        arrival = arrival_tf.value.split(", ")
        iata_arrival = arrival[0]
        iata_depature = departure[0]

        flights_data = search_flight_controller.send_flight_search_request(iata_depature, iata_arrival)
        print(flights_data)
        for flight in flights_data:
            flights_list_view.controls.append(FlightCard(flight, page).get_card())
        print(flight_cards)

        show_flights()

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
        on_click=lambda e: submit_button_click()
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


    flights_list_view = ListView(
        controls = flight_cards,
        #visible=False,
        spacing=5,
        expand=True,  # Ensure it expands within the parent container
        auto_scroll=True,  # Enable scrolling
    )


    search_fields = Column(
        controls=[
            headline,
            Container(departure_tf),
            departure_results,  # Dropdown for departure
            Container(arrival_tf),
            arrival_results,  # Dropdown for arrival
            date_pick_button,
            submit_button,
            complain
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=30,
        visible = True
    )

    def show_flights():
        flight_fields.visible = True
        search_fields.visible = False
        page.update()


    def show_search():
        flight_fields.visible = False
        search_fields.visible = True
        flights_list_view.controls.clear()
        page.update()


    flight_fields = Column(
        controls=[
            flights_list_view,
            ElevatedButton(
                text = "Go back",
                icon=icons.ARROW_LEFT,
                on_click=lambda e: show_search()
            )
        ],
        visible=False
    )

    return View(
        route="/add_flight/search_your_journey",
        controls=[
            Container(
                bgcolor=colours["background"],
                expand = True,
                border=border.all(1, color=colours["gray_text"]),
                border_radius=35,
                content=Column(
                    controls=[
                        Container(
                            content=Stack(
                                controls=[
                                    # Main content
                                    flight_fields,
                                    search_fields,
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
