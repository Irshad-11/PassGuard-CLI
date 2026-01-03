import os
import string

# Session & Files
SESSION_TIME = 300
CONFIG_FILE = "config.json"
DB_NAME = "pass_guard.db"
ML_FILE = "password.txt"

# UI Constants
UGLY_CHARS = "-_<>/\\`"
CLEAN_PUNCT = "".join([c for c in "!@#$%^&*()+=?" if c not in UGLY_CHARS])

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class X: 
        def __getattr__(self, k): return ""
    Fore = Style = X()