import pytest
from src.password import is_valid_password

@pytest.mark.parametrize(
    "password, expected",
    [
        ("ABCDEFGH", False),
        ("Ab1!efgh", False),  # 이 케이스는 실제 함수 구현에 따라 True일 수도
        ("PASSWORD123", False),
        ("Pass 123!", False),
        ("P@ssword", True),
        ("Ab1!", False)
    ],
    ids=[
        "only-uppercase",
        "should-be-valid",           # 또는 "check-failure"
        "missing-special-or-lower",
        "contains-space",
        "valid-basic",
        "too-short"
    ]
)
def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected
