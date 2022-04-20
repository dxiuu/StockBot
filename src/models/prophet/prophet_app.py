import streamlit as st
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from prophet_model import ProphetModel

# configure page
st.set_page_config(page_title="StockBot", page_icon=None, layout="centered", initial_sidebar_state="expanded")

# construct navigation
menu = ["Stocks", "Forex", "Crypto"]
choice = st.sidebar.selectbox('Navigation', menu)

# assign containers
intro = st.container()
inputs = st.container()
predict = st.container()
indicators = st.container()

# fill containers
with intro:
    st.title("StockBot")
    st.subheader("Forecasting your stocks with Prophet")

with inputs:
    stock_ticker = st.text_input("Enter ticker:")
    n_years = st.slider('Forecast over:', 1, 10, 3)

with predict:
    if stock_ticker != '':
        
        pm = ProphetModel()
        data = pm.get_data(stock_ticker)
        pm.set_period(n_years)
        pm.create_dataframe(data)
        forecast = pm.predict()

        st.subheader(f'Forecast plot over {n_years} years')
        fig1 = plot_plotly(pm._model, forecast)
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Forecast components")
        fig2 = pm._model.plot_components(forecast)
        st.write(fig2)
