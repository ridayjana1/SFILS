import csv
import mysql.connector

# Update these with credentials you used when setting up MySQL!
DB_CONFIG = {
    'user': 'root',            # or your 'sfuser'
    'password': '',            # your password here, if any
    'host': 'localhost',
    'database': 'sf_library',
    'unix_socket': '/tmp/mysql.sock'
}

CSV_FILE = 'Library_Usage_20251027.csv'   # adjust to your actual file path

def main():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Track unique branches so we only insert once
    branches = {}
    # Track unique patrons so we only insert once (by a composite key of relevant fields)
    patrons = {}

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Insert branch if new
            branch_name = row['Home Library Definition'].strip()
            if branch_name not in branches:
                cursor.execute(
                    "INSERT INTO branches (branch_name) VALUES (%s)", [branch_name]
                )
                conn.commit()
                branches[branch_name] = cursor.lastrowid
            branch_id = branches[branch_name]

            # Insert patron if new (define uniqueness by all relevant fields)
            patron_key = (
                row['Patron Type Definition'].strip(),
                row['Age Range'].strip(),
                row['Notice Preference Definition'].strip(),
                row['Provided Email Address'].strip(),
                row['Year Patron Registered'].strip(),
                row['Within San Francisco County'].strip(),
            )
            if patron_key not in patrons:
                cursor.execute(
                    """INSERT INTO patrons 
                    (year_registered, age_range, notice_preference, provided_email, within_sf_county, patron_type) 
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    [
                        int(row['Year Patron Registered']) if row['Year Patron Registered'] else None,
                        row['Age Range'].strip(),
                        row['Notice Preference Definition'].strip(),
                        True if row['Provided Email Address'].strip().upper() == 'TRUE' else False,
                        True if row['Within San Francisco County'].strip().upper() == 'TRUE' else False,
                        row['Patron Type Definition'].strip()
                    ]
                )
                conn.commit()
                patrons[patron_key] = cursor.lastrowid
            patron_id = patrons[patron_key]

            # Insert activity record
            cursor.execute(
                """INSERT INTO activities 
                (patron_id, branch_id, circulation_active_month, circulation_active_year, total_checkouts, total_renewals) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                [
                    patron_id,
                    branch_id,
                    row['Circulation Active Month'].strip(),
                    int(row['Circulation Active Year']) if row['Circulation Active Year'] and row['Circulation Active Year'].lower() != 'null' else None,
                    int(row['Total Checkouts'].replace(',', '')) if row['Total Checkouts'] and row['Total Checkouts'].lower() != 'null' else 0,
                    int(row['Total Renewals'].replace(',', '')) if row['Total Renewals'] and row['Total Renewals'].lower() != 'null' else 0,
                ]
            )
            conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
