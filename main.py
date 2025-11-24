# main.py

import asyncio
import uuid
from dotenv import load_dotenv

# Load environment variables (API keys, etc.)
load_dotenv()

# ADK Imports (adjust if your local ADK uses slightly different paths)
from google.adk.runners import Runner
from google.genai import types

# Our internal services
from infra.memory import session_service
from agents.orchestrator_agent import orchestrator_agent


async def interactive_cli():
    """
    Interactive CLI that talks to the orchestrator_agent.
    """
    print("\nFlight Booking Assistant (powered by gemini-2.5-flash-lite)")
    print("Type 'exit' to quit.\n")

    app_name = "flight_app"
    user_id = "user1"
    session_id = f"s_{uuid.uuid4().hex[:8]}"

    # Create ADK session
    await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )

    # Runner executes the agent pipeline
    runner = Runner(
        agent=orchestrator_agent,
        app_name=app_name,
        session_service=session_service
    )

    while True:
        text = input("YOU: ").strip()
        if text.lower() in ("exit", "quit"):
            print("Exiting assistant.")
            break

        # Create ADK Content object
        content = types.Content(
            parts=[types.Part(text=text)]
        )

        full_response = ""

        # Stream events from agent
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=content
        ):
            if event.is_final_response() and event.content:
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text:
                        full_response += part.text

        if full_response:
            print(f"\nAGENT: {full_response}\n")


if __name__ == "__main__":
    asyncio.run(interactive_cli())
