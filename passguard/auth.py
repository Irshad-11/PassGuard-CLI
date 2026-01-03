import time
from passguard.crypto import sha
from passguard.db import log

def get_session_time(conn, session_limit):
    r = conn.execute("SELECT start FROM session").fetchone()
    if not r: return 0
    elapsed = int(time.time()) - r[0]
    return max(0, session_limit - elapsed)

def login(conn, master_hash, key):
    if sha(key) == master_hash:
        conn.execute("DELETE FROM session")
        conn.execute("INSERT INTO session VALUES(?)", (int(time.time()),))
        conn.commit()
        log(conn, "AUTH_LOGIN", "SUCCESS")
        return True
    log(conn, "AUTH_LOGIN", "FAIL")
    return False

def logout(conn):
    conn.execute("DELETE FROM session")
    conn.commit()
    log(conn, "AUTH_LOGOUT", "SUCCESS")

def is_authed(conn, session_limit):
    rem = get_session_time(conn, session_limit)
    return rem > 0