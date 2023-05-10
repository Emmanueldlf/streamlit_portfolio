import requests
import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/edlf_picture.jpg")

with col2:
    st.title("Emmanuel de La Forest")
    content = """
    Hi, I am Emmanuel. I am currently transitioning toward a career in tech. I first learnt Ruby and RoR at Le Wagon, and it is only my second python app
    """

    st.write(content)
