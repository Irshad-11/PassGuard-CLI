from passguard.crypto import entropy
from passguard.ml import analyze_corpus

def check_weak(conn, s, u, p):
    reason = None
    ent = entropy(p)
    if len(p) < 8: reason = "Too Short"
    elif ent < 40: reason = "Low Entropy"
    
    w = analyze_corpus()
    if len(p) < w['len'] - 2: reason = "Style Weakness"

    if reason:
        conn.execute("INSERT INTO warnings VALUES(?,?,?,?)", (s, u, reason, ent))
        conn.commit()