import streamlit as st
import requests

def display():
    st.title("Plan Your Trip")
    destination = st.text_input("Enter Destination:")
    if destination:
        st.write(f"Fetching weather and travel updates for {destination}...")
        try:
            response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={destination}")
            if response.status_code == 200:
                weather = response.json()["current"]["condition"]["text"]
                st.success(f"Current weather in {destination}: {weather}")
            else:
                st.error("Unable to fetch weather data.")
        except Exception as e:
            st.error(f"Error: {e}")
