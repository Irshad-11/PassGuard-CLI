import sqlite3
import os
import json
from passguard.config import CONFIG_FILE, DB_NAME, Fore
from datetime import datetime

def get_db():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            cfg = json.load(f)
        conn = sqlite3.connect(cfg["db"])
        return conn, cfg
    return None, None

def log(conn, action, status):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("INSERT INTO logs VALUES(?,?,?)", (action, status, now))
    conn.commit()

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, type TEXT, service TEXT, username TEXT, secret TEXT);
        CREATE TABLE IF NOT EXISTS logs(action TEXT, status TEXT, ts TEXT);
        CREATE TABLE IF NOT EXISTS session(start INTEGER);
        CREATE TABLE IF NOT EXISTS warnings(service TEXT, username TEXT, reason TEXT, score REAL);
        CREATE TABLE IF NOT EXISTS history(password TEXT, score REAL, ts TEXT);
    """)
    conn.commit()
    conn.close()