import sqlite3

from utils.constants import DB_PATH


class FlightDao:
    def __init__(self):
        self.db_path = DB_PATH
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def fetch_flights(self, departure, arrival, date):
        return None
    def update_flight(self):
        return None
