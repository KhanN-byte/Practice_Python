'''
Connecting to SQL Database using SQLite3 module
'''


import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE users1 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
c.execute('''INSERT INTO users1 (name, email) VALUES (?, ?)''', ('John', 'john@example.com'))
c.execute('''INSERT INTO users1 (name, email) VALUES (?, ?)''', ('Jane', 'jane@example.com'))


conn.commit()
conn.close()


