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
            if params:
                return self.conn.execute(query, params)
            else:
                return self.conn.execute(query)
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return None
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
