from CommandLine import CommandLineApp
from ExcelWriter import ExcelWriter

if __name__ == "__main__":
    db_file = '../database.db'
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