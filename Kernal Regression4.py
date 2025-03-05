import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# File paths
path_djia = '/Users/kellya.alwood/Desktop/Download Data - INDEX_US_DOW JONES GLOBAL_DJIA.csv'
path_xau_usd = '/Users/kellya.alwood/Desktop/XAU_USD Historical Data.csv'

# Read the CSV files and ensure dates are parsed as datetime objects
data_djia = pd.read_csv(path_djia, parse_dates=['Date'])
data_xau_usd = pd.read_csv(path_xau_usd, parse_dates=['Date'])

# Clean the data: remove commas and convert numeric columns to floats
data_djia['Open'] = data_djia['Open'].str.replace(',', '').astype(float)
data_djia['High'] = data_djia['High'].str.replace(',', '').astype(float)
data_djia['Low'] = data_djia['Low'].str.replace(',', '').astype(float)
data_djia['Close'] = data_djia['Close'].str.replace(',', '').astype(float)

data_xau_usd['Price'] = data_xau_usd['Price'].str.replace(',', '').astype(float)
data_xau_usd['Open'] = data_xau_usd['Open'].str.replace(',', '').astype(float)
data_xau_usd['High'] = data_xau_usd['High'].str.replace(',', '').astype(float)
data_xau_usd['Low'] = data_xau_usd['Low'].str.replace(',', '').astype(float)

# Since 'merge_asof' is used, the data must be sorted by the 'Date' column
data_djia.sort_values('Date', inplace=True)
data_xau_usd.sort_values('Date', inplace=True)

# Perform an asof merge on the 'Date' column
merged_data = pd.merge_asof(data_xau_usd, data_djia, on='Date')

# Calculate the Pearson correlation coefficient between the 'Close' price of DJIA and 'Price' of XAU/USD
correlation = pearsonr(merged_data['Price'], merged_data['Close'])[0]

# Plotting the prices
plt.figure(figsize=(14, 7))

# Plot XAU/USD prices
plt.subplot(1, 2, 1)
plt.plot(merged_data['Date'], merged_data['Price'], label='XAU/USD Price', color='gold')
plt.title('XAU/USD Price Over Time')
plt.legend()

# Plot DJIA closing prices
plt.subplot(1, 2, 2)
plt.plot(merged_data['Date'], merged_data['Close'], label='DJIA Close', color='blue')
plt.title('DJIA Close Over Time')
plt.legend()

plt.tight_layout()
plt.show()

# Print the correlation
print(f"The Pearson correlation coefficient between XAU/USD Prices and DJIA Close prices is: {correlation:.4f}")




