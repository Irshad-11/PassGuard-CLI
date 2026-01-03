import hashlib
import math
import string
from passguard.config import CLEAN_PUNCT

def sha(x: str) -> str:
    return hashlib.sha256(x.encode()).hexdigest()

def entropy(p: str) -> float:
    """Calculates password entropy in bits."""
    if not p: return 0
    pool = 0
    if any(x.islower() for x in p): pool += 26
    if any(x.isupper() for x in p): pool += 26
    if any(x.isdigit() for x in p): pool += 10
    if any(x in string.punctuation for x in p): pool += 32
    
    # Formula: $E = L \times \log_2(R)$ where L is length and R is pool size
    return len(p) * math.log2(pool) if pool > 0 else 0