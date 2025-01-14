from flet import *

from utils.constants import colours

class SingletonNavBar:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonNavBar, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, page):
        if not self._initialized:
            self._initialized = True
            self._navigation_bar = self.create_navigation_bar(page)

    @property
    def instance(self):
        return self._navigation_bar

    @staticmethod
    def create_navigation_bar(page: Page):
        destinations = [
            NavigationBarDestination(icon=Icons.AIRPLANEMODE_ON, label="Your Flights"),
            NavigationBarDestination(icon=Icons.SEARCH, label="Add Flight"),
            NavigationBarDestination(icon=Icons.AIRPORT_SHUTTLE, label="Airports"),
        ]

        return NavigationBar(
            destinations=destinations,
            on_change=lambda e: page.go("/"+destinations[e.control.selected_index].label.lower().replace(" ", "_")),
            bgcolor=colours["navbar"],
            indicator_color=colours["login_button"],
        )