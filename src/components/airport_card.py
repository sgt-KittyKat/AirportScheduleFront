# components/airport_card.py
from flet import *

from features.airports.airport import Airport
from utils.constants import colours


class AirportCard:

    def __init__(self, airport:Airport):
        """
        Initialize the airportCard with airport data.
        Args:
            airport (airport): An instance of the airport model.
        """
        self.airport = airport
        self.card = None  # Will hold the Flet UI representation
        self.destination_page = f"/airports/id={airport.id}"

    def build(self):
        """
        Build and return the UI for the airportCard.
        """
        self.card = OutlinedButton(
                content=Container(
                    content=Row(
                        [
                            # Left Section: Outbound, Destination, Time
                            Text(value=f"{self.airport.name}, {self.airport.code}", size = 20)
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    alignment=alignment.center,
                    #border=border.all(1, color=colours["gray_text"]),
                    #border_radius=10,
                    padding=padding.only(left=20, right=20, top=5, bottom=5)
                ),
                #on_click=
        )
        #print(self.card.content.controls[0].value + "JA DALBAEB")
        #return self.card

    def update(self, airport):
        """
        Update the card's airport data and rebuild the UI.
        Args:
            airport (airport): An updated instance of the airport model.
        """
        self.airport = airport
        self.build()

    def get_card(self):
        """
        Return the rendered card (build if not already built).
        """
        if self.card is None:
            self.build()
        return self.card
