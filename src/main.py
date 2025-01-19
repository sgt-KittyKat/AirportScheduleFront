from flet import *

from app.navigation import Navigator
from utils.constants import *


def main(page:Page):
    page.expand = True,
    navigator = Navigator(page)
    page.on_route_change = navigator.route_change
    page.go("/login_page")

if __name__ == "__main__":
    app(target=main)