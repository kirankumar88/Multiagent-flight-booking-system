import streamlit as st
from api_client import orchestrate_search, book_flight
from datetime import date

st.title("✈️ Flight Booking Assistant")
st.caption("Powered by Gemini + Multi-Agent Architecture")

# -------------------------
# SEARCH SECTION
# -------------------------
st.header("Search Flights")

cities = {
    "Delhi (DEL)": "DEL",
    "Dubai (DXB)": "DXB",
    "Hyderabad (HYD)": "HYD",
    "Mumbai (BOM)": "BOM",
    "Chennai (MAA)": "MAA",
    "Singapore (SIN)": "SIN"
}

origin_name = st.selectbox("Origin", list(cities.keys()))
dest_name = st.selectbox("Destination", list(cities.keys()))
date_value = st.date_input("Travel Date (YYYY-MM-DD)", date.today())

origin = cities[origin_name]
dest = cities[dest_name]
date_str = str(date_value)

if st.button("Search"):
    result = orchestrate_search(origin, dest, date_str)

    if "error" in result:
        st.error(f"Error: {result['error']}")
    elif "flights" in result and len(result["flights"]) > 0:
        st.subheader("Flights Found!")
        for f in result["flights"]:
            st.write(f"**Flight ID:** {f['id']}")
            st.write(f"**Airline:** {f['airline']}")
            st.write(f"**Date:** {f['date']}")
            st.write(f"**Price:** {f['price']}")
            st.write(f"**Seats:** {f['seats']}")
            st.write("---")
    else:
        st.info("No flights found.")

# -------------------------
# BOOKING SECTION
# -------------------------
st.header("Book a Flight")

flight_id = st.text_input("Enter Flight ID to Book")

if st.button("Book"):
    result = book_flight(flight_id)
    
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"Booking Confirmed! Booking ID: {result.get('booking_id')}")
