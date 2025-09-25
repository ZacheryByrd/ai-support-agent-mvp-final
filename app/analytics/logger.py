import sqlite3, os, time
from pathlib import Path

DB_PATH = Path(__file__).parent / "log.db"

def _init():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts INTEGER,
            user_id TEXT,
            question TEXT,
            answer TEXT,
            route TEXT,  -- 'faq' | 'escalated'
            resolved INTEGER
        )"""
    )
    conn.commit()
    conn.close()

_init()

def log_interaction(user_id: str, question: str, answer: str, route: str, resolved: bool):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO interactions (ts, user_id, question, answer, route, resolved) VALUES (?,?,?,?,?,?)",
        (int(time.time()), user_id, question, answer, route, 1 if resolved else 0)
    )
    conn.commit()
    conn.close()
