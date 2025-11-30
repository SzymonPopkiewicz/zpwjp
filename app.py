import streamlit as st
from data_fetcher import fetch_stock
from processing import compute_daily_returns, filter_date_range
from analysis import summary_stats
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from plots import plot_price_interactive

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META","APTV"]
ticker = st.sidebar.selectbox("Select Ticker", options=tickers, index=0)

start = st.sidebar.date_input("Start",pd.to_datetime("2024-11-01"))
end = st.sidebar.date_input("End")

data = fetch_stock(ticker, str(start), str(end))
data = compute_daily_returns(data)
data = filter_date_range(data, start, end)

st.plotly_chart(plot_price_interactive(data), use_container_width=True)


#fig, ax = plt.subplots(figsize=(10, 4))
#ax.plot(data["Date"], data["Close"])
#ax.tick_params(axis='x', labelrotation=45)
#plt.tight_layout()
#st.pyplot(fig)

stats = summary_stats(data)
st.subheader("📊 Statystyki")
st.dataframe(stats, hide_index=True)


st.subheader(f"Dane: {ticker}")
st.dataframe(data.sort_values("Date",ascending=False), hide_index=True)





