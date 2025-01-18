import pandas as pd
import requests

from utils.constants import SERVER_LINK


def get_airports_data():
    r = requests.get(SERVER_LINK + "/airports")
    data = r.json()["airports"]

    df = pd.DataFrame(data)
    filtered_data = df[["iata_code", "name", "city"]]
    list_of_lists = filtered_data.values.tolist()
    return list_of_lists