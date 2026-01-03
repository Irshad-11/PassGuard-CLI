
<img src="https://raw.githubusercontent.com/Irshad-11/Documents/refs/heads/main/passguardCLI.png" alt="Banner">

<h1 align="center">PassGuard-CLI <img src="https://img.shields.io/badge/Version-1.0.0-blueviolet" alt="Version Badge"></h1>
<p align="center">
<img src="https://img.shields.io/badge/UNIX%20style-437057" alt="UNIX Style">
<img src="https://img.shields.io/badge/Scriptable%20CLI-1C352D" alt="Scriptable CLI">
<img src="https://img.shields.io/badge/Interactive%20TUI-064232" alt="Interactive TUI">
<img src="https://img.shields.io/badge/Security-SHA--256-red" alt="Security Badge">
</p>

## What is PassGuard-CLI?

PassGuard-CLI is a professional, modular, terminal-based password manager designed for developers who value speed and local security. It allows you to store and manage Account credentials, API keys, SSH entries, and Personal notes in a secure, SQLite-backed vault.

What sets PassGuard apart is its **Intelligence Engine**: it includes an ML-based generator that learns "Strong Style" patterns from a local corpus (`password.txt`), ensuring your generated passwords aren't just random, but follow high-quality complexity standards.

## How it Works

1. **Zero-Knowledge local storage**: All data is stored in a local `.db` file. Your Master Access Key is never stored in plain text; it is protected using **SHA-256** hashing.
2. **Session-Based Security**: Once you login, a secure session is created that expires automatically after **300 seconds (5 minutes)** to prevent unauthorized access if your terminal is left open.
3. **Dual-Mode Interface**:
* **CLI Mode**: Fast, one-liner commands for automation and scripting.
* **TUI Mode**: A rich, menu-driven terminal interface for exploratory management.


4. **Health Monitoring**: The system automatically flags weak passwords based on real-time **Entropy Calculations** ().

## The Tech Stack

PassGuard-CLI is built with a modern, modular Python stack to ensure performance and portability:

* **Language**: Python 3.10+
* **Database**: SQLite3 (Local, serverless relational storage)
* **CLI/TUI Framework**: Custom modular engine with `Colorama` for terminal styling.
* **Cryptography**: `hashlib` (SHA-256) and `secrets` (Cryptographically secure random numbers).
* **DevOps**: Pytest (Automated testing) and GitHub Actions (CI/CD Build Pipeline).

> [!TIP]
> **Architecture Info**: For detailed logic flows, DB schemas, and ML explanation, please refer to our **[Documentation Section](https://www.google.com/search?q=docs/ARCHITECTURE.md)**.

---

## 🚀 Installation (Single Executable)

PassGuard-CLI is distributed as a **single standalone executable**. You do not need to install Python or any dependencies to run it.

1. Go to the **[Releases](https://www.google.com/search?q=https://github.com/Irshad-11/PassGuard-CLI/releases)** page.
2. Download the `passguard.exe` for your operating system.
3. (Optional) Add the folder containing `passguard.exe` to your System PATH to run it from any terminal.

### For Developers (Run from Source)

```bash
git clone https://github.com/Irshad-11/PassGuard-CLI.git
cd PassGuard-CLI
pip install -r requirements.txt
python -m passguard.app

```

---

## 🛠️ Usage Quick-Start

### 1. Initialize & Login

On your first run, the system will guide you through setting up your Master Access Key.

```bash
# Login to start a session
passguard login MySecretKey123

```

### 2. Intelligent Password Generation

Generates a password based on your `password.txt` style and copies it to the clipboard.

```bash
passguard gen -copy

```

### 3. Quick Entry Management

Add and retrieve secrets without entering the TUI.

```bash
# Add a new account
passguard add ACC Google myname@gmail.com MyPassword123!

# Get secret to clipboard
passguard get ACC Google myname@gmail.com -copy

```

### 4. Interactive TUI

Simply run the application without arguments to enter the full Interactive Mode:

```bash
passguard

```

---

## 📚 Detailed Documentation

* **[Setup & Troubleshooting](https://www.google.com/search?q=docs/SETUP.md)**
* **[Full Command Reference](https://www.google.com/search?q=docs/COMMANDS.md)**
* **[Security & Entropy Math](https://www.google.com/search?q=docs/SECURITY.md)**

---

## 👨‍💻 Credits & Developer Info

* **Lead Developer**: **Irshad Hossain**, Software Engineering Student at UFTB.
* **Project Purpose**: Developed as a professional-grade security tool for the 1st-year Software Engineering curriculum.
* **Contact**: [GitHub/Irshad-11](https://www.google.com/search?q=https://github.com/Irshad-11)

---

<p align="center">Made with ❤️ for the Terminal Community</p>
