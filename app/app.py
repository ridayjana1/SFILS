from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'user': 'root',            # change as needed
    'password': '',            # your MySQL password if you set one
    'host': 'localhost',
    'database': 'sf_library',
    'unix_socket': '/tmp/mysql.sock'
}

@app.route('/')
def home():
    html = """
    <h2>SF Library Data App</h2>
    <ul>
      <li><a href="/branches">Branches</a></li>
      <li><a href="/patrons">Patrons</a></li>
      <li><a href="/activities">Activities</a></li>
      <li><a href="/stats">Checkout Stats</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/branches')
def branches():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT branch_id, branch_name FROM branches')
    branches = cursor.fetchall()
    cursor.close()
    conn.close()
    html = """
    <h2>Library Branches</h2>
    <ul>
    {% for branch in branches %}
      <li>{{ branch[1] }}</li>
    {% endfor %}
    </ul>
    <a href="/">Home</a>
    """
    return render_template_string(html, branches=branches)

@app.route('/patrons')
def patrons():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('SELECT patron_id, year_registered, age_range, patron_type FROM patrons LIMIT 50')
    patrons_data = cursor.fetchall()
    cursor.close()
    conn.close()
    html = """
    <h2>Patrons</h2>
    <table border="1">
      <tr><th>ID</th><th>Year Registered</th><th>Age Range</th><th>Type</th></tr>
      {% for row in patrons %}
        <tr>
          <td>{{ row[0] }}</td>
          <td>{{ row[1] }}</td>
          <td>{{ row[2] }}</td>
          <td>{{ row[3] }}</td>
        </tr>
      {% endfor %}
    </table>
    <a href="/">Home</a>
    """
    return render_template_string(html, patrons=patrons_data)

@app.route('/activities')
def activities():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT activities.activity_id, patrons.patron_type, branches.branch_name, activities.circulation_active_month, activities.circulation_active_year, activities.total_checkouts, activities.total_renewals
           FROM activities
           JOIN patrons ON activities.patron_id = patrons.patron_id
           JOIN branches ON activities.branch_id = branches.branch_id
           LIMIT 50'''
    )
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    html = """
    <h2>Activities</h2>
    <table border="1">
    <tr>
      <th>ID</th><th>Patron Type</th><th>Branch</th><th>Month</th><th>Year</th><th>Checkouts</th><th>Renewals</th>
    </tr>
    {% for row in records %}
      <tr>
        <td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ row[2] }}</td><td>{{ row[3] }}</td><td>{{ row[4] }}</td><td>{{ row[5] }}</td><td>{{ row[6] }}</td>
      </tr>
    {% endfor %}
    </table>
    <a href="/">Home</a>
    """
    return render_template_string(html, records=records)

@app.route('/stats')
def stats():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT branches.branch_name, SUM(activities.total_checkouts)
           FROM activities
           JOIN branches ON activities.branch_id = branches.branch_id
           GROUP BY branches.branch_name
           ORDER BY SUM(activities.total_checkouts) DESC
           LIMIT 10'''
    )
    stats = cursor.fetchall()
    cursor.close()
    conn.close()
    html = """
    <h2>Top 10 Branches by Total Checkouts</h2>
    <table border="1">
      <tr><th>Branch</th><th>Total Checkouts</th></tr>
      {% for row in stats %}
        <tr><td>{{ row[0] }}</td><td>{{ row[1] }}</td></tr>
      {% endfor %}
    </table>
    <a href="/">Home</a>
    """
    return render_template_string(html, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
