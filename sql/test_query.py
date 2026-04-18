import sqlite3
import pandas as pd

conn = sqlite3.connect('sales.db')

query = "SELECT * FROM orders LIMIT 5"
query = """
SELECT DATE("Order Date") as order_date,
       SUM(Sales) as total_sales
FROM orders
GROUP BY order_date
ORDER BY order_date
"""
df = pd.read_sql(query, conn)

print(df)