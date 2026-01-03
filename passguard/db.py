import sqlite3
import os
import json
from datetime import datetime
from passguard.config import CONFIG_FILE


def get_db():
    if os.path.exists(CONFIG_FILE):
        cfg = json.load(open(CONFIG_FILE))
        return sqlite3.connect(cfg["db"]), cfg
    return None, None


def log(conn, action, status):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("INSERT INTO logs VALUES(?,?,?)", (action, status, ts))
    conn.commit()


def init_db(path):
    conn = sqlite3.connect(path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, type TEXT, service TEXT, username TEXT, secret TEXT);
        CREATE TABLE IF NOT EXISTS logs(action TEXT, status TEXT, ts TEXT);
        CREATE TABLE IF NOT EXISTS session(start INTEGER);
        CREATE TABLE IF NOT EXISTS warnings(service TEXT, username TEXT, reason TEXT, score REAL);
        CREATE TABLE IF NOT EXISTS history(password TEXT, score REAL, ts TEXT);
    """)
    conn.commit()
    conn.close()
