from dataclasses import dataclass

@dataclass
class Airport:
    name: str
    iata: str
    city: str
    #icao: str