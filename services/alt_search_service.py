# services/alt_search_service.py
from fastapi import FastAPI, HTTPException
import sqlite3, os, time, random
from infra.observability import logger, incr, observe, metrics_response

app = FastAPI()
DB = os.path.join(os.path.dirname(__file__), "..", "database", "flights.db")

@app.post("/search")
def search(payload: dict):
    start = time.time()
    origin = payload.get("origin")
    dest = payload.get("dest")
    if not origin or not dest:
        raise HTTPException(status_code=400, detail="origin and dest required")
    logger.info("alt_search request", extra={"origin": origin, "dest": dest})
    incr("alt_search_service", "search")

    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("SELECT id, airline, price, seats FROM flights WHERE origin=? AND dest=?", (origin, dest))
        rows = cur.fetchall()
        conn.close()
    except Exception as e:
        logger.error("db error alt", extra={"error": str(e)})
        raise HTTPException(status_code=500, detail="database error")

    # Slightly modify prices to show variance between sources
    flights = []
    for r in rows:
        price = max(1.0, r[2] + random.uniform(-15.0, 30.0))
        flights.append({"id": r[0], "airline": r[1], "price": round(price, 2), "seats": r[3], "source": "alt"})

    latency = time.time() - start
    observe("alt_search_service", "search", latency)
    logger.info("alt_search done", extra={"count": len(flights), "latency_s": latency})
    return {"flights": flights}

@app.get("/metrics")
def metrics():
    return metrics_response()
