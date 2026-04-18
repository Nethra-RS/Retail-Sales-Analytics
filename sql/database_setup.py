import sqlite3
import pandas as pd

# Load raw data
df = pd.read_csv('../data/train.csv')

# Connect to database
conn = sqlite3.connect('sales.db')

# Create raw table
df.to_sql('orders', conn, if_exists='replace', index=False)

print("Raw data loaded into SQL")