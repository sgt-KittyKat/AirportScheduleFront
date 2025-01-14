from dataclasses import dataclass

@dataclass
class Airport:
    id: int
    name: str
    code: str
    city: str
    country: str