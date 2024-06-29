import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime  

# Prompt the user for the stock ticker symbol
stock_symbol = input("Enter the stock ticker symbol (e.g., AMD): ")

# Prompt the user for the start_date of the analysis
start_date = input("Enter the start date (YYYY-MM-DD): ")

# Get the current date
end_date = datetime.now().strftime('%Y-%m-%d')

# Convert start_date and end_date to datetime objects
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

# Download historical data for a stock
stock = yf.Ticker(stock_symbol)
historical_data = stock.history(period="max")

# Display the downloaded data
#stock_data.tail(20)

# Ensure the index is in datetime format and convert to timezone-naive
historical_data.index = pd.to_datetime(historical_data.index).tz_localize(None)

# Ensure the index is in datetime format
#historical_data.index = pd.to_datetime(historical_data.index)  #Explain...
#===============================================

# Filter data between the start_date and end_date
historical_data = historical_data[(historical_data.index >= start_date) & (historical_data.index <= end_date)]

# Reset index to include the date column for plotting
historical_data.reset_index(inplace=True)

# Plot the closing price as a line chart
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(historical_data['Date'], historical_data['Close'], label='Closing Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title(f'{stock_symbol} Stock Closing Price Over Time')
plt.grid(True)
plt.legend()
plt.show()

# Display the downloaded data (optional)
print(historical_data.head())