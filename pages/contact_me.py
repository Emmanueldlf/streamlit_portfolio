# import requests
import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Email Address")
    message = st.text_area("Message")
    email = f"""\
Subject: New email
From: {user_email}
Body: {message}
        """
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Email sent succesfully")
