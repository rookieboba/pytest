import pytest
from src.login_validator import LoginHistoryValidator

@pytest.mark.parametrize(
    "logs, expected",
    [
        # 정상 케이스
        ([{
            "username": "tester01",
            "gender": "M",
            "ip": "192.168.0.1"
        }],
        ["Valid"]),

        # 필드 누락 케이스
        ([{
            "gender": "M",
            "ip": "192.168.0.1"
        }],
        ["missing field: username"]),

        ([{
            "username": "tester01",
            "ip": "192.168.0.1"
        }],
        ["missing field: gender"]),

        ([{
            "username": "tester01",
            "gender": "M"
        }],
        ["missing field: ip"]),

        # username 문제
        ([{
            "username": "john doe",
            "gender": "W",
            "ip": "192.168.0.1"
        }],
        ["username invalid: contains space"]),

        ([{
            "username": "ab",
            "gender": "M",
            "ip": "192.168.0.1"
        }],
        ["username invalid: too short"]),

        ([{
            "username": "averyverylongusername",
            "gender": "W",
            "ip": "192.168.0.1"
        }],
        ["username invalid: too long"]),

        # gender 문제
        ([{
            "username": "tester",
            "gender": "X",
            "ip": "192.168.0.1"
        }],
        ["gender invalid: must be 'M' or 'W'"]),

        # ip 문제
        ([{
            "username": "tester",
            "gender": "M",
            "ip": "999.999.999.999"
        }],
        ["ip invalid: not a valid IPv4 address"]),

        # 혼합 케이스
        ([
            {
                "username": "validuser",
                "gender": "M",
                "ip": "10.0.0.1"
            },
            {
                "username": "bad user",
                "gender": "W",
                "ip": "10.0.0.2"
            },
            {
                "username": "tester",
                "gender": "Z",
                "ip": "10.0.0.3"
            },
            {
                "username": "user3",
                "gender": "M",
                "ip": "invalid.ip"
            }
        ],
        ["Valid", "username invalid: contains space", "gender invalid: must be 'M' or 'W'", "ip invalid: not a valid IPv4 address"]),
    ],
    ids=[
        "valid input",
        "missing username",
        "missing gender",
        "missing ip",
        "username contains space",
        "username too short",
        "username too long",
        "invalid gender value",
        "invalid ip address",
        "mixed: valid + multiple errors"
    ]
)
def test_validate_logins(logs, expected):
    validator = LoginHistoryValidator()
    assert validator.validate_logins(logs) == expected
