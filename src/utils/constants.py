from flet.core.page import Page

from features.airports.airport import Airport
from features.flights.flight import Flight
from features.users.user import User

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 450
WINDOW_PADDING_UP = 20
WINDOW_PADDING_DOWN = 20

HEAD_FONT_SIZE = 35

colours = {
        "background": "#FFFFFF",
        "gray_text": "#A6A6A6",
        "login_text": "#036BB9",
        "login_button": "#0386D0",
        "navbar": "#469FD1",
        "gray_text_2": "#747070",
        "black": "#000000"
    }

ADMIN = User(
        1,
        username="admin",
        password="admin",
        upcoming_flights = [Flight(
                id = 1,
                origin="WAW",
                destination="BER",
                departure_time="19:30",
                arrival_time="21:00",
                #departure_date="16.10.2024",
                flight_number="OS 220",
                #airline="Austrian Airlines",
                #aircraft="EMBRAER 195",
                status="Check-in closed"
        ),
        Flight(
                id = 1,
                origin="BO",
                destination="BER",
                departure_time="19:30",
                arrival_time="21:00",
                #departure_date="16.10.2024",
                flight_number="OS 220",
                #airline="Austrian Airlines",
                #aircraft="EMBRAER 195",
                status="Check-in closed"
        )
        ],
        flight_history=[]
)

DUMMY_AIRPORT = Airport("KURWA AIRPORT", "BER", "KURISKO",)

DB_PATH = "..."

SERVER_LINK = "http://127.0.0.1:5000"

AIRPORTS_DATA = None
