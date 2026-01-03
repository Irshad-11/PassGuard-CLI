import sqlite3
import pytest
from passguard.db import init_db, log

def test_init_db(tmp_path):
    db_file = tmp_path / "test_pg.db"
    init_db(str(db_file))
    assert db_file.exists()
    
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    assert "items" in tables
    assert "logs" in tables

def test_db_logging(temp_db):
    log(temp_db, "TEST_ACTION", "SUCCESS")
    res = temp_db.execute("SELECT action, status FROM logs").fetchone()
    assert res[0] == "TEST_ACTION"
    assert res[1] == "SUCCESS"