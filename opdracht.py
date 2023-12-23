import sqlite3
import pandas as pd

class DatabaseConnector:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def execute_query(self, query):
        if not self.conn:
            self.connect()

        with self.conn:
            return pd.read_sql_query(query, self.conn)

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None

# Create an instance of DatabaseConnector
db_connector = DatabaseConnector('database.db')

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

# Execute the query and retrieve data into a pandas DataFrame
opdracht_data = db_connector.execute_query(query)

# Close the database connection
db_connector.close_connection()

# Display the results
print(opdracht_data)
