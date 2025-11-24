# agents/booking_agent.py

from google.adk.agents import LlmAgent
from tools.http_tools import (
    create_hold,
    confirm_booking,
    pause_job,
    resume_job,
    get_job_status,
)

booking_agent = LlmAgent(
    name="booking_agent",
    description="Handles booking lifecycle: hold, confirm, pause/resume, and job status.",
    model="gemini-2.5-flash-lite",
    instruction="""
You are the Booking Agent.

Tools you can use:
- create_hold(session_id, flight_id)
- confirm_booking(job_id)
- pause_job(job_id)
- resume_job(job_id)
- get_job_status(job_id)

Your tasks:
- Create holds for a selected flight.
- Confirm a held booking.
- Pause or resume booking jobs.
- Return structured data: job_id, state, session_id, flight_id.
""",
    tools=[create_hold, confirm_booking, pause_job, resume_job, get_job_status],
)
