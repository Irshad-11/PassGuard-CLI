<img src="https://raw.githubusercontent.com/Irshad-11/Documents/refs/heads/main/passguardCLI.png" alt="Banner">

<h1 align="center">PassGuard-CLI <img src="https://img.shields.io/badge/Coming%20Soon-8A2BE2" alt="Coming Soon Badge"></h1>
<p align="center">
  <img src="https://img.shields.io/badge/UNIX%20style-437057" alt="Coming Soon Badge">
  <img src="https://img.shields.io/badge/Scriptable%20CLI-1C352D" alt="Coming Soon Badge">
  <img src="https://img.shields.io/badge/Interactive%20TUI-064232" alt="Coming Soon Badge">
</p>

## What is PassGuard-CLI?

PassGuard-CLI is a secure, terminal-based password manager. It allows users to store, manage, and generate passwords, API keys, SSH entries, finance details, and personal notes in an encrypted local database. The tool supports both quick UNIX-style subcommands for fast operations and an interactive terminal GUI mode for more exploratory usage. All data is encrypted locally using strong algorithms, with a Access key for admin privilege. It emphasizes security features like rate-limited logins, password history, audit logs, backups, and expiry warnings. Built as a single executable.

## Why PassGuard-CLI?

Developers often prefer terminal-based tools because they integrate seamlessly into workflows, avoid bloated GUIs, and allow scripting/automation. PassGuard-CLI caters to this by providing:

- **Quick Commands**: For devs who need instant access (e.g., generate and copy a password in one line without prompts).
- **Offline Security**: No cloud dependency—everything stays on your machine, reducing attack surfaces.
- **Customization for Devs**: Handles API keys, SSH paths, and structured categories efficiently for hundreds of entries.
- **Developer-Friendly Features**: Random password generation with policies, clipboard integration for quick copy-paste into workflows, It's open-source, so you can fork and modify it for your needs.
- **Minimalist and Efficient**: No web bloat, just pure CLI power for those who live in terminals.

If you're tired of browser extensions or heavy apps, PassGuard-CLI keeps your secrets safe and accessible via the command line.

## How to Run PassGuard-CLI on Your Machine

[To be filled later: Installation instructions, e.g., git clone, build with C++, dependencies like SQLite/OpenSSL.]

## Available CLI Commands

PassGuard-CLI supports UNIX-style subcommands for quick operations. Some require login (session-based, expires after 5 minutes ). Use `pass --help` for full usage.

### 1. `pass init`

- **Functionality**: Initializes the database and sets the Access key if not already set. User must run this manually on first use.
  
- **Demo**:
  
  ```
  $ pass init
  
  Welcome to PassGuard-CLI v1.0.0!
  Initializing setup...
  
  Set Access key: ******** (e.g., MyStrongPass123!)
  Confirm Access key: ********
  
  Access Key set Successfully. (Enforced policy: min 6 chars, 1 upper, 1 lower, 1 num, 1 special)
  Database created at ~/.passguard/passman.db (encrypted).
  ```
  

### 2. `pass gen [flags]`

- **Functionality**: Generates a random strong password (default: length 8, includes uppercase/lowercase/numbers/specials). No prompts—direct output. Flags for customization.
  
- **Flags**:
  
  - `--len <number>`: Set length (default 8).
  - `--nonum`: Disallow numbers (default yes).
  - `--nochar`: Disallow special chars (default yes).
  - `--noupper`: Disallow uppercase (default yes).
  - `--copy`: Copy to clipboard.
- **Demo**:
  
  ```
  $ pass gen --len 16 --copy
  
  Generated: XyZ1aBcD!EfGh2IjK
  Copied to clipboard!
  ```
  

### 3. `pass login`

- **Functionality**: Logs in with Access key, starting a session for protected commands (e.g. `get`,`add`,`del`)
  
- **Demo**:
  
  ```
  $ pass login
  
  Access key: ********
  
  Successful Login.
  Session Started. Expires in 5 minutes .
  ```
  
  Failed attempt:
  
  ```
  $ pass login
  
  Access key: wrongpass
  
  Failed. Try again in 10 seconds... (Increases by 10s per fail; locks after 5 fails for 1 hour)
  ```
  

