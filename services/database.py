import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent.parent / 'monitoring.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            cpu_percent REAL NOT NULL,
            ram_percent REAL NOT NULL,
            disk_free_gb REAL NOT NULL,
            disk_total_gb REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def save_snapshot(cpu: float, ram: float, disk_free_gb: float, disk_total_gb: float):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO snapshots (timestamp, cpu_percent, ram_percent, disk_free_gb, disk_total_gb) "
        "VALUES (?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), cpu, ram, disk_free_gb, disk_total_gb)
    )
    conn.commit()
    conn.close()


def get_recent_snapshots(limit: int = 500):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT timestamp, disk_free_gb FROM snapshots ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return list(reversed(rows))

def reset_db():
    if DB_PATH.exists():
        DB_PATH.unlink()