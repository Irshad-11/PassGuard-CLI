# 🔄 Data Flow: User → Database

## 📌 System Flow

1. **User Inputs Master Key**  
   The user provides a master key at the CLI/TUI prompt.

2. **Authentication (`auth.py`)**  
   - The input is **hashed** using secure algorithms.  
   - The hash is compared against the stored reference in `config.json`.  
   - If the comparison succeeds, authentication is valid.

3. **Database Connection (`db.py`)**  
   - A secure SQLite connection is opened.  
   - Encrypted fields are prepared for read/write operations.

4. **Interface Rendering (`menus.py`)**  
   - The **TUI** (Text User Interface) is rendered.  
   - Interactive menus allow the user to navigate commands.

5. **Machine Learning (`ml.py`)**  
   - Reads `password.txt` corpus.  
   - Sets **generation weights** for password suggestions.  
   - Improves entropy and mimics strong password styles.

---

## 🔐 Security Formula (Entropy)

We calculate password strength using:



\[
E = L \times \log_2(R)
\]



Where:  
- \(L\): Length of the password  
- \(R\): Character pool size (e.g., 94 for full ASCII set)

---

## 📊 Example

For a password of length \(L = 12\) with \(R = 94\):



\[
E = 12 \times \log_2(94) \approx 78.8 \ \text{bits}
\]



This ensures strong resistance against brute-force attacks.
