from flet import *
from flet.core.alignment import center

from features.users.user_service import UserService
from screens.login_page.login_page_controller import LoginPageController
from utils import constants
from components.airport_card import AirportCard
from components.sing_navigation_bar import SingletonNavBar
from features.airports.airport import Airport
from utils.constants import *
from screens.airports import airports_controller

def register_view(page: Page):
    #user_service = UserService()
    #page_controller = LoginPageController()
    def register_attempt(e):
        username = email_tf.content.value
        password = pw_tf.content.value


    navigation_bar = SingletonNavBar(page).instance
    register_text = Text(
        value = "Register",
        color = colours["login_text"],
    )
    login_button = ElevatedButton(
        text="Login",
        color = colors.GREY,
        on_click = lambda e: page.go("/login_page")
    )
    login_register_button = Container(
        content = Row(
            controls = [
                login_button,
                register_text
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
    )

    email_tf = Container(
        content = TextField(
            label="Email address",
            #color=colours["gray_text"],
            border_color = colors.BLUE,
            icon = Icon(Icons.EMAIL),
        ),
        width = 300,
    )

    pw_tf = Container(
        content = TextField(
            label="Password",
            #color = colours["gray_text"],
            border_color = colors.BLUE,
            password=True,
            can_reveal_password=True,
            #prefix = Icon(Icons.PASSWORD)
            icon = Icon(Icons.PASSWORD),
        ),
        width = 300,
    )
    repeat_pw_tf = Container (
        content = TextField(
            label="Repeat password",
            border_color = colors.BLUE,
            password = True,
            can_reveal_password=True,
            icon = Icon(Icons.LOCK),
        ),
        width = 300,
    )
    submit_button = Container(
        content = ElevatedButton(
            text = "Register",
            on_click = register_attempt,
        )
    )

    return View (
        route = "/register_page",
        controls = [Container(
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
                                    content=Text("Register", size=HEAD_FONT_SIZE),
                                    alignment=alignment.center,
                                    margin = margin.only(bottom = 50)
                                ),
                                login_register_button,
                                email_tf,
                                pw_tf,
                                repeat_pw_tf,
                                submit_button,
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