import requests
import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Email Address")
    message = st.text_area("Message")
    button = st.form_submit_button()
    if button:
        message = message + user_email
