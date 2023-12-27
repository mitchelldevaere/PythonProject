**Python project**

**Requirements.txt:**
In dit bestand staan alle packages die het project gebruikt. dit bestand is gemaakt door het commando pip freeze

**Productie nemen:**
De database moet worden geplaatst in de root van het project. Beter gezegd wordt de database geplaatst in de folder net boven de modules folder
![image](https://github.com/mitchelldevaere/PythonProject/assets/91076821/5d2afd3f-37e3-43de-9753-84520032e774)

Verder moeten er geen andere instellingen gemaakt worden om het project te runnen.

**Doel:**
Het doel van dit project is het ontwikkelen van een command-line applicatie in Python voor het beheren van gebruikers en orders in een SQLite-database. De applicatie biedt verschillende functionaliteiten, waaronder het toevoegen van gebruikers, het plaatsen van orders, het opvragen van gebruikersinformatie, het tonen van alle orders en gebruikers, en het exporteren van de gegevens naar een Excel-bestand.

Hier is een overzicht van de belangrijkste componenten en functies:

**DatabaseConnector Class:**

Deze klasse biedt een interface voor het verbinden met een SQLite-database en het uitvoeren van query's. Het implementeert het __enter__ en __exit__ protocol, wat betekent dat het kan worden gebruikt met with statements om ervoor te zorgen dat de databaseverbinding correct wordt geopend en gesloten.

**CommandLineApp Class:**

Deze klasse fungeert als een tussenlaag tussen de gebruiker en de database. Het bevat methoden om gebruikers toe te voegen, orders te plaatsen en informatie op te vragen over gebruikers en orders.

**ExcelWriter Class:**

Deze klasse maakt gebruik van de CommandLineApp om gegevens uit de database op te halen en deze te exporteren naar een Excel-bestand met behulp van de pandas library.

**Hoofdprogramma (if name == "main"):**

In het hoofdprogramma wordt een instantie van CommandLineApp en ExcelWriter gemaakt, en er wordt een oneindige lus gestart om gebruikersinteractie mogelijk te maken. De gebruiker kan kiezen uit verschillende opties, zoals het toevoegen van gebruikers, het plaatsen van orders, het opvragen van informatie en het exporteren van gegevens naar Excel.
