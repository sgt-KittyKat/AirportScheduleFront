from flet import *
from flet.core.alignment import center

from features.users.auth_service import AuthService
from features.users.user_service import UserService
from screens.login_page.login_page_controller import LoginPageController
from utils import constants
from components.airport_card import AirportCard
from components.sing_navigation_bar import SingletonNavBar
from features.airports.airport import Airport
from utils.constants import *
from screens.airports import airports_controller

def login_view(page: Page):
    #user_service = UserService()
    login_controller = LoginPageController(page, AuthService())

    def login_attempt(e):
        username = email_tf.content.value
        password = pw_tf.content.value
        response = login_controller.authenticate_user(username, password)
        if response["success"] is True:
            complain.visible = False
            page.update()
            page.go("/add_flight")

        else:
            complain.visible = True
            page.update()


    complain = Text(
        value="Invalid email or password",
        color=colors.RED,
        visible=False
    )


    navigation_bar = SingletonNavBar(page).instance
    login_text = Text(
        value = "Login",
        color = colours["login_text"],
    )
    register_button = ElevatedButton(
        text="Register",
        color = colors.GREY,
        on_click=lambda e: page.go("/register_page")
    )
    login_register_button = Container(
        content = Row(
            controls = [
                login_text,
                register_button
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

    submit_button = Container(
        content = ElevatedButton(
            text = "Login",
            on_click = login_attempt
        )
    )

    return View(
        route = "/login_page",
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
                                    content=Text("Log In", size=HEAD_FONT_SIZE),
                                    alignment=alignment.center,
                                    margin = margin.only(bottom = 50)
                                ),
                                login_register_button,
                                email_tf,
                                pw_tf,
                                submit_button,
                                complain
                            ],
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            expand=True,
                        ),
                        #navigation_bar,
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                )
            )
        ]
    )