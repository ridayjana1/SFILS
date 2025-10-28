# Database Scripts

This folder contains all the initialization scripts that helps us (perhaps convert and) load the Excel sheet into the database tables.

The scripts that are used to modify (indexing, moving, updating, data cleaning, ...) the database tables (after the data is loaded into the database) are also included here.

# Database Scripts

This folder contains scripts and instructions related to the MySQL database schema and data import.

## Database Setup

- Tables for `patrons`, `branches`, and `activities` are created using SQL.
- All import and setup is handled via Python script (`app/load_data.py`).
- Example usage:
- mysql -u root -p
- source create_table.sql
- or by rnning the loader in the `app` folder:
- python load_data.py

## mySQL scripts
 `CREATE DATABASE sf_library;`
 `USE sf_library;`
 `CREATE TABLE patrons (
        patron_id INT AUTO_INCREMENT PRIMARY KEY,
        year_registered INT,
        age_range VARCHAR(40),
        notice_preference VARCHAR(20),
        provided_email BOOLEAN,
        within_sf_county BOOLEAN,
        patron_type VARCHAR(20)
     );

    CREATE TABLE branches (
         branch_id INT AUTO_INCREMENT PRIMARY KEY,
         branch_name VARCHAR(50)
    );

     CREATE TABLE activities (
         activity_id INT AUTO_INCREMENT PRIMARY KEY,
         patron_id INT,
         branch_id INT,
         circulation_active_month VARCHAR(10),
         circulation_active_year INT,
         total_checkouts INT,
         total_renewals INT,
        FOREIGN KEY (patron_id) REFERENCES patrons(patron_id),
         FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
     );

`SHOW TABLES;`
