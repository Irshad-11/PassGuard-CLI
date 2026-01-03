from passguard.crypto import sha, entropy

def test_sha():
    assert sha("1122") == "808643809930f2526c2f7413661109a1a9e33d26240217be543e096f30a43064"

def test_entropy():
    assert entropy("abc") > 0
    assert entropy("") == 0