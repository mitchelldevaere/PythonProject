from CommandLine import CommandLineApp
import pandas as pd

class ExcelWriter:
    def __init__(self, db_file):
        self.commandLine = CommandLineApp(db_file)

    def write_to_excel(self):
        with pd.ExcelWriter('database.xlsx') as writer:

            # Tabblad 1: Alle factuurlijnen
            self.commandLine.get_all_users().to_excel(writer, sheet_name='Alle_gebruikers', index=False)

            self.commandLine.get_all_orders().to_excel(writer, sheet_name='Alle_Orders', index=False)