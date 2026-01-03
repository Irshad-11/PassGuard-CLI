import hashlib
import math
import string

def sha(x: str) -> str:
    return hashlib.sha256(x.encode()).hexdigest()


def entropy(p: str) -> float:
    pool = 0
    if any(c.islower() for c in p): pool += 26
    if any(c.isupper() for c in p): pool += 26
    if any(c.isdigit() for c in p): pool += 10
    if any(c in string.punctuation for c in p): pool += 32
    return len(p) * math.log2(pool) if pool else 0
