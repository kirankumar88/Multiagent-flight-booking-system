from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "flights.db")

class SearchRequest(BaseModel):
    origin: str
    dest: str
    date: str  # YYYY-MM-DD

@app.post("/search")
def search_flights(data: SearchRequest):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        # Updated query including DATE
        query = """
        SELECT id, airline, origin, dest, date, price, seats
        FROM flights
        WHERE origin = ? AND dest = ? AND date = ?
        """

        cur.execute(query, (data.origin, data.dest, data.date))
        rows = cur.fetchall()
        conn.close()

        if not rows:
            return {"flights": []}

        results = [
            {
                "id": r[0],
                "airline": r[1],
                "origin": r[2],
                "dest": r[3],
                "date": r[4],
                "price": r[5],
                "seats": r[6],
            }
            for r in rows
        ]

        return {"flights": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
