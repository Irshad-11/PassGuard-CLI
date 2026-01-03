import sys
import pyperclip
from passguard.auth import login, is_authed
from passguard.ml import gen_password
from passguard.db import log
from passguard.warnings import check_weak
from passguard.config import SESSION_TIME

def cli_help():
    print("Usage:\n login <key>\n gen [-copy]\n add <type> <srv> <user> <pass>\n get <type> <srv> <user> [-copy]")

def run_cli(conn, cfg, args):
    if not args: return False
    cmd = args[0].lower()

    if cmd == "help":
        cli_help(); return True

    if cmd == "login":
        if len(args) < 2: return True
        if login(conn, cfg['master'], args[1]): print("Authenticated.")
        else: print("Failed.")
        return True

    if cmd == "gen":
        p = gen_password(conn)
        print(f"Password: {p}")
        if "-copy" in args: pyperclip.copy(p)
        return True

    if cmd == "add":
        if len(args) < 5: return True
        conn.execute("INSERT INTO items VALUES(NULL,?,?,?,?)", (args[1].upper(), args[2], args[3], args[4]))
        check_weak(conn, args[2], args[3], args[4])
        conn.commit()
        print("Entry Added."); return True

    if cmd == "get":
        if not is_authed(conn, SESSION_TIME): 
            print("Login required."); return True
        res = conn.execute("SELECT secret FROM items WHERE type=? AND service=? AND username=?", 
                          (args[1].upper(), args[2], args[3])).fetchone()
        if res:
            print(f"Secret: {res[0]}")
            if "-copy" in args: pyperclip.copy(res[0])
        else: print("Not found.")
        return True
    return False