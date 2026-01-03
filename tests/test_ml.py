from unittest.mock import patch, mock_open
from passguard.ml import analyze_corpus, gen_password

def test_analyze_corpus():
    mock_data = "ABC123abc!!!\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        weights = analyze_corpus()
        assert weights['upper'] >= 1
        assert weights['digit'] >= 1

def test_gen_password_complexity(temp_db):
    pw = gen_password(temp_db)
    assert len(pw) > 0
    # Check if history recorded it
    res = temp_db.execute("SELECT password FROM history").fetchone()
    assert res[0] == pw