import streamlit as st

def display():
    st.title("Travel Blog")
    blog_post = st.text_area("Share your travel experience:")
    if st.button("Post Blog"):
        st.success("Your blog has been posted!")
