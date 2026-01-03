import secrets
import string
from datetime import datetime

from passguard.crypto import entropy
from passguard.config import ML_FILE, CLEAN_PUNCT


def analyze_corpus():
    weights = {'upper': 2, 'lower': 4, 'digit': 2, 'punct': 2, 'len': 12}
    count = 0

    try:
        with open(ML_FILE) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                count += 1
                for c in line:
                    if c.isupper(): weights['upper'] += 1
                    elif c.islower(): weights['lower'] += 1
                    elif c.isdigit(): weights['digit'] += 1
                    elif c in string.punctuation: weights['punct'] += 1

        if count:
            for k in ['upper', 'lower', 'digit', 'punct']:
                weights[k] = max(1, int(weights[k] / count))
    except:
        pass

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

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("INSERT INTO history VALUES(?,?,?)", (pw, entropy(pw), ts))
    conn.commit()

    return pw
