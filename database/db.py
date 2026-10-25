import sqlite3
from flask import g

DATABASE = "spendly.db"

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db

def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS."""
    db = sqlite3.connect(DATABASE)
    with db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date DATE NOT NULL,
                description TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
        """)
    db.close()

def seed_db():
    """Inserts sample data for development."""
    db = sqlite3.connect(DATABASE)
    with db:
        # Check if users table is empty
        cursor = db.execute("SELECT count(*) FROM users")
        if cursor.fetchone()[0] == 0:
            # Insert a test user (using a hashed password for consistency)
            # password123 -> hashed
            from werkzeug.security import generate_password_hash
            hashed_password = generate_password_hash("password123")
            cursor = db.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                ("testuser", "test@example.com", hashed_password)
            )
            user_id = cursor.lastrowid

            # Insert sample expenses in INR
            expenses = [
                (user_id, 1200.0, "Grocery", "2023-10-01", "Weekly supermarket run"),
                (user_id, 450.0, "Transport", "2023-10-02", "Auto rickshaw to office"),
                (user_id, 3000.0, "Rent", "2023-10-01", "October room rent"),
                (user_id, 250.0, "Dining", "2023-10-03", "Street food snack"),
                (user_id, 1500.0, "Internet", "2023-10-05", "Monthly broadband bill"),
                (user_id, 800.0, "Entertainment", "2023-10-06", "Movie ticket"),
                (user_id, 2000.0, "Shopping", "2023-10-07", "New clothes"),
                (user_id, 600.0, "Health", "2023-10-08", "Pharmacy medicines"),
            ]
            db.executemany(
                "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
                expenses
            )
    db.close()
