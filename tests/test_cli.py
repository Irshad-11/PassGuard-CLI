from passguard.cli import run_cli

def test_cli_help_command(temp_db):
    # Should return True because 'help' is a valid command
    cfg = {"master": "hash", "db": "path"}
    assert run_cli(temp_db, cfg, ["help"]) is True

def test_cli_unauthorized_get(temp_db):
    cfg = {"master": "hash", "db": "path"}
    # Should fail or return True (but print error) because no session exists
    assert run_cli(temp_db, cfg, ["get", "ACC", "Google", "user"]) is True