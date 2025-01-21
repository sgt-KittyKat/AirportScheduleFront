# components/airport_card.py
from flet import *
#from app.navigation import Navigator
from features.airports.airport import Airport
from utils.constants import colours


class AirportCard:

    def __init__(self, airport:Airport, page):
        self.airport = airport
        self.card = None
        self.destination_page = f"/airports/id={airport.iata}"
        self.page = page

    def build(self):
        self.card = OutlinedButton(
                content=Container(
                    content=Row(
                        [
                            Text(value=f"{self.airport.name}, {self.airport.iata}", size = 20)
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    alignment=alignment.center,
                    #border=border.all(1, color=colours["gray_text"]),
                    #border_radius=10,
                    padding=padding.only(left=20, right=20, top=5, bottom=5)
                ),
                style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                ),
                on_click = lambda e: self.page.go(self.destination_page)
        )

    def update(self, airport):

        self.airport = airport
        self.build()

    def get_card(self):
        if self.card is None:
            self.build()
        return self.card
