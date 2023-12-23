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
