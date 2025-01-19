
from flet import *
from flet.core.alignment import center

from components.sing_navigation_bar import SingletonNavBar
from utils.constants import *

def create_button(page:Page, text: str):
    return Container(
            OutlinedButton(
                content=Container(
                    content = Text(
                        text,
                        size=20,
                        color=colours["login_text"],
                    ),
                    alignment = alignment.center,
                    margin=10
                ),
                on_click=lambda e: page.go("/add_flight/" + text.lower().replace(" ", "_")),
                width = 300,
            ),
            alignment=alignment.center,
            margin=margin.only(bottom=100)
        )


def add_flight_view(page: Page):
    navigation_bar = SingletonNavBar(page).instance
    search_button = create_button(page, "Search your journey")
    upload_button = create_button(page, "Upload a ticket")
    return View(
            route = "/add_flight",
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
                                    content=Text("Search", size=HEAD_FONT_SIZE),
                                    alignment=alignment.center,
                                    margin = margin.only(bottom=200),
                                ),
                                search_button,
                                upload_button,
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            #expand=True,
                        ),
                        navigation_bar
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                )
            )
        ]
    )