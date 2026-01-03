import secrets
import string
from passguard.config import ML_FILE, CLEAN_PUNCT
from passguard.crypto import entropy

def analyze_corpus():
    weights = {'upper': 2, 'lower': 4, 'digit': 2, 'punct': 2, 'len': 12}
    count = 0
    try:
        with open(ML_FILE, "r") as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
            for line in lines:
                count += 1
                for char in line:
                    if char.isupper(): weights['upper'] += 1
                    elif char.islower(): weights['lower'] += 1
                    elif char.isdigit(): weights['digit'] += 1
                    elif char in string.punctuation: weights['punct'] += 1
        if count > 0:
            for k in ['upper', 'lower', 'digit', 'punct']:
                weights[k] = max(1, int(weights[k] / count))
    except: pass
    return weights

def gen_password(conn):
    w = analyze_corpus()
    pool = (
        [secrets.choice(string.ascii_uppercase) for _ in range(w['upper'])] +
        [secrets.choice(string.ascii_lowercase) for _ in range(w['lower'])] +
        [secrets.choice(string.digits) for _ in range(w['digit'])] +
        [secrets.choice(CLEAN_PUNCT) for _ in range(w['punct'])]
    )
    secrets.SystemRandom().shuffle(pool)
    pw = "".join(pool[:20])
    
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("INSERT INTO history VALUES(?,?,?)", (pw, entropy(pw), now))
    conn.commit()
    return pw