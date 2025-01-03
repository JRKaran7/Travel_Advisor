### File: main.py
import streamlit as st

# Sidebar navigation
st.sidebar.title("AI Travel Advisor")
menu_options = ["Home", "Plan Your Trip", "Group Travel", "Trivia", "Cultural Insights", "Blog"]
choice = st.sidebar.radio("Navigate", menu_options)

if choice == "Home":
    import home
    home.display()

elif choice == "Plan Your Trip":
    import plan_trip
    plan_trip.display()

elif choice == "Group Travel":
    import group_travel
    group_travel.display()

elif choice == "Trivia":
    import trivia
    trivia.display()

elif choice == "Cultural Insights":
    import cultural_insights
    cultural_insights.display()

elif choice == "Blog":
    import blog
    blog.display()

st.sidebar.markdown("---")
st.sidebar.write("Powered by AI Travel Advisor")
