# database/init_db.py

import sqlite3
import os
import random
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "flights.db")

# -----------------------------
# Airport + Airline Master Data
# -----------------------------
AIRPORTS = {
    "DEL": "Delhi",
    "BOM": "Mumbai",
    "MAA": "Chennai",
    "HYD": "Hyderabad",
    "BLR": "Bangalore",
    "CCU": "Kolkata",
    "COK": "Cochin",
    "AMD": "Ahmedabad",
    "PNQ": "Pune",
    "GOI": "Goa",
    "DXB": "Dubai",
    "AUH": "Abu Dhabi",
    "DOH": "Doha",
    "SIN": "Singapore",
    "KUL": "Kuala Lumpur",
    "JFK": "New York JFK",
    "LHR": "London Heathrow",
    "SYD": "Sydney",
    "HKG": "Hong Kong",
}

AIRLINES = [
    "Air India",
    "Indigo",
    "Vistara",
    "SpiceJet",
    "Emirates",
    "Etihad",
    "Qatar Airways",
    "Singapore Airlines",
    "Malaysia Airlines",
    "Qantas",
    "Cathay Pacific",
    "ANA",
    "Lufthansa",
    "British Airways",
    "Air France",
    "Delta",
    "United Airlines",
    "American Airlines",
    "Japan Airlines",
]

# ------------------------------------
# Generate N days of realistic dates
# ------------------------------------
def generate_dates(n_days: int = 30):
    base = datetime.today()
    return [(base + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(n_days)]

DATES = generate_dates(30)


# ------------------------------------
# Build a big list of flights
# ------------------------------------
def generate_flight_data():
    flights = []

    for origin in AIRPORTS.keys():
        for dest in AIRPORTS.keys():
            if origin == dest:
                continue  # no same-origin/dest

            for date in DATES:
                airline = random.choice(AIRLINES)
                # Roughly realistic international price range
                price = round(random.uniform(80, 1200), 2)
                seats = random.randint(5, 40)

                flights.append(
                    (airline, origin, dest, date, price, seats)
                )

    return flights


# ------------------------------------
# Create / reset DB and insert data
# ------------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # NOTE: upgraded schema – adds `date`
    cur.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        airline TEXT,
        origin TEXT,
        dest TEXT,
        date TEXT,
        price REAL,
        seats INTEGER
    );
    """)

    # Clear existing data so reruns are clean
    cur.execute("DELETE FROM flights")

    flights = generate_flight_data()

    cur.executemany(
        "INSERT INTO flights (airline, origin, dest, date, price, seats) VALUES (?, ?, ?, ?, ?, ?)",
        flights
    )

    conn.commit()
    conn.close()
    print(f"✔ Flights database initialized with {len(flights)} rows.")


if __name__ == "__main__":
    init_db()
