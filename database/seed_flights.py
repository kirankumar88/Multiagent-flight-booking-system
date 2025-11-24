import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "flights.db")

FLIGHTS = [
    ("Air India", "DEL", "DXB", 400, 12),
    ("Indigo", "DEL", "DXB", 350, 7),
    ("Emirates", "DEL", "DXB", 520, 9),
    ("Air India", "HYD", "DXB", 380, 10),
    ("Indigo", "HYD", "DXB", 340, 8),
]

def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executemany(
        "INSERT INTO flights (airline, origin, dest, price, seats) VALUES (?, ?, ?, ?, ?)",
        FLIGHTS
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Seeding flights...")
    seed()
    print("Done.")
