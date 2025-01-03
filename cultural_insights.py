import streamlit as st

def display():
    st.title("Cultural Insights")
    country = st.selectbox("Choose a country", ["France", "Japan", "India", "Brazil"])
    if country:
        cultural_info = {
            "France": "Known for its art, cuisine, and the Eiffel Tower.",
            "Japan": "Famous for sushi, cherry blossoms, and samurai culture.",
            "India": "Renowned for its spices, Bollywood, and the Taj Mahal.",
            "Brazil": "Famous for Carnival, football, and the Amazon rainforest."
        }
        st.write(cultural_info[country])
        st.image(f"images/{country.lower()}.jpg", use_column_width=True)