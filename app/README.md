# The App to Query, Retrieve, and Update Database

This folder contains the source code of the (minimal) application that allows user interaction with the database.
# SFILS Library Database Application

This folder contains the programming app built around the SFILS MySQL database.  
Here you will find:

- `app.py` — Flask web application for browsing and analyzing library data.
- `load_data.py` — Python script to import CSV library records into MySQL tables.
- `Library_Usage_20251027.csv` — Example dataset used.

## How to run the app

1. Install dependencies:
2. pip3 install flask mysql-connector-python
3. Ensure MySQL is running and data is imported. refer scripts/README.md
4. Run the web app:
5. python3 app.py

## Open a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features

- View branches, patrons, activities, and top checkout stats.
- Connects to your `sf_library` MySQL database.

