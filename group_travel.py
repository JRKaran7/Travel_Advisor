import streamlit as st

def display():
    st.title("Group Travel Planning")
    st.write("Collaborate with friends and family on your itinerary.")
    itinerary = st.text_area("Shared Itinerary:")
    if st.button("Save Itinerary"):
        st.success("Itinerary saved successfully!")