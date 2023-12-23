from DatabaseConnector import DatabaseConnector
import pandas as pd

class CommandLineApp:
    def __init__(self, db_file):
        self.db_connector = DatabaseConnector(db_file)

    def add_user(self, name, age):
        query = 'INSERT INTO users (name, age) VALUES (?, ?)'
        self.db_connector.execute_query(query, (name, age))

    def place_order(self, user_id, product, amount):
        query = 'INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)'
        self.db_connector.execute_query(query, (user_id, product, amount))

    def get_user_info(self, user_id):
        query = 'SELECT * FROM users WHERE id = ?'
        result = self.db_connector.execute_query(query, (user_id,))
        return pd.DataFrame(result, columns=['ID', 'Name', 'Age'])

    def get_all_users(self):
        query = 'SELECT * FROM users'
        result = self.db_connector.execute_query(query)
        return pd.DataFrame(result, columns=['ID', 'Name', 'Age'])

    def get_all_orders(self):
        query = '''
            SELECT
                orders.ID AS OrderID,
                users.Name AS UserName,
                orders.Product AS Product,
                orders.Amount AS Amount
            FROM
                orders
            LEFT JOIN
                users ON orders.user_ID = users.ID
        '''
        result = self.db_connector.execute_query(query)
        return pd.DataFrame(result, columns=['OrderID', 'UserName', 'Product', 'Amount'])