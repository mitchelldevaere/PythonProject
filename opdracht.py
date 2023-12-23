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

if __name__ == "__main__":
    db_file = 'database.db'
    app = CommandLineApp(db_file)

    while True:
        print("\n1. Add User\n2. Place Order\n3. Get User Info\n4. List All Orders\n5. List all users\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            age = input("Enter user age: ")
            app.add_user(name, age)
            print("User added successfully!")

        elif choice == '2':
            user_id = input("Enter user ID: ")
            product = input("Enter product: ")
            amount = input("Enter amount: ")
            app.place_order(user_id, product, amount)
            print("Order placed successfully!")

        elif choice == '3':
            user_id = input("Enter user ID: ")
            user_info = app.get_user_info(user_id)
            if user_info:
                print("User Info:")
                print(user_info)
            else:
                print("User not found.")

        elif choice == '4':
            all_orders = app.get_all_orders()
            if all_orders:
                print("All Orders:")
                for order in all_orders:
                    print(order)
            else:
                print("No orders found.")

        elif choice == '5':
            all_users = app.get_all_users()
            if all_users:
                print("All users:")
                for user in all_users:
                    print(user)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please enter a valid option.")
