import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY
        first_name TEXT NOT NULL
        last_name TEXT NULL
        username TEXT NULL
        user_id INTEGER NOT NULL
    )""")


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, full_name, username, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO users (first_name, last_name, username, user_id) VALUES (?, ?, ?)',
                                       (full_name, username, user_id))


conn.commit()
conn.close()
