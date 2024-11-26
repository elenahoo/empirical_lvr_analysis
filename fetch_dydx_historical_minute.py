import requests
import time
import csv
import pandas as pd
from io import StringIO

# API base URL and constant parameters
base_url = "https://data-api.cryptocompare.com/futures/v1/historical/open-interest/minutes?"

# Initial request parameters
params = {
    'market': 'dydxv4',
    'instrument': 'ETH-USD-VANILLA-PERPETUAL', 
    'limit': '60',
    'aggregate': '1',
    'fill': 'true',
    'apply_mapping': 'true',
    'groups': 'OHLC',
    'to_ts': '1727740800', ## 2024-10-01 00:00:00
    'response_format': 'CSV',
    'api_key': 'YOUR_API_KEY'  
}


# Function to make the API request and return the CSV data
def fetch_data(to_ts):
    params['to_ts'] = str(to_ts)  # Update the timestamp in the params
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.text  # Return the CSV content as text
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Function to parse the CSV response and find the minimum timestamp
def extract_min_timestamp(csv_data):
    f = StringIO(csv_data)
    reader = csv.DictReader(f)
    
    min_timestamp = None
    for row in reader:
        timestamp = int(row['TIMESTAMP'])
        if min_timestamp is None or timestamp < min_timestamp:
            min_timestamp = timestamp  # Update the minimum timestamp
    
    return min_timestamp

# Main loop to fetch data 10 times and append to a dataframe
all_data = pd.DataFrame()  # Initialize an empty dataframe

## (1659312000  #Starting from 2024-09-01 backwards 6 months)
current_timestamp = 1727740800 
num_requests = 1000 

for i in range(num_requests):
    print(f"Request {i + 1} with to_ts={current_timestamp}...")
    
    # Fetch the data from the API
    csv_data = fetch_data(current_timestamp)
    
    if csv_data:
        # Convert the CSV data to a pandas DataFrame
        data = pd.read_csv(StringIO(csv_data))
        
        # Append the new data to the all_data dataframe
        all_data = pd.concat([all_data, data], ignore_index=True)
        
        # Find the minimum TIMESTAMP in the fetched data
        min_timestamp = extract_min_timestamp(csv_data)
        if min_timestamp is None:
            print("No valid data found in response, stopping.")
            break
        
        # Update the current timestamp for the next request
        current_timestamp = min_timestamp - 1  # Move backward in time
        time.sleep(1)  # Sleep to avoid hitting rate limits
    else:
        print("Error fetching data, stopping.")
        break

# Display the dataframe with all fetched data
print("Data fetching completed!")
print(all_data.head())  # Show first few rows of the dataframe

all_data.to_csv('dydx_m_eth_usd_sep_oct24.csv')