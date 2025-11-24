# Multiagent-flight-booking-system
A Google ADK–powered prototype flight booking system with multi-agent orchestration, FastAPI microservices, Streamlit UI, and Docker. Demonstrates smart, modular, cloud-ready automation for search and booking workflows.

Multiagent Flight Booking System (Prototype)
A cloud-ready, Docker-orchestrated multi-agent flight booking prototype powered by Google ADK, FastAPI microservices, Streamlit UI, and agent-driven orchestration. This system demonstrates a modern, modular, and production-style architecture for automated flight search and booking workflows.

<p align="center">

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python">

  <!-- FastAPI -->
  <img src="https://img.shields.io/badge/FastAPI-Microservices-009688?logo=fastapi&logoColor=white" alt="FastAPI">

  <!-- Streamlit -->
  <img src="https://img.shields.io/badge/Streamlit-UI-ee2c4a?logo=streamlit&logoColor=white" alt="Streamlit">

  <!-- Docker -->
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker">

  <!-- Google ADK -->
  <img src="https://img.shields.io/badge/Google%20ADK-Multiagent%20Framework-4285F4?logo=google&logoColor=white" alt="Google ADK">

  <!-- Status -->
  <img src="https://img.shields.io/badge/Status-Prototype-orange?style=flat-square" alt="Prototype">

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">

</p>


Project Overview:
This prototype showcases a scalable multi-agent architecture where each agent handles a specialized responsibility:
Search Agent → Handles flight lookup logic
Booking Agent → Simulates booking and confirmation
Orchestrator Agent → Coordinates search and booking workflows
Streamlit UI → User-facing interface for interacting with the system
The system simulates real airline processes using microservices and agent coordination through Google ADK.

Architecture :
The application is composed of four containerized microservices:
    Service	           Port	          Description
Search Service	       8001	       Simulated flight search
Booking Service	       8002        Booking + confirmation
Orchestrator Service	 8004	       Multi-agent logic + routing
UI (Streamlit)	       8501	       Frontend interface

All services communicate through Docker’s internal DNS.

Tech Stack : 
FastAPI (microservices)
Streamlit (web UI)
Google ADK (multi-agent orchestration)
Python 3.10
Docker + Docker Compose
httpx (service-to-service communication)

Run the System with Docker Compose :
Ensure Docker Desktop is installed, then from the project root:
docker compose up --build
The UI will be available at: http://localhost:8501
All services start automatically and communicate internally.

🧪 Features :
✔ Multi-agent workflow using Google ADK
✔ Microservices architecture
✔ Dockerized and cloud-ready
✔ Mocked real-world flight search + booking
✔ Single-command deployment via docker-compose
✔ Clean service boundaries + REST APIs

🧩 Future Enhancements :
Integrate real airline APIs (Amadeus / Skyscanner)
Add PostgreSQL for persistent bookings
Implement authentication
Deploy to Google Cloud Run or Railway
Add async background booking jobs

Status : This is a prototype, designed to demonstrate system architecture, agent coordination, and containerized deployment.


