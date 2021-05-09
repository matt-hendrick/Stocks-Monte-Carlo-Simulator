import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


def runMonteCarloSim(symbol="^SPX"):

    symbol = symbol.upper()

    style.use('ggplot')

    start = dt.datetime(1900, 1, 1)
    end = dt.datetime(2021, 5, 9)

    prices = web.DataReader(symbol, 'stooq', start, end)['Close']
    returns = prices.pct_change()

    last_price = prices[0]

    print(last_price, prices)

    # Number​ of Simulations
    num_simulations = 1000
    num_days = 252

    simulation_df = pd.DataFrame()

    for x in range(num_simulations):
        count = 0
        daily_vol = returns.std()

        price_series = []

        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)

        for y in range(num_days):
            if count == 251:
                break
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1

        simulation_df[x] = price_series

    simulation_df.T.describe(percentiles=[.95, .75, .5, .25, .05])
    fig = plt.figure()
    fig.suptitle('Monte Carlo Simulation: '+symbol)
    plt.plot(simulation_df)
    plt.axhline(y=last_price, color='r', linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('Price')
    st.pyplot(fig)
    fig2 = plt.figure()
    plt.plot(simulation_df.quantile(.10, axis=1), label="10% percentile")
    plt.plot(simulation_df.quantile(.25, axis=1), label="25% percentile")
    plt.plot(simulation_df.quantile(.50, axis=1), label="50% percentile")
    plt.plot(simulation_df.quantile(.75, axis=1), label="75% percentile")
    plt.plot(simulation_df.quantile(.90, axis=1), label="90% percentile")
    plt.axhline(y=last_price, color='r', linestyle='-')
    plt.legend()
    st.pyplot(fig2)
