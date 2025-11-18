import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.sf_library

with open('Library_Usage_20251027.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    activities = []
    for row in reader:
        doc = {
            "patron_type": row["Patron Type Definition"].strip(),
            "age_range": row["Age Range"].strip(),
            "notice_preference": row["Notice Preference Definition"].strip(),
            "provided_email": row["Provided Email Address"].strip().upper() == "TRUE",
            "year_registered": row["Year Patron Registered"].strip(),
            "within_sf_county": row["Within San Francisco County"].strip().upper() == "TRUE",
            "branch_name": row["Home Library Definition"].strip(),
            "month": row["Circulation Active Month"].strip(),
            "year": row["Circulation Active Year"].strip(),
            "total_checkouts": int(row["Total Checkouts"].replace(",", "")) if row["Total Checkouts"].lower() != "null" else 0,
            "total_renewals": int(row["Total Renewals"].replace(",", "")) if row["Total Renewals"].lower() != "null" else 0
        }
        activities.append(doc)
    db.activities.insert_many(activities)
print("Data loaded into MongoDB!")

