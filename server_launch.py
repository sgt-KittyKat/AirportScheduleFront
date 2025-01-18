from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Path to your existing SQLite database file
DATABASE = 'flight_app.db'


def get_db_connection():
    """
    Creates and returns a new SQLite database connection,
    ensuring rows are returned as dictionaries (row_factory).
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    """
    Simple index endpoint to confirm the server is running.
    """
    return "Welcome to my simple Flask webserver!"


@app.route('/airport-iata/<iata_code>', methods=['GET'])
def get_airport_iata(iata_code):
    """
    Fetch given airport data by IATA code
    """
    # For example, if you'd like to query the database for this iata_code,
    # you could uncomment and adapt this:
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM flights WHERE origin = ?", (iata_code,))
    # rows = cursor.fetchall()
    # conn.close()
    #
    # flights = []
    # for row in rows:
    #     flights.append({
    #         'flight_id': row['id'],
    #         'origin': row['origin'],
    #         'destination': row['destination'],
    #         'status': row['status'],
    #         'departure_time': row['departure_time'],
    #         'arrival_time': row['arrival_time'],
    #         'flight_number': row['flight_number']
    #     })

    # For now, let's just simulate a response:
    departures = [
        {
            'id': 1,
            'origin': 'WAW',
            'destination': 'BER',
            #'departure_date': 'now',
            'status': 'boarding',
            'departure_time': '11:00',
            'arrival_time': '13:00',
            'flight_number': '1234',
            #'airline': 'KURWA AIRLINES',
            #'aircraft': 'KURWOLOT'
        }
    ]

    arrivals = [
        {
            'id': 1,
            'origin': 'KURWA',
            'destination': 'BER',
            #'departure_date': 'now',
            'status': 'boarding',
            'departure_time': '11:00',
            'arrival_time': '13:00',
            'flight_number': '1234',
            #'airline': 'KURWA AIRLINES',
            #'aircraft': 'KURWOLOT'
        }
    ]

    return jsonify({
        "requested_iata_code": iata_code,
        "departures": departures,
        "arrivals": arrivals

    })


if __name__ == '__main__':
    # Enable debug for development; turn it off for production
    app.run(debug=True)