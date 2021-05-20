import streamlit as st
from investmentMonteCarloSim import *


def runSim():
    runInvestmentMonteCarloSim(
        symbol, initialInvestment, monthlyInvestment, year)


st.header("Monte Carlo Simulation of Investment Returns Over Time (1000 simulations)")

symbol = st.text_input("Enter a stock or index to simulate investment OR")
symbol = st.selectbox(label="You can also select an example ticker from this list", options=[
                      "^SPX", "^DJI", "^NDQ", "AAPL", "GOOG", "AMZN"])
st.write("Example tickers: ^SPX = 'S&P 500', ^DIA = 'Dow Jones', ^NDQ = 'Nasdaq Composite AAPL = 'Apple', GOOG = 'Google', AMZN = 'Amazon'")

initialInvestment = st.number_input("Enter your initial investment")
monthlyInvestment = st.number_input("Enter your monthly investment")
year = int(st.number_input(
    "Enter the number of years that you want to simulate"))


if st.button("Run Monte Carlo Simulation"):
    runSim()