### 4. `pass add <category> [flags]`

- **Functionality**: Adds a new entry to a category (password, apikey, ssh, finance, personal). Prompts for details if flags incomplete. Requires login.
  
- **Categories**: password, apikey, ssh, finance, personal.
  
- **Flags**:
  
  - **password**: `--for <company> --username <user> --password <pass>` (empty password for random).
  - **apikey**: `--for <company> --service <service> --key <key>`.
  - **ssh**: `--alias <name> --username <user> --path <path>`.
  - **finance**: `--type <debit/credit/bank> --holder <name> --number <number> --expiry <MM/YY>`.
  - **personal**: `--title <title> --content <text>`.
- **Demo (Password)**:
  
  ```
  $ pass add password --for Facebook --username abc@11s --password ""
  
  (Assumes logged in; else prompts for master)
  Generating random strong password...
  Generated: XyZ1aBcD!EfGh2IjK (Strength checked against policy)
  Account added successfully.
  ```
  
- **Demo (API Keys)**:
  
  ```
  $ pass add apikey --for project2 --service GitHub --key ghp_abc123xyz
  
  API key for GitHub added successfully.
  ```
  
- **Demo (SSH)**:
  
  ```
  $ pass add ssh --alias prod-server --username ubuntu --path /home/user/.ssh/id_rsa_prod
  
  SSH entry for prod-server added successfully.
  ```
  
- **Demo (Finance)**:
  
  ```
  $ pass add finance --type debit --holder "Irshad Hossain" --number 1234-5678-9012-3456 --expiry 12/27
  
  Finance entry added successfully.
  ```
  
- **Demo (Personal)**:
  
  ```
  $ pass add personal --title "My NID" --content "233 221 344"
  
  Personal note added successfully.
  ```
  

### 5. `pass get <category> <identifier> [flags]`

- **Functionality**: Retrieves an entry (e.g., password). Requires login.
  
- **Flags**: `--copy`: Copy password/key to clipboard.
  
- **Demo**:
  
  ```
  $ pass get password abc@11s --copy
  
  Password for Facebook: XyZ1aBcD!EfGh2IjK
  Copied!
  ```
  

### 6. `pass list <category>`

- **Functionality**: Lists entries in a category (e.g., as table). Requires login.
  
- **Demo**:
  
  ```
  $ pass list password
  
  +-----------+----------+-----------------+-------------+
  | Service   | Username | Last Changed    | Expiry Warn |
  +-----------+----------+-----------------+-------------+
  | Facebook  | abc@11s  | 2025-08-21      | None        |
  +-----------+----------+-----------------+-------------+
  ```
  

### 7. `pass change <category> <identifier> [flags]`

- **Functionality**: Changes details (e.g., password). Old value saved to history. Requires login.
  
- **Demo**:
  
  ```
  $ pass change password abc@11s --password NewPass456!
  
  Changed successfully. Old password saved to history.
  ```
  

### 8. `pass delete <category> <identifier>`

- **Functionality**: Deletes an entry (moved to recoverable trash for 7 days). Requires login and confirmation.
  
- **Demo**:
  
  ```
  $ pass delete password abc@11s
  
  Confirm deletion? (y/n): y
  Deleted. Recoverable for 7 days.
  ```
  

### 9. `pass settings [subcommand]`

- **Functionality**: Manages settings (e.g., change master, backup, logs). Requires login.
  
- **Subcommands**: change-master, backup, recover, expiry-warn, audit-logs, policies.
  
- **Demo** (Audit Logs):
  
  ```
  $ pass settings audit-logs
  
  Audit Logs:
  - 2025-08-21 10:00: Successful login
  - 2025-08-21 10:05: Accessed Facebook password
  ```
  

### 10. `pass reset`

- **Functionality**: Wipes database and resets (for forgot master). Loses all data.
  
- **Demo**:
  

```
  $ pass reset

  Warning: This wipes all data! Confirm? (y/n): y
  Reset complete. Re-initialize with 'pass init'.
```

### 11. `pass logout`

