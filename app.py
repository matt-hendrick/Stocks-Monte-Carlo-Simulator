import streamlit as st
from test import *


def runSim():
    runMonteCarloSim(symbol)


symbol = st.text_input("Enter a stock ticker")

st.write("Prominent example tickers: ^SPX = 'S&P 500', ^DIA = 'Dow Jones', ^NDQ = 'Nasdaq Composite AAPL = 'Apple', GOOG = 'Google', AMZN = 'Amazon'")

if st.button("Run Monte Carlo Simulation"):
    runSim()
