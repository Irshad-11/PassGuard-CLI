import sys
import time
import pyperclip
from passguard.ui import clear, banner, draw_table, loading_anim
from passguard.auth import login, logout, is_authed, get_session_time
from passguard.config import SESSION_TIME, Fore
from passguard.ml import gen_password
from passguard.warnings import check_weak

def add_entries_menu(conn):
    clear(); banner(get_session_time(conn, SESSION_TIME))
    print("ADD NEW ENTRY\n1. Account\n2. API Key\n3. SSH Key\n4. Note\n5. Cancel")
    ch = input("> ")
    t_map = {"1": "ACC", "2": "API", "3": "SSH", "4": "NOTE"}
    if ch in t_map:
        s = input("Service: "); u = input("User: "); p = input("Secret: ")
        conn.execute("INSERT INTO items VALUES(NULL,?,?,?,?)", (t_map[ch], s, u, p))
        check_weak(conn, s, u, p)
        conn.commit()
        loading_anim("Saving...")

def user_menu(conn, cfg):
    while is_authed(conn, SESSION_TIME):
        clear(); banner(get_session_time(conn, SESSION_TIME))
        print("1. Add\n2. View\n3. Generate\n4. Logout")
        ch = input("> ")
        if ch == "1": add_entries_menu(conn)
        elif ch == "3": 
            p = gen_password(conn); print(f"Gen: {p}")
            pyperclip.copy(p); input()
        elif ch == "4": logout(conn); break

def guest_menu(conn, cfg):
    while True:
        if is_authed(conn, SESSION_TIME): user_menu(conn, cfg)
        clear(); banner(0)
        print("GUEST MODE\n1. Login\n2. Exit")
        ch = input("> ")
        if ch == "1":
            key = input("Key: ")
            if login(conn, cfg['master'], key): user_menu(conn, cfg)
        elif ch == "2": sys.exit()