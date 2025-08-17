import sqlite3

DB_PATH = "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            bio TEXT NOT NULL
        );           
        """)
        conn.commit()

def get_all_users():
    with get_connection() as conn:
        rows = conn.execute("SELECT name, bio FROM users").fetchall()
    
    return {name:bio for name, bio in rows}

def insert_user(name, bio):
    with get_connection() as conn:
        conn.execute("INSERT INTO users (name,bio) VALUES (?,?)", (name, bio))
        conn.commit()
