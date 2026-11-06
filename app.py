import streamlit as st
from logic import add

st.title("Hello App")
a = st.number_input("First number")
b = st.number_input("Second number")
st.write(f"Sum: {add(a, b)}")
