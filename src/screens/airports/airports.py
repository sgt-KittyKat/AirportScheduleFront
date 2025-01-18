from flet import *
from flet.core.alignment import center

from features.airports.airport_service import AirportService
from utils import constants
from components.airport_card import AirportCard
from components.sing_navigation_bar import SingletonNavBar
from features.airports.airport import Airport
from utils.constants import *
from screens.airports import airports_controller

from screens.individual_airport.ind_airport_controller import IndividualAirportController


def airports_view(page: Page):
    navigation_bar = SingletonNavBar(page).instance
    airport_controller = IndividualAirportController(page, AirportService())
    search_tf = Container(
        TextField(
            label="Enter Airport Name",
            autofocus=True,
            on_change=lambda e: update_search_results(e.data),
        ),
        width=300,
        alignment=alignment.center
    )
    data = airports_controller.get_airports_data()
    constants.AIRPORTS_DATA = data
    airport_cards = Column(controls=[],)

    airport_controller.generate_airport_page(DUMMY_AIRPORT.iata)
    airport_cards.controls.append(AirportCard(constants.DUMMY_AIRPORT, page).get_card())

    search_results = Container(
        content=Column(spacing=5),
        border=border.all(1, colors.GREY),
        border_radius=5,
        padding=5,
        width=300,
        visible=False
    )

    def update_search_results(query):
        search_results.content.controls.clear()
        search_results.visible = False

        if query.strip():
            search_results.visible = True

            # Filter results: search only at the beginning of entries
            filtered_results = [
                f"{str(item[0])}, {str(item[1])}, {str(item[2])}"
                for item in data
                if str(item[0]).lower().startswith(query.lower()) or
                   str(item[1]).lower().startswith(query.lower()) or
                   str(item[2]).lower().startswith(query.lower())
            ]

            for result in filtered_results:
                search_results.content.controls.append(
                    TextButton(
                        text=result,
                        on_click=lambda e, r=result: select_result(r)
                    )
                )
        page.update()

    def select_result(selected_item):
        page.update()
        print(f"selected_item: {selected_item}")  # Debugging

        search_tf.content.value = selected_item
        search_results.content.controls.clear()  # Clear results after selection
        search_results.visible = False  # Hide the results

        airport_data = selected_item.split(", ")

        new_airport = Airport(2, airport_data[1], airport_data[0], airport_data[2], "NONE", "NONE")

        # print(new_airport)
        # airport_controller.generate_airport_page(new_airport.id)
        new_card = AirportCard(new_airport, page).get_card()
        # page.controls.append(new_card)
        airport_cards.controls.append(
            new_card
        )
        # print(airport_cards)
        page.update()

    return View(
        route="/airports",
        controls=[Container(
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
                                content=Text("Airports", size=HEAD_FONT_SIZE),
                                alignment=alignment.center,
                                margin=margin.only(bottom=50)
                            ),
                            search_tf,
                            search_results,
                            airport_cards
                        ],
                        alignment=MainAxisAlignment.START,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        expand=True,
                    ),
                    navigation_bar
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        ]
    )
