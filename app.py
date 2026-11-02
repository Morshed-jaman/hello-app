import streamlit as st
from logic import greet_name

st.title("Hello App")

name = st.text_input("What is your name?")

if name:
    st.write(greet_name(name))