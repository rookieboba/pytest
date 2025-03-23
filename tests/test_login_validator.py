import pytest
from src.login_validator import LoginHistoryValidator

validator = LoginHistoryValidator()

# ---------- Username 테스트 ----------

@pytest.mark.parametrize("username, expected", [
    ("validuser", "Valid"),
    ("ab", "username invalid: too short"),
    ("averyverylongusername", "username invalid: too long"),
    ("john doe", "username invalid: contains space"),
], ids=[
    "valid username",
    "username too short",
    "username too long",
    "username contains space"
])
def test_username_validation(username, expected):
    logs = [{
        "username": username,
        "gender": "M",
        "ip": "192.168.0.1"
    }]
    assert validator.validate_logins(logs)[0] == expected

# ---------- Gender 테스트 ----------

@pytest.mark.parametrize("gender, expected", [
    ("M", "Valid"),
    ("W", "Valid"),
    ("X", "gender invalid: must be 'M' or 'W'"),
    ("", "gender invalid: must be 'M' or 'W'"),
], ids=[
    "gender M",
    "gender W",
    "invalid gender X",
    "empty gender"
])
def test_gender_validation(gender, expected):
    logs = [{
        "username": "tester",
        "gender": gender,
        "ip": "192.168.0.1"
    }]
    assert validator.validate_logins(logs)[0] == expected

# ---------- IP 테스트 ----------

@pytest.mark.parametrize("ip, expected", [
    ("192.168.0.1", "Valid"),
    ("999.999.999.999", "ip invalid: not a valid IPv4 address"),
    ("256.0.0.1", "ip invalid: not a valid IPv4 address"),
    ("abc.def.ghi.jkl", "ip invalid: not a valid IPv4 address"),
], ids=[
    "valid ip",
    "ip all segments invalid",
    "ip segment overflow",
    "ip string junk"
])
def test_ip_validation(ip, expected):
    logs = [{
        "username": "tester",
        "gender": "M",
        "ip": ip
    }]
    assert validator.validate_logins(logs)[0] == expected

# ---------- 필드 누락 테스트 ----------

@pytest.mark.parametrize("log, expected", [
    ({"gender": "M", "ip": "192.168.0.1"}, "missing field: username"),
    ({"username": "tester", "ip": "192.168.0.1"}, "missing field: gender"),
    ({"username": "tester", "gender": "M"}, "missing field: ip"),
], ids=[
    "missing username",
    "missing gender",
    "missing ip"
])
def test_missing_field(log, expected):
    assert validator.validate_logins([log])[0] == expected

# ---------- 혼합 케이스 테스트 ----------

def test_mixed_valid_invalid():
    logs = [
        {
            "username": "user1",
            "gender": "M",
            "ip": "192.168.0.1"
        },
        {
            "username": "bad user",
            "gender": "M",
            "ip": "192.168.0.2"
        },
        {
            "username": "user2",
            "gender": "X",
            "ip": "192.168.0.3"
        },
        {
            "username": "user3",
            "gender": "M",
            "ip": "256.0.0.1"
        },
    ]

    expected = [
        "Valid",
        "username invalid: contains space",
        "gender invalid: must be 'M' or 'W'",
        "ip invalid: not a valid IPv4 address"
    ]

    assert validator.validate_logins(logs) == expected
