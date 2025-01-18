from dataclasses import dataclass

@dataclass
class Flight:
    id: int
    origin: str
    destination: str
    status: str
    departure_time: str
    expected_departure_time: str | None
    arrival_time: str | None
    expected_arrival_time: str | None
    flight_number: str
    terminal: str | None
    checkin_gate: str | None
    boarding_gate: str | None
    baggage_reclaim_belt: str | None
