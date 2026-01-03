
<img src="https://raw.githubusercontent.com/Irshad-11/Documents/refs/heads/main/passguardCLI.png" alt="Banner">

<h1 align="center">PassGuard-CLI <img src="https://img.shields.io/badge/Beta-v1.0.2-blueviolet" alt="Version Badge"></h1>
<p align="center">
<img src="https://img.shields.io/badge/Machine%20Learning-437057" alt="UNIX Style">
<img src="https://img.shields.io/badge/Scriptable%20CLI-1C352D" alt="Scriptable CLI">
<img src="https://img.shields.io/badge/Interactive%20TUI-064232" alt="Interactive TUI">
<img src="https://img.shields.io/badge/Security-SHA--256-red" alt="Security Badge">
</p>

## What is PassGuard-CLI?

PassGuard-CLI is a professional, modular, terminal-based password manager designed for developers who value speed and local security. It allows you to store and manage Account credentials, API keys, SSH entries, and Personal notes in a secure, SQLite-backed vault. It offers a UNIX-style CLI and a TUI, along with features like rate-limited logins and audit logs.

## How it Works

1. **Zero-Knowledge local storage**: All data is stored in a local `.db` file. Your Master Access Key is never stored in plain text; it is protected using **SHA-256** hashing.
2. **Session-Based Security**: Once you login, a secure session is created that expires automatically after **300 seconds (5 minutes)** to prevent unauthorized access if your terminal is left open.
3. **Dual-Mode Interface**:
* **CLI Mode**: Fast, one-liner commands for automation and scripting.
* **TUI Mode**: A rich, menu-driven terminal interface for exploratory management.


4. **Password Monitoring**: The system automatically flags weak passwords based on real-time **Entropy Calculations** ().

## The Tech Stack

PassGuard-CLI is built with a modern, modular Python stack to ensure performance and portability:

* **Language**: Python 3.10+
* **Database**: SQLite3 (Local, serverless relational storage)
* **CLI/TUI Framework**: Custom modular engine with `Colorama` for terminal styling.
* **Cryptography**: `hashlib` (SHA-256) and `secrets` (Cryptographically secure random numbers).
* **DevOps**: Pytest (Automated testing) and GitHub Actions (CI/CD Build Pipeline).

> [!TIP]
> **Architecture Info**: For detailed logic flows, DB schemas, and ML explanation, please refer to our **[Documentation Section](https://github.com/Irshad-11/PassGuard-CLI/tree/main/docs/ARCHITECTURE.md)**.

---

## 🚀 Installation (Single Executable)

PassGuard-CLI is distributed as a **single standalone executable**. You do not need to install Python or any dependencies to run it.

### For Developers (Run from Source)

```bash
git clone https://github.com/Irshad-11/PassGuard-CLI.git
cd PassGuard-CLI
pip install -r requirements.txt
python -m passguard.app

```
---

## For General Users (Run exe - Windows only)

### Step 1: Download & Setup
- Download the latest **[Releases](https://github.com/Irshad-11/PassGuard-CLI/releases)** containing the `pass.exe` file.
- Navigate to the folder where it is downloaded.
> [!IMPORTANT]
> **Vault Security**: For better security, move `pass.exe` to a personal or separate folder. This folder is your sensitive vault, so avoid keeping it in Downloads.

## Step 2: Add Pass to Windows PATH
- Copy the folder path where `pass.exe` is located.
- Open **Windows Search** → type **Edit Environmental Variables** → open it.
- Click **New** under the **Path** section and paste your folder path → Save.
> [!TIP]
> **Quick Access**: Once added to PATH, you can run `pass` from any CMD window without navigating to its folder.

## Step 3: Run PassGuard
- Open **CMD** and type `pass`.
- It will open the terminal-based TUI and ask for your **DB Path**:
  - Paste the folder path where `pass.exe` is located (completely safe).
- It will then ask for an **Access Key**:
  - Enter a 4-digit number for a quick and easy memorable key.
> [!CAUTION]
> **Access Key Advice**: Use a number that is easy to remember but not obvious, to balance convenience and security.

🎉 **Ollah! You are ready to go.**  
You will see the PassGuard homepage:

![PassGuard Homepage](https://raw.githubusercontent.com/Irshad-11/Documents/1643c7f7e409eaa45d59ed9023f8ab0c64d1d157/download.png)

> [!NOTE]
> **CMD Usage**: You can access PassGuard anytime from CMD by typing `pass` or `pass <argument>`.  
> Example commands: `pass add`, `pass login <key>`.


## 🛠️ Usage Quick-Start

### 1. Initialize & Login

On your first run, the system will guide you through setting up your Master Access Key.

```bash
# Login to start a session
pass login MySecretKey123

```

### 2. Strong Password Generation

Generates a password based on your `password.txt` style and copies it to the clipboard.

```bash
pass gen -copy

```

### 3. Quick Entry Management

Add and retrieve secrets without entering the TUI.

```bash
# Add a new account
pass add acc Google myname@gmail.com MyPassword123!

# Get secret to clipboard
pass get acc Google myname@gmail.com
pass get acc Google myname@gmail.com -copy
acc -> Account
api -> API
ssh -> SSH
note -> Personal Note

```

### 4. Interactive TUI

Simply run the application without arguments to enter the full Interactive Mode:

```bash
pass

```

---

## 📚 Detailed Documentation

* **[Setup & Troubleshooting](https://github.com/Irshad-11/PassGuard-CLI/tree/main/docs/SETUP.md)**
* **[Full Command Reference](https://github.com/Irshad-11/PassGuard-CLI/tree/main/docs/COMMANDS.md)**
* **[Security & Entropy Math](https://github.com/Irshad-11/PassGuard-CLI/tree/main/docs/SECURITY.md)**

---

## 👨‍💻 Credits & Developer Info

* **Lead Developer**: **Irshad Hossain**, Software Engineering Student at UFTB.
* **Project Purpose**: Developed as a professional-grade security tool for the 1st-year Software Engineering curriculum.
* **Contact**: [GitHub/Irshad-11](https://www.google.com/search?q=https://github.com/Irshad-11)

---

<p align="center">Made with ❤️ for the Terminal Community</p>
