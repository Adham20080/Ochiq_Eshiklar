import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY
first_name TEXT NOT NULL
last_name TEXT NULL
username TEXT NOT NULL)""")

conn.commit()
conn.close()
