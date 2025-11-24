from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os
import uuid

app = FastAPI(title="Booking Service")

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "flights.db")

class BookRequest(BaseModel):
    flight_id: int

@app.post("/book")
def book_flight(req: BookRequest):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        # 1. Fetch flight
        cur.execute("SELECT id, airline, price, seats FROM flights WHERE id = ?", (req.flight_id,))
        row = cur.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail="Flight ID not found")

        flight_id, airline, price, seats = row

        # 2. Check seat availability
        if seats <= 0:
            raise HTTPException(status_code=400, detail="No seats available")

        # 3. Deduct seat
        new_seats = seats - 1
        cur.execute("UPDATE flights SET seats = ? WHERE id = ?", (new_seats, req.flight_id))
        conn.commit()

        # 4. Create booking ID
        booking_id = str(uuid.uuid4())[:8]

        conn.close()

        return {
            "status": "success",
            "message": "Flight booked successfully!",
            "flight_id": flight_id,
            "airline": airline,
            "price": price,
            "remaining_seats": new_seats,
            "booking_id": booking_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
