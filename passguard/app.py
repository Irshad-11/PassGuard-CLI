import sys
import os
import json

from passguard.db import get_db, init_db
from passguard.crypto import sha
from passguard.config import CONFIG_FILE, DB_NAME, ML_FILE
from passguard.cli import run_cli
from passguard.menus import guest_menu


def main():
    # Ensure ML corpus exists
    if not os.path.exists(ML_FILE):
        with open(ML_FILE, "w") as f:
            f.write("K9#qP2!mZ7*r\n")

    conn, cfg = get_db()

    # First-time setup
    if not cfg:
        print("--- SETUP ---")
        path = input("DB Folder: ") or "."
        master = input("Access Key: ")

        db_path = os.path.join(path, DB_NAME)
        init_db(db_path)

        with open(CONFIG_FILE, "w") as f:
            json.dump({"db": db_path, "master": sha(master)}, f)

        conn, cfg = get_db()

    # CLI → fallback to TUI
    if not run_cli(conn, cfg, sys.argv[1:]):
        guest_menu(conn, cfg)


if __name__ == "__main__":
    main()
