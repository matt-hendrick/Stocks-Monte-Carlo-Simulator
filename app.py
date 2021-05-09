import streamlit as st
from investmentMonteCarloSim import *


def runSim():
    runMonteCarloSim(symbol)


st.header("Monte Carlo Simulation of Stock Prices (1000 simulations)")

symbol = st.text_input("Enter a stock ticker")

st.write("Prominent example tickers: ^SPX = 'S&P 500', ^DIA = 'Dow Jones', ^NDQ = 'Nasdaq Composite AAPL = 'Apple', GOOG = 'Google', AMZN = 'Amazon'")

if st.button("Run Monte Carlo Simulation"):
    runSim()
