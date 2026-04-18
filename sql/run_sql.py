import sqlite3

conn = sqlite3.connect('sales.db')

with open('transformation.sql', 'r') as file:
    sql_script = file.read()

conn.executescript(sql_script)

print("Transformation complete!")