import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas


class ProphetModel:
    def __init__(self, df=None, period=None, start="2015-01-01"):
        self._df = df
        self._period = period
        self._START = start
        self._forecast = None
        self._model = None

    def get_data(self, ticker):
        TODAY = date.today().strftime("%Y-%m-%d")
        data = yf.download(ticker, self._START, TODAY)
        data.reset_index(inplace=True)
        return data
    
    def set_period(self, n_years):
        self._period = n_years * 365
    
    def create_dataframe(self, data):
        df_t = data[['Date', 'Close']]
        df_t = df_t.rename(columns={'Date': 'ds', 'Close': 'y'})
        self._df = df_t        

    def predict(self):
        self._model = Prophet()
        self._model.fit(self._df)
        future = self._model.make_future_dataframe(periods=self._period)
        self._forecast = self._model.predict(future)
        return self._forecast

    def plot_pred(self, model, n_years):
        st.subheader('Forecast data')
        st.write(self._forecast.tail())
            
        st.subheader(f'Forecast plot over {n_years} years')
        fig1 = plot_plotly(model, self._forecast)
        st.plotly_chart(fig1)

        st.subheader("Forecast components")
        st.write('Trend and seasonality')
        fig2 = model.plot_components(self._forecast)
        st.write(fig2)

    def change_start(self, new_start):
        self._START = new_start
