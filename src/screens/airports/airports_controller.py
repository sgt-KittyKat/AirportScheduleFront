import pandas as pd

def get_airports_data():
    df = pd.read_csv("../data/airports.csv")
    filtered_data = df[["IATA", "Airport name", "City"]]
    list_of_lists = filtered_data.values.tolist()
    return list_of_lists