# import requests
import streamlit as st
import pandas


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

content2 = """
Below are some of my first apps
"""
st.info(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
