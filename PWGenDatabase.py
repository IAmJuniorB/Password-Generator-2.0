import sqlite3
from PasswordGenerator2 import *

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('passwords.db')

# Create a table to store the passwords
conn.execute('''CREATE TABLE IF NOT EXISTS passwords
            (id INTEGER PRIMARY KEY, 
            length INTEGER,
            password TEXT,
            date_generated DATE)''')

# Insert the generated password into the table
conn.execute("INSERT INTO passwords (length, password, date_generated) VALUES (?, ?, datetime('now'))", (passlen.get(), passstr.get()))

conn = sqlite3.connect('passwords.db')
c = conn.cursor()

c.execute("SELECT * from passwords")
print(c.fetchall())

# Commit the changes and close the connection
conn.commit()
conn.close()
