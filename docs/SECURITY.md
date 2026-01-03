# 🔐 Cryptographic Standards

## Entropy Calculation

We calculate password strength using the following formula:



\[
E = L \times \log_2(R)
\]



Where:

- \(L\): Length of the password  
- \(R\): Character pool size (e.g., 94 for all standard ASCII)

---

### 📊 Example
For a password of length \(L = 12\) using the full ASCII set (\(R = 94\)):



\[
E = 12 \times \log_2(94) \approx 78.8 \ \text{bits}
\]



This means the password has approximately **78 bits of entropy**, which is considered strong against brute-force attacks.
