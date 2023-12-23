import sqlite3

class DatabaseConnector:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_connection()

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def execute_query(self, query, params=None):
        if not self.conn:
            self.connect()

        try:
            with self.conn:
                if params:
                    return self.conn.execute(query, params)
                else:
                    return self.conn.execute(query)
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return None

    def fetch_all(self, query, params=None):
        result = self.execute_query(query, params)
        if result:
            return result.fetchall()
        return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None

class CommandLineApp:
    def __init__(self, db_file):
        self.db_file = db_file
        self.db_connector = DatabaseConnector(db_file)

    def add_user(self, name, age):
        query = 'INSERT INTO users (name, age) VALUES (?, ?)'
        self.db_connector.execute_query(query, (name, age))

    def place_order(self, user_id, product, amount):
        query = 'INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)'
        self.db_connector.execute_query(query, (user_id, product, amount))

    def get_user_info(self, user_id):
        query = 'SELECT * FROM users WHERE id = ?'
        return self.db_connector.fetch_all(query, (user_id,))

    def get_all_users(self):
        query = 'SELECT * FROM users'
        return self.db_connector.fetch_all(query)

    def get_all_orders(self):
        query = 'SELECT * FROM orders'
        return self.db_connector.fetch_all(query)

