import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "bi_app.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                username  TEXT    NOT NULL UNIQUE,
                email     TEXT    NOT NULL UNIQUE,
                password  TEXT    NOT NULL,
                is_active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT   NOT NULL DEFAULT (datetime('now'))
            )
        """)
        conn.commit()
