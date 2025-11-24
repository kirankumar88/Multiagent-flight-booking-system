import httpx

# IMPORTANT:
# Inside Docker, DO NOT use localhost.
# Use Docker service names from docker-compose.

ORCHESTRATOR_URL = "http://orchestrator:8004/orchestrate_search"
BOOK_URL = "http://booking:8002/book"

def orchestrate_search(origin, dest, date):
    payload = {
        "origin": origin,
        "dest": dest,
        "date": date
    }
    try:
        with httpx.Client(timeout=20) as client:
            resp = client.post(ORCHESTRATOR_URL, json=payload)
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {"error": str(e)}

def book_flight(flight_id):
    payload = {"flight_id": flight_id}
    try:
        with httpx.Client(timeout=20) as client:
            resp = client.post(BOOK_URL, json=payload)
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {"error": str(e)}
