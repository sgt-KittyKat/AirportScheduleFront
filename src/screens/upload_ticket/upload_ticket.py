
from flet import *
from flet.core.alignment import center

from components.sing_navigation_bar import SingletonNavBar
from utils.constants import *


def upload_ticket_view(page: Page):
    navigation_bar = SingletonNavBar(page).instance

    def on_upload_click(e):
        print("File uploaded!")  # Add your file upload logic here

    def on_camera_click(e):
        print("Open camera!")  # Add your camera capture logic here
    return View(
        route = "/add_flight/upload_a_ticket",
        controls = [Container(
        bgcolor=colours["background"],
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        border=border.all(1, color=colours["gray_text"]),
        border_radius=35,
        content = Column(
                    controls = [
                        Container(
                            content=Column(
                                [
                                    Text(
                                        "Upload your ticket",
                                        weight=FontWeight.BOLD,
                                        size=20,
                                        text_align=TextAlign.CENTER,
                                    ),
                                    Container(
                                        OutlinedButton(
                                            content=Container(
                                                content=Column(
                                                    controls=[
                                                        Icon(name=icons.IMAGE, size=40, color=colors.GREY),
                                                        #Text("Upload your ticket"),
                                                    ],
                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                ),
                                                alignment=center,
                                                width=300,
                                                height=150,
                                            ),
                                            style=ButtonStyle(
                                                shape=RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=on_upload_click
                                        ),
                                        alignment=center
                                    ),
                                    Text("or", text_align=TextAlign.CENTER),
                                    FilledButton(
                                        "Open Camera & Take Photo",
                                        on_click=on_camera_click,
                                        icon=icons.CAMERA_ALT,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=20,
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
        ]
    )