from google.adk.agents import LlmAgent
from tools.http_tools import orchestrated_search

flight_search_agent = LlmAgent(
    name="flight_search_agent",
    description="Agent that retrieves flight options by calling the orchestrator backend.",
    model="gemini-2.5-flash-lite",
    instruction="""
You are the Flight Search Agent.

You MUST collect:
- origin
- destination
- travel date (YYYY-MM-DD)

Only when you have all three, call the tool:
  orchestrated_search(origin, dest, date)

The tool returns a JSON with a 'results' list of flights.
Summarize the best options (cheapest few) and include flight IDs in your response.
""",
    tools=[orchestrated_search],
)
