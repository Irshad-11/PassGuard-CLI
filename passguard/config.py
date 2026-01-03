import string

SESSION_TIME = 300
CONFIG_FILE = "config.json"
DB_NAME = "pass_guard.db"
ML_FILE = "password.txt"

UGLY_CHARS = "-_<>/\\`"
CLEAN_PUNCT = "".join(c for c in "!@#$%^&*()+=?" if c not in UGLY_CHARS)

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class X:
        def __getattr__(self, _): return ""
    Fore = Style = X()
