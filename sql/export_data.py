import pandas as pd
import sqlite3
import os

# Check current location
print("Running from:", os.getcwd())

# Connect to DB
conn = sqlite3.connect('sales.db')

# Load clean data
df = pd.read_sql("SELECT * FROM orders_clean", conn)

# Export CSV
df.to_csv("clean_data.csv", index=False)

print("✅ clean_data.csv created successfully!")