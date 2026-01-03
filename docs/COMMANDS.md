# 📖 PassGuard-CLI Command Reference

This document provides a detailed breakdown of all available commands, flags, and interactive menu options within PassGuard.

---

## 🖥️ 1. Command Line Interface (CLI)
CLI commands are used for quick automation, scripts, or terminal power-users. Commands follow the syntax: `python -m passguard.app <command> [arguments] [flags]`

### A. Authentication
| Command | Arguments | Description |
|:---|:---|:---|
| `login` | `<key>` | Validates the master key and starts a 300s (5min) session. |
| `logout` | None | Immediately terminates the active session. |

### B. Vault Operations
| Command | Arguments | Flags | Description |
|:---|:---|:---|:---|
| `add` | `<type> <service> <user> <pass>` | None | Adds a secret. Types: `ACC`, `API`, `SSH`, `NOTE`. |
| `get` | `<type> <service> <user>` | `-copy` | Retrieves a secret. Requires active session. |

### C. Password Generation
| Command | Arguments | Flags | Description |
|:---|:---|:---|:---|
| `gen` | None | `-copy` | Generates a password based on the `password.txt` ML corpus. |

### D. Utility
| Command | Arguments | Description |
|:---|:---|:---|
| `help` | None | Displays the quick-reference command list. |

---

## 🖱️ 2. Text User Interface (TUI)
The TUI is triggered by running the application without arguments: `python -m passguard.app`.

### Main Menu (Guest Mode)
Used when no session is active.
1. **Login**: Prompt for Master Key to enter User Mode.
2. **Generate Password**: Quick generation without saving to vault.
3. **View History**: View the last 10 passwords generated (Stored in `history` table).
4. **Exit**: Closes the application.

### Main Menu (User Mode)
Accessible only after successful login.
1. **Add Entries**: Opens a sub-menu to choose entry type and input data.
2. **View Entries**: 
    - **Accounts**: Web/App logins.
    - **API Keys**: Development secrets.
    - **SSH Keys**: Server credentials.
    - **Notes**: Secure text snippets.
3. **Password Warnings**: Lists entries flagged for "Low Entropy" or "Pattern Reuse."
4. **System Logs**: View the internal audit trail (Actions, Status, Timestamps).
5. **Generate Password**: High-entropy generation with auto-copy to clipboard.
6. **Help**: Displays system limits and security tips.
7. **Logout**: Returns to Guest Mode.

---

## 🧠 3. ML Corpus Configuration (`password.txt`)
PassGuard does not use a rigid set of rules. It learns "Strong Style" from this file.

### How to Modify:
Open `password.txt` in any text editor. Add passwords you consider "Ideal":
- **To increase length**: Add longer passwords.
- **To increase complexity**: Add passwords with more symbols (e.g., `!@#$%`).
- **To decrease complexity**: Remove symbol-heavy examples.

> [!IMPORTANT]
> PassGuard calculates the **Average Weight** of characters in this file. It will not copy these passwords exactly, but it will mimic their structure.

---

## 🛠️ 4. Quick Examples

**Start a session and add a Gmail account:**
```bash
python -m passguard.app login MyMasterKey123
python -m passguard.app add ACC Google myname@gmail.com MyStrongPass!