from fastapi import FastAPI
import httpx
import os

app = FastAPI()

SEARCH_SERVICE = os.getenv(
    "SEARCH_SERVICE",
    "http://search:8001/search"
)

BOOKING_SERVICE = os.getenv(
    "BOOKING_SERVICE",
    "http://booking:8002/book"
)

@app.post("/orchestrate_search")
async def orchestrate_search(req: dict):
    origin = req["origin"]
    dest = req["dest"]
    date = req["date"]

    async with httpx.AsyncClient() as client:
        resp = await client.post(SEARCH_SERVICE, json=req)
        return resp.json()

@app.post("/orchestrate_booking")
async def orchestrate_booking(req: dict):
    flight_id = req["flight_id"]

    async with httpx.AsyncClient() as client:
        resp = await client.post(BOOKING_SERVICE, json=req)
        return resp.json()
