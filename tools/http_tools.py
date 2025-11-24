import os
import httpx

# Orchestrator endpoint (Docker internal DNS name)
ORCHESTRATOR_URL = os.getenv(
    "ORCHESTRATOR_URL",
    "http://orchestrator:8004/orchestrate_search"
)

# Booking service base URL (Docker internal DNS name)
BOOKING_BASE_URL = os.getenv(
    "BOOKING_BASE_URL",
    "http://booking:8002"
)

def orchestrated_search(origin: str, dest: str, date: str) -> dict:
    """
    Call orchestrator_service to perform a flight search.
    """
    payload = {"origin": origin, "dest": dest, "date": date}
    with httpx.Client(timeout=10.0) as client:
        resp = client.post(ORCHESTRATOR_URL, json=payload)
        resp.raise_for_status()
        return resp.json()

def create_hold(session_id: str, flight_id: int) -> dict:
    """
    Send a hold request to booking service.
    """
    url = f"{BOOKING_BASE_URL}/hold"
    payload = {"session_id": session_id, "flight_id": flight_id}
    with httpx.Client(timeout=10.0) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()

def confirm_booking(job_id: str) -> dict:
    """
    Confirm a held booking job.
    """
    url = f"{BOOKING_BASE_URL}/confirm"
    payload = {"job_id": job_id}
    with httpx.Client(timeout=10.0) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()

def pause_job(job_id: str) -> dict:
    """
    Pause long-running booking job.
    """
    url = f"{BOOKING_BASE_URL}/jobs/pause"
    payload = {"job_id": job_id}
    with httpx.Client(timeout=10.0) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()

def resume_job(job_id: str) -> dict:
    """
    Resume paused booking job.
    """
    url = f"{BOOKING_BASE_URL}/jobs/resume"
    payload = {"job_id": job_id}
    with httpx.Client(timeout=10.0) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()

def get_job_status(job_id: str) -> dict:
    """
    Get job status from booking service.
    """
    url = f"{BOOKING_BASE_URL}/jobs/{job_id}"
    with httpx.Client(timeout=10.0) as client:
        resp = client.get(url)
        resp.raise_for_status()
        return resp.json()
