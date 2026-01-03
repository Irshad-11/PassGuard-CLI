import os
import sys
import time
from datetime import datetime
from passguard.config import Fore, Style

def clear(): os.system("cls" if os.name == "nt" else "clear")

def banner(rem_time):
    time_col = Fore.GREEN if rem_time > 60 else Fore.RED
    print(Fore.CYAN + r"""
  _____                _____                    _         _____ _      ______ 
 |  __ \              / ____|                  | |       / ____| |    |_    _|
 | |__) |_ _ ___ ___| |  __ _   _  __ _ _ __ __| |______| |    | |      | |  
 |  ___/ _` / __/ __| | |_ | | | |/ _` | '__/ _` |______| |    | |      | |  
 | |  | (_| \__ \__ \ |__| | |_| | (_| | | | (_| |      | |____| |____ _| |_ 
 |_|   \__,_|___/___/\_____|\__,_|\__,_|_|  \__,_|       \_____|______|_____|
""")
    if rem_time > 0:
        print(f"{' ' * 20} {time_col}● SESSION EXPIRES IN: {rem_time}s\n")

def draw_table(headers, rows, widths):
    print("┌" + "┬".join("─" * w for w in widths) + "┐")
    head_str = "│"
    for h, w in zip(headers, widths):
        head_str += f" {h.ljust(w-2)} │"
    print(head_str)
    print("├" + "┼".join("─" * w for w in widths) + "┤")
    for row in rows:
        row_str = "│"
        for item, w in zip(row, widths):
            row_str += f" {str(item)[:w-2].ljust(w-2)} │"
        print(row_str)
    print("└" + "┴".join("─" * w for w in widths) + "┘")

def loading_anim(msg="Processing"):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(10):
        for frame in frames:
            sys.stdout.write(f"\r{Fore.CYAN}{frame} {msg}...")
            sys.stdout.flush()
            time.sleep(0.01)
    sys.stdout.write("\r" + " " * 40 + "\r")