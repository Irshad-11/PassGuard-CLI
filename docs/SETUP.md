
# 🛠️ Installation & Setup Guide

This guide provides step-by-step instructions to get **PassGuard-CLI** running on your machine, whether you are a user or a developer.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher**: [Download here](https://www.python.org/downloads/)  
- **Pip**: Python package manager (usually included with Python)  
- **Git**: To clone and manage the repository  

---

## 🏗️ 1. Local Development Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/pass-guard.git
cd pass-guard
```

### Step 2: Create a Virtual Environment
It is highly recommended to use a virtual environment to avoid dependency conflicts.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 2. Initializing the Vault

Run the application for the first time to start the interactive setup wizard:

```bash
python -m passguard.app
```

During setup, you will be asked for:

- **Database Path**: The folder where `pass_guard.db` will be stored.  
- **Master Access Key**: Your primary key. Do not lose it. It is hashed using **SHA-256** before storage.  

---

## 🧪 3. Running Automated Tests

To ensure everything is installed correctly, run the test suite:

```bash
# Install pytest if not present
pip install pytest

# Run all tests
pytest tests/
```

---

## 📦 4. Building the Executable (.exe)

If you want to create a standalone file that doesn't require Python to run:

### Windows Build
```bash
pip install pyinstaller
build_local.bat
```

### Manual Build Command
```bash
pyinstaller --onefile --name passguard passguard/app.py
```

The output will be located in the **`dist/`** folder.
