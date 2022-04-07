import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas


class ProphetModel:
    def __init__(self, df, period, start):
        self._df = df
        self._period = period
        self._START = start
        self._forecast = None

    def get_data(self, ticker):
            TODAY = date.today().strftime("%Y-%m-%d")
            data = yf.download(ticker, self.START, TODAY)
            data.reset_index(inplace=True)
            return data

    def predict(self):
        m = Prophet()
        m.fit(self._df)
        future = m.make_future_dataframe(periods=self._period)
        self._forecast = m.predict(future)

    def plot_pred(self, model, n_years):
        st.subheader('Forecast data')
        st.write(self._forecast.tail())
            
        st.write(f'Forecast plot for {n_years} years')
        fig1 = plot_plotly(model, self._forecast)
        st.plotly_chart(fig1)

        st.write("Forecast components")
        fig2 = model.plot_components(self._forecast)
        st.write(fig2)

    def change_start(self, new_start):
        self._START = new_start
