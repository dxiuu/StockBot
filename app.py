import streamlit as st

#define containers
intro = st.container()
inp = st.container()

with intro:
    st.title("StockBot")
    st.subheader("Forecasting your stocks with Prophet")

with inp:
    inp = st.text_input("Enter ticker:")

#move ui elements from prophet_model.py into app.py