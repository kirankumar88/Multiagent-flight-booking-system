# agents/orchestrator_agent.py

from google.adk.agents import LlmAgent
from agents.flight_search_agent import flight_search_agent
from agents.booking_agent import booking_agent

orchestrator_agent = LlmAgent(
    name="orchestrator_agent",
    description="Main conversational agent that coordinates flight search and booking.",
    model="gemini-2.5-flash-lite",
    instruction="""
You are the main Flight Booking Orchestrator.

- Understand user intent (search flights, hold flights, confirm booking, job status).
- For flight search → call flight_search_agent (A2A).
- For booking or job operations → call booking_agent (A2A).
- Maintain conversation flow.
- Request missing info (origin, destination, date).
- Return natural language responses to the user.
""",
    sub_agents=[flight_search_agent, booking_agent],
)