- **Functionality**: Ends the current session.
  
- **Demo**:
  

```
  $ pass logout

  Session ended.  
```

## Available Interactive Terminal

Run `pass` without subcommands to enter interactive mode. It's a menu-driven GUI in the terminal (using tables for pretty UI). Non-logged-in options are limited; login for full access.

### Initial Run (First Time)

```
$ pass

Welcome to PassGuard-CLI v1.0.0!
Initializing setup...

Set Access key: ********
Confirm MasteAccess key*****

Master pasAccess keyssfully.
Database created.

pass> 
```

### Non-Logged-In Menu

```

Available options (not logged in):
1. Random Password Generator
2. Login
3. Settings (limited)
4. Exit

pass> 1

Length: 16 (or enter custom)
Generated: XyZ1aBcD!EfGh2IjK (Strong by default; no allow prompts)

pass> 2

Access key: ********

Successful Login.
Session Started. Expires in 5 minutes.
```

### Logged-In Menu

```
pass> 

Available options (logged in):
1. Random Password Generator
2. Category
3. Settings
4. Log Out

pass> 2

Categories:
1. Password Manager
2. API Keys
3. SSH
4. Finance
5. Personal
6. Back

pass> 1 (Password Manager)

Password Manager Options:
1. Add new Account
2. Change Password
3. Delete Account
4. List Accounts
5. View Account
6. Back

pass> 1  (Add new Account)

For: Facebook
Username: abc@11s
Password (leave empty for random): 

Generating random strong password...
Generated: XyZ1aBcD!EfGh2IjK
Account added successfully.

pass> 4  (List Accounts)

+-----------+----------+-----------------+
|   For     | Username | Last Changed    |
+-----------+----------+-----------------+
| Facebook  | abc@11s  | 2025-08-21      |
+-----------+----------+-----------------+

pass> 5  (View Account)

Username: abc@11s
Password: XyZ1aBcD!EfGh2IjK (Revealed temporarily; auto-hides after 10s)

pass> 2  (Change Password)

Username: abc@11s
New Password (leave empty for random): NewPass456!
Changed. Old password saved to history.

pass> 3  (Delete Account)

Username: abc@11s
Confirm? (y/n): y
Deleted. Recoverable for 7 days.

pass> 6 (Back to Categories)

pass> 2 (API Keys)

API Keys Options:
1. Add new API Key
2. Change Key
3. Delete API Key
4. List API Keys
5. View API Key
6. Back

pass> 1  (Add new API Key)

For: Project2
Service: GitHub
Key: ghp_abc123xyz
API key added successfully.

pass> 4  (List API Keys)

+----------+---------+-----------------+
|    For   | Service | Last Changed    |
-----------+---------+-----------------+
| Project2 | GitHub  | 2025-08-21      |
+----------+---------+-----------------+

pass> 5  (View API Key)

For: Project2
Service: GitHub
Key: ghp_abc123xyz (Revealed temporarily; auto-hides after 10s)

pass> 2  (Change Key)

Select: Project2
New Key (leave empty to keep): ghp_new456xyz
Changed. Old key saved to history.

pass> 3  (Delete API Key)

Select: Project2
Confirm? (y/n): y
Deleted. Recoverable for 7 days.

pass> 6 (Back to Categories)

pass> 3 (SSH)

SSH Options:
1. Add new SSH Entry
2. Change Path/Username
3. Delete SSH Entry
4. List SSH Entries
5. View SSH Entry
6. Back

pass> 1  (Add new SSH Entry)

Alias: prod-server
Username: ubuntu
Key Path: /home/user/.ssh/id_rsa_prod
SSH entry added successfully.

pass> 4  (List SSH Entries)

+-------------+----------+-----------------+
| Alias       | Username | Last Changed    |
+-------------+----------+-----------------+
| prod-server | ubuntu   | 2025-08-21      |
+-------------+----------+-----------------+

pass> 5  (View SSH Entry)

Select: prod-server
Username: ubuntu
Key Path: /home/user/.ssh/id_rsa_prod (Revealed temporarily; auto-hides after 10s)

pass> 2  (Change Path/Username)

Select: prod-server
New Username (leave empty to keep): newuser
New Key Path (leave empty to keep): /home/user/.ssh/id_rsa_new
Changed. Old details saved to history.

pass> 3  (Delete SSH Entry)

Select: prod-server
Confirm? (y/n): y
Deleted. Recoverable for 7 days.

pass> 6 (Back to Categories)

pass> 4 (Finance)

Finance Options:
1. Add new Finance Entry
2. Change Details
3. Delete Finance Entry
4. List Finance Entries
5. View Finance Entry
6. Back

pass> 1  (Add new Finance Entry)

Type (debit/credit/bank): debit
Cardholder: Irshad Hossain
Card Number: 1234-5678-9012-3456
Expiry (MM/YY): 12/27
Finance entry added successfully.

pass> 4  (List Finance Entries)

+--------+---------------+---------------------+-----------------+-------------+
| Type   | Cardholder    |      CardNumber     | Last Changed    | Expiry Warn |
+--------+---------------+---------------------+-----------------+-------------+
| debit  | Irshad Hossain| 1234-5678-9012-3456 | 2025-08-21      | 12/27       |
+--------+---------------+---------------------+-----------------+-------------+

pass> 5  (View Finance Entry)

Select: debit
last4: 3456
Cardholder: Irshad Hossain
Card Number: 1234-5678-9012-3456  (Revealed temporarily; auto-hides after 10s)
Expiry: 12/27

pass> 2  (Change Details)

Select: debit
last4: 3456
New Type (leave empty to keep): 
New Cardholder (leave empty to keep): 
New Card Number (leave empty to keep): 9876-5432-1098-7654
New Expiry (leave empty to keep): 01/28
Changed. Old details saved to history.

pass> 3  (Delete Finance Entry)

Select: debit
last4: 3456
Confirm? (y/n): y
Deleted. Recoverable for 7 days.

pass> 6 (Back to Categories)

pass> 5 (Personal)

Personal Options:
1. Add new Note
2. Change Note
3. Delete Note
4. List Notes
5. View Note
6. Back

pass> 1

Title: My NID
Content: 233 221 344
Personal note added successfully.

pass> 4  (List Notes)

+--------------------+-----------------+
| Title             | Last Changed     |
+--------------------+-----------------+
| My Secret Recipe  | 2025-08-21       |
+--------------------+-----------------+

pass> 5  (View Note)

Select: My Secret Recipe
Content: Mix flour, eggs, and magic. (Revealed temporarily; auto-hides after 10s)

pass> 2  (Change Note)

Select: My Secret Recipe
New Title (leave empty to keep): 
New Content (leave empty to keep): Mix flour, sugar, and magic.
Changed. Old note saved to history.

pass> 3  (Delete Note)

Select: My Secret Recipe
Confirm? (y/n): y
Deleted. Recoverable for 7 days.

pass> 6 (Back to Categories)

pass> 6 (Back to Main Menu)

```

### Settings Menu (Logged-In)

```
pass> 3

Settings:
1. Change Access key
2. Backup Database
3. Recover from Backup
4. Check Expiry Warnings
5. View Audit Logs
6. Password Policies
7. Session Timeout (current: 5 min)
8. Recover Deleted
9. Back

pass> 1

Current Access Key: ********
New: ********
Confirm: ********

Changed. Data re-encrypted.

pass> 4

Passwords older than 90 days: None (Lists if any, with change option).

pass> 5

Audit Logs:
- 2025-08-21 10:00: Successful login
- etc.

pass> 8

Deleted Items:
- Facebook (deleted 2025-08-21)
Recover? (y/n): y
Recovered.
```

### Edge Cases in Interactive Mode

- **Corruption**: On start, "Database corrupted! Recover from backup? (y/n)" – Selects from 3-day backups.
- **Session Expiry**: "Session expired. Re-login."
- **Large Lists**: Handles 100s efficiently with scrolling/pagination in UI.

## Developer Info

- **Developer**: Irshad Hossain, Student in the Software Engineering Department at UFTB.
- **Project**: Will developed as part of 1st year software engineering course.
