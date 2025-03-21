# tests/test_validate.py

import pytest
from src.validate import UserValidator

@pytest.mark.parametrize("users, expected", [
    (
        [{
            "username": "alice", 
            "age": "25", 
            "email": "alice@mail.com"
        }],
        ["Valid"]
    ),
    (
        [{
            "username": "b ob", 
            "age": "abc", 
            "email": "bob[at]mail.com"
        }],
        ["age invalid"]
    ),
    (
        [{
            "username": "cj", 
            "age": "18", 
            "email": "cj@mail.com"
        }],
        ["username invalid"]
    ),
    (
        [{
            "username": "daniel123", 
            "age": "200", 
            "email": "daniel@example.com"
        }],
        ["age invalid"]
    ),
    (
        [{
            "username": "noemail", 
            "age": "30"
        }],
        ["missing field"]
    ),
    (
        [
            {"username": "okman", "age": "40", "email": "ok@man.com"},
            {"username": "bad man", "age": "30", "email": "badman.com"}
        ],
        ["Valid", "username invalid"]
    )
], ids=[
    "valid_user",
    "invalid_age_format",
    "username_too_short",
    "age_out_of_range",
    "missing_email",
    "valid_and_invalid_mixed"
])
def test_validate_users(users, expected):
    validator = UserValidator()
    assert validator.validate_users(users) == expected


