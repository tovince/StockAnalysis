import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime

# Set up the Streamlit app
st.title('Stock Analysis')

# Prompt the user for the stock ticker symbol
stock_symbol = st.text_input("Enter the stock ticker symbol (e.g., AMD): ", "AMD")

# Prompt the user for the start_date of the analysis
start_date = st.text_input("Enter the start date (YYYY-MM-DD): ", "2023-01-01")

# Get the current date
end_date = datetime.now().strftime('%Y-%m-%d')

# Convert start_date and end_date to datetime objects
try:
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
except ValueError:
    st.error("Please enter the date in YYYY-MM-DD format.")
    st.stop()

# Download historical data for a stock
stock = yf.Ticker(stock_symbol)
historical_data = stock.history(period="max")

# Ensure the index is in datetime format and convert to timezone-naive
historical_data.index = pd.to_datetime(historical_data.index).tz_localize(None)

# Filter data between the start_date and end_date
historical_data = historical_data[(historical_data.index >= start_date) & (historical_data.index <= end_date)]

# Reset index to include the date column for plotting
historical_data.reset_index(inplace=True)

# Plot the closing price as a line chart
fig, ax = plt.subplots(figsize=(10, 5))  # Set the figure size
ax.plot(historical_data['Date'], historical_data['Close'], label='Closing Price')
ax.set_xlabel('Date')
ax.set_ylabel('Closing Price')
ax.set_title(f'{stock_symbol} Stock Closing Price Over Time')
ax.grid(True)
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Display the downloaded data
st.write(historical_data.head())
