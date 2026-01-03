import sys
import time
import pyperclip

from passguard.ui import clear, banner, draw_table, loading_anim, version
from passguard.auth import login, logout, is_authed, get_session_time
from passguard.config import SESSION_TIME, Fore
from passguard.ml import gen_password
from passguard.warnings import check_weak


def add_entries_menu(conn):
    clear()
    banner(get_session_time(conn, SESSION_TIME))

    print("ADD NEW ENTRY")
    print("1. Account")
    print("2. API Key")
    print("3. SSH Key")
    print("4. Personal Note")
    print("5. Cancel")

    ch = input("> ")

    t_map = {
        "1": ("ACC", "Service", "Username"),
        "2": ("API", "Service", "Project"),
        "3": ("SSH", "Host/Server", "User"),
        "4": ("NOTE", "Title", "Category"),
    }

    if ch in t_map:
        t, l1, l2 = t_map[ch]
        s = input(f"{l1}: ")
        u = input(f"{l2}: ")
        p = input("Secret: ")

        conn.execute(
            "INSERT INTO items VALUES(NULL,?,?,?,?)",
            (t, s, u, p)
        )
        check_weak(conn, s, u, p)
        conn.commit()

        loading_anim("Securing")
        print(Fore.GREEN + "Entry saved.")
        time.sleep(1)


def view_entries_menu(conn):
    while True:
        clear()
        banner(get_session_time(conn, SESSION_TIME))

        print("VIEW ENTRIES")
        print("1. Accounts")
        print("2. API Keys")
        print("3. SSH Keys")
        print("4. Personal Notes")
        print("5. Back")

        ch = input("> ")

        types = {
            "1": "ACC",
            "2": "API",
            "3": "SSH",
            "4": "NOTE",
        }

        if ch == "5":
            break

        if ch in types:
            loading_anim("Decrypting")

            rows = conn.execute(
                "SELECT service, username, secret FROM items WHERE type=?",
                (types[ch],)
            ).fetchall()

            draw_table(
                ["Service / Title", "User / ID", "Secret / Value"],
                rows,
                [25, 20, 30]
            )

            input("\nPress Enter to continue...")


def user_menu(conn, cfg):
    while is_authed(conn, SESSION_TIME):
        clear()
        banner(get_session_time(conn, SESSION_TIME))

        warn_count = conn.execute(
            "SELECT COUNT(*) FROM warnings"
        ).fetchone()[0]

        if warn_count > 0:
            disp = warn_count if warn_count < 10 else "9+"
            print(Fore.RED + f"⚠ Password Warnings: [{disp}]")

        print("\n1. Add Entries")
        print("2. View Entries")
        print("3. Warnings")
        print("4. Logs")
        print("5. Generate Password")
        print("6. Help")
        print("7. Logout")

        ch = input("> ")

        if ch == "1":
            add_entries_menu(conn)

        elif ch == "2":
            view_entries_menu(conn)

        elif ch == "3":
            clear()
            banner(get_session_time(conn, SESSION_TIME))

            rows = conn.execute(
                "SELECT * FROM warnings"
            ).fetchall()

            draw_table(
                ["Service", "User", "Issue", "Score"],
                rows,
                [15, 15, 18, 10]
            )
            input()

        elif ch == "4":
            clear()
            banner(get_session_time(conn, SESSION_TIME))

            rows = conn.execute(
                "SELECT * FROM logs ORDER BY ts DESC LIMIT 15"
            ).fetchall()

            draw_table(
                ["Action", "Status", "Time"],
                rows,
                [25, 10, 25]
            )
            input()

        elif ch == "5":
            pw = gen_password(conn)
            print(Fore.YELLOW + f"\nML Generated: {pw}")
            pyperclip.copy(pw)
            print("(Copied to clipboard)")
            input()

        elif ch == "6":
            print("\nHELP")
            print("- Session lasts 5 minutes")
            print("- Password style learned from password.txt")
            print("- Weak passwords generate warnings")
            print("- CLI supports -copy flag")
            input()

        elif ch == "7":
            logout(conn)
            break


def guest_menu(conn, cfg):
    while True:
        if is_authed(conn, SESSION_TIME):
            user_menu(conn, cfg)

        clear()
        banner(0)

        print("GUEST MODE")
        print("1. Login")
        print("2. Generate Password")
        print("3. Password History")
        print("4. About")
        print("5. Exit")

        ch = input("> ")

        if ch == "1":
            key = input("Access Key: ")
            if login(conn, cfg["master"], key):
                user_menu(conn, cfg)

        elif ch == "2":
            pw = gen_password(conn)
            print(Fore.YELLOW + f"\nGenerated: {pw}")
            pyperclip.copy(pw)
            input()

        elif ch == "3":
            clear()
            banner(0)

            rows = conn.execute(
                "SELECT * FROM history ORDER BY ts DESC LIMIT 10"
            ).fetchall()

            draw_table(
                ["Password", "Score", "Time"],
                rows,
                [20, 10, 25]
            )
            input()
            
        elif ch == "4":
            clear()
            banner(0)
            version(0)
            print("PassGuard CLI - Secure Password Manager")
            print("Developed by Irshad Hossain\n")
            input("Press Enter to continue...")            

        elif ch == "5":
            sys.exit()
