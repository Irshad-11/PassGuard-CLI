import time
from passguard.auth import login, logout, is_authed, get_session_time
from passguard.crypto import sha

def test_login_flow(temp_db):
    master_key = "secret123"
    master_hash = sha(master_key)
    
    # Test Failed Login
    assert login(temp_db, master_hash, "wrong_key") is False
    
    # Test Successful Login
    assert login(temp_db, master_hash, master_key) is True
    assert is_authed(temp_db, 300) is True

def test_session_expiry(temp_db):
    # Manually insert an expired session (1 hour ago)
    old_time = int(time.time()) - 3601
    temp_db.execute("INSERT INTO session VALUES(?)", (old_time,))
    assert is_authed(temp_db, 300) is False

def test_logout(temp_db):
    temp_db.execute("INSERT INTO session VALUES(?)", (int(time.time()),))
    logout(temp_db)
    res = temp_db.execute("SELECT * FROM session").fetchone()
    assert res is None