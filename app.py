import streamlit as st


st.title("StockBot")


intro = st.container()
inp = st.container()

with intro:
    st.title("StockBot")
    st.subheader("Forecasting your stocks with Prophet")

with inp:
    inp = st.text_input("Enter ticker:")
