import sys
import os
import json
from passguard.db import get_db, init_db
from passguard.crypto import sha
from passguard.config import CONFIG_FILE, DB_NAME, ML_FILE
from passguard.cli import run_cli
from passguard.menus import guest_menu

def main():
    if not os.path.exists(ML_FILE):
        with open(ML_FILE, "w") as f: f.write("K9#qP2!mZ7*r\n")

    conn, cfg = get_db()
    if not cfg:
        print("--- SETUP ---")
        path = input("DB Folder: ") or "."
        master = input("Master Key: ")
        db_p = os.path.join(path, DB_NAME)
        init_db(db_p)
        with open(CONFIG_FILE, "w") as f:
            json.dump({"db": db_p, "master": sha(master)}, f)
        conn, cfg = get_db()

    if not run_cli(conn, cfg, sys.argv[1:]):
        guest_menu(conn, cfg)

if __name__ == "__main__":
    main()