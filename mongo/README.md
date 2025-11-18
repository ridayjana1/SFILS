# MISFILS
MISFILS: The MongoDB-based Implementation for the San Francisco Integrated Library System.

This folder contains the submission files for Assignment 2. The remaining folders contain the files from Assignment 1.

Make sure to keep all your Assignment 2 files inside this folder to keep the rest of the folders free from clutter. That way, it will be easier to grade both Assignment 1 and Assignment 2.


# SFILS MongoDB Migration
# SFILS Assignment 2: MongoDB Migration

This folder contains the MongoDB-based port of the San Francisco Library Information System (SFILS)project originally built with MySQL.
## Prerequisites

- Python 3
- [MongoDB](https://www.mongodb.com/try/download/community) installed and running locally on port 27017
- Python packages: `pymongo`



## Files

- `load_mongo.py` — Loads the library dataset from CSV into a MongoDB collection.
- `app_mongo.py` — Contains sample queries for analyzing the imported data.
- `Library_Usage_20251027.csv` — The dataset to import.

## Usage

1. Place `Library_Usage_20251027.csv` in this folder.
2. Run data loader:
  ```
  python load_mongo.py
  ```
3. Execute sample queries:
  ```
  python app_mongo.py
  ```

## Notes and Differences from SQL Version

- Data is stored in a single flexible MongoDB `activities` collection (no normalization).
- MongoDB allows for rapid prototyping and easy schema changes compared to MySQL.
