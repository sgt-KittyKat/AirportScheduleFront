from dataclasses import dataclass

@dataclass
class Flight:
    id: int
    origin: str
    destination: str
    #departure_date: str
    status: str
    departure_time: str
    arrival_time: str
    flight_number: str
    #airline: str
    #aircraft: str