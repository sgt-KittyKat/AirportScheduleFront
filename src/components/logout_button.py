from flet import *

class LogoutButton:
    def __init__(self, page: Page):
        self.page = page

    def get_button(self):
        return ElevatedButton(
            text="Log Out",
            icon=Icons.LOGOUT,
            on_click= lambda e: self.log_out()
        )

    def log_out(self):
        self.page.client_storage.clear()
        self.page.go("/login_page")