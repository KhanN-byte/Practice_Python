'''
Pattern Matching & Substitution 
Regex

'''

import re

txt = 'My email is janedoe@example.com and my friends email is john@example.com'

new_txt = re.sub(r'\b[\w.-]+@[\w.-]+\.[\w.-]+\b', 'redacted', txt)
print(new_txt)

import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('example1.db')
c = conn.cursor()

# Create the users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Optionally, insert some sample data
c.execute("INSERT INTO users (name, email) VALUES ('Jane Doe', 'janedoe@example.com')")
c.execute("INSERT INTO users (name, email) VALUES ('John Smith', 'johnsmith@example.com')")
conn.commit()

# Select and print all data from the users table
c.execute("SELECT * FROM users")
rows = c.fetchall()
for r in rows:
    with open('customers.txt', 'a') as file:
        file.write(f'New Data: {r}\n')

# Close the connection
conn.close()

