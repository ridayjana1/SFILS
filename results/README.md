# Findings and Results

This folder contains key findings and performance metrics from analyzing the SFILS library database.

## Main Findings

- **Branch Activity:** The most active branches by total checkouts are displayed on the `/stats` page of the app. (Example: Main Branch had the highest activity.)
- **Patron Demographics:** The most common patron types and age ranges can be seen in the `/patrons` and `/activities` views.
- **Monthly Trends:** The busiest circulation months were [insert busiest months if you found them].


- There were [5] unique patrons in the dataset.
- Branch "Main" had [10] checkouts in total.
- Age group "0 to 9 years" had [3] patrons with renewals.


## Performance Metrics

- **Initial data loading:** Data import using `load_data.py` completed in approximately [time it took, e.g., “2 minutes”].
- **Query performance:** Most web app queries return results in less than 1 second.

## Normalization

- The database is normalized into separate `patrons`, `branches`, and `activities` tables to support flexible querying and reduce data redundancy. No single giant table is used.
