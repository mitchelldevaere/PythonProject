import sqlite3
import pandas as pd

class DatabaseConnector:
    def __init__(self, db_file):
        self.db_file = db_file

    def execute_query(self, query, params=None):
        conn = sqlite3.connect(self.db_file)

        if params:
            result =  pd.read_sql_query(query, conn, params=params)
            conn.close()
            return result
        else:
            result =  pd.read_sql_query(query, conn)
            conn.close()
            return result

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
        return self.db_connector.execute_query(query, (user_id,))

    def get_all_users(self):
        query = 'SELECT * FROM users'
        return self.db_connector.execute_query(query)

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
        return self.db_connector.execute_query(query)

class ExcelWriter:
    def __init__(self, db_file):
        self.commandLine = CommandLineApp(db_file)

    def write_to_excel(self):
        with pd.ExcelWriter('database.xlsx') as writer:

            # Tabblad 1: Alle factuurlijnen
            self.commandLine.get_all_users().to_excel(writer, sheet_name='Alle_gebruikers', index=False)

            self.commandLine.get_all_orders().to_excel(writer, sheet_name='Alle_Orders', index=False)

if __name__ == "__main__":
    db_file = 'database.db'
    app = CommandLineApp(db_file)
    writer = ExcelWriter(db_file)

    while True:
        print("\n1. Gebruiker toevoegen\n2. Order plaatsen\n3. Gebruiker info opvragen\n4. Alle orders\n5. Alle gebruikers\n6. Data naar Excel\n7. Afsluiten")
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
            if not user_info.empty:
                print("Gebruiker info:")
                print(user_info)
            else:
                print("Gebruiker niet gevonden.")


        elif choice == '4':
            all_orders = app.get_all_orders()
            if not all_orders.empty:
                print("Alle Orders:")
                for order in all_orders.itertuples(index=False):
                    print(order)
            else:
                print("Geen orders gevonden.")


        elif choice == '5':
            all_users = app.get_all_users()
            if not all_users.empty:
                print("Alle gebruikers:")
                for user in all_users.itertuples(index=False):
                    print(user)

        elif choice == '6':
            writer.write_to_excel()
            print("Alle data wordt geplaatst in Excel.")

        elif choice == '7':
            break

        else:
            print("Ongeldige keuze.")
