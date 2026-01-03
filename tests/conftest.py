import pytest
import sqlite3
import os
from passguard.db import init_db

@pytest.fixture
def temp_db(tmp_path):
    db_file = tmp_path / "test.db"
    init_db(str(db_file))
    conn = sqlite3.connect(str(db_file))
    yield conn
    conn.close()