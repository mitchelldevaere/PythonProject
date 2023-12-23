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
        except Exception as e:
            print(f"Error executing query: {str(e)}")
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
        return self.db_connector.execute_query(query, (user_id,))

    def get_all_users(self):
        query = 'SELECT * FROM users'
        return self.db_connector.execute_query(query)

    def get_all_orders(self):
        query = 'SELECT * FROM orders'
        return self.db_connector.execute_query(query)

if __name__ == "__main__":
    db_file = 'database.db'
    app = CommandLineApp(db_file)

    while True:
        print("\n1. Gebruiker toevoegen\n2. Order plaatsen\n3. Gebruiker info opvragen\n4. Alle orders\n5. Alle gebruikers\n6. Afsluiten")
        choice = input("kies welke optie: ")

        if choice == '1':
            name = input("Geef naam: ")
            age = input("Geef leeftijd: ")
            app.add_user(name, age)
            print("Gebruiker succesvol toegevoegd")

        elif choice == '2':
            user_id = input("Geef gebruiker ID: ")
            product = input("Geef product: ")
            amount = input("Geef aantal: ")
            app.place_order(user_id, product, amount)
            print("Order succesvol geplaatst")

        elif choice == '3':
            user_id = input("Geef gebruiker ID: ")
            user_info = app.get_user_info(user_id)
            if user_info:
                print("Gebruiker info:")
                print(user_info)
            else:
                print("Gebruiker niet gevonden.")

        elif choice == '4':
            all_orders = app.get_all_orders()
            if all_orders:
                print("Alle Orders:")
                for order in all_orders:
                    print(order)
            else:
                print("Geen orders gevonden.")

        elif choice == '5':
            all_users = app.get_all_users()
            if all_users:
                print("Alle gebruikers:")
                for user in all_users:
                    print(user)

        elif choice == '6':
            break

        else:
            print("Ongeldige keuze.")
