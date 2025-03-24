# tests/test_UserSignup.py

import pytest
from src.UserSignup import UserSignup

signup = UserSignup()

# ---------- 정상 케이스 ----------
def test_user_signup_success():
    user = {
        "username": "sungbin",
        "password": "secure123",
        "email": "sungbin@example.com",
        "gender": "M"
    }
    assert signup.signup(user) == "Signup Successful"

# ---------- 필드 누락 ----------
@pytest.mark.parametrize("user, expected", [
    ({"password": "123456", "email": "a@a.com", "gender": "M"}, "missing field: username"),
    ({"username": "abc", "email": "a@a.com", "gender": "M"}, "missing field: password"),
    ({"username": "abc", "password": "123456", "gender": "M"}, "missing field: email"),
    ({"username": "abc", "password": "123456", "email": "a@a.com"}, "missing field: gender"),
], ids=["no username", "no password", "no email", "no gender"])
def test_missing_fields(user, expected):
    assert signup.signup(user) == expected

# ---------- username 유효성 ----------
@pytest.mark.parametrize("username, expected", [
    ("ab", "username invalid"),
    ("this username", "username invalid"),
    ("x" * 25, "username invalid"),
], ids=["too short", "contains space", "too long"])
def test_invalid_username(username, expected):
    user = {
        "username": username,
        "password": "123456",
        "email": "a@a.com",
        "gender": "M"
    }
    assert signup.signup(user) == expected

# ---------- password 유효성 ----------
@pytest.mark.parametrize("password, expected", [
    ("123", "password invalid"),
    (123456, "password invalid"),
], ids=["too short", "not a string"])
def test_invalid_password(password, expected):
    user = {
        "username": "user01",
        "password": password,
        "email": "a@a.com",
        "gender": "M"
    }
    assert signup.signup(user) == expected

# ---------- email 유효성 ----------
@pytest.mark.parametrize("email, expected", [
    ("userexample.com", "email invalid"),
    ("user@examplecom", "email invalid"),
    (12345, "email invalid"),
], ids=["no @", "no dot", "not a string"])
def test_invalid_email(email, expected):
    user = {
        "username": "user01",
        "password": "123456",
        "email": email,
        "gender": "M"
    }
    assert signup.signup(user) == expected

# ---------- gender 유효성 ----------
@pytest.mark.parametrize("gender, expected", [
    ("X", "gender invalid"),
    ("", "gender invalid"),
    (None, "gender invalid"),
], ids=["invalid value", "empty", "none"])
def test_invalid_gender(gender, expected):
    user = {
        "username": "user01",
        "password": "123456",
        "email": "a@a.com",
        "gender": gender
    }
    assert signup.signup(user) == expected
