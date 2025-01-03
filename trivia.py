import streamlit as st
import random

def display():
    st.title("Travel Trivia")
    st.write("Answer questions to earn rewards!")

    questions = {
        "Which country is known as the Land of the Rising Sun?": "Japan",
        "What is the capital of France?": "Paris",
        "Which country has the Great Wall?": "China"
    }

    question, answer = random.choice(list(questions.items()))
    options = ["China", "Japan", "Thailand", "India", "France", "Paris"]
    random.shuffle(options)

    user_answer = st.radio(question, options)

    if st.button("Submit Answer"):
        if user_answer == answer:
            st.success("Correct! You earned 10 points.")
        else:
            st.error("Incorrect. Try again!")