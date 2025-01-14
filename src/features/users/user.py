from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    password: str
    flight_history: list
    upcoming_flights: list