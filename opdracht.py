import sqlite3
import pandas as pd

# Connection to the "opdracht" database
conn = sqlite3.connect('database.db')

# SQL query to retrieve the desired data
query = '''
    SELECT
        users.Name AS UserName,
        orders.Product AS Product,
        orders.Amount AS Amount
    FROM
        users
    LEFT OUTER JOIN
        orders ON users.id = orders.user_id
'''

# Retrieve data and place it into a pandas DataFrame
opdracht_data = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

print(opdracht_data)
