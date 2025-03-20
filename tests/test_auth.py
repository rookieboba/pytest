import pytest
from auth import AuthService

@pytest.fixture
def auth_service():
    return AuthService()

def test_login_success(auth_service):
    """정상적인 로그인 테스트"""
    assert auth_service.login("user1", "password123") == "로그인 성공"

def test_login_failure(auth_service):
    """잘못된 비밀번호로 로그인 시도"""
    assert auth_service.login("user1", "wrongpassword") == "로그인 실패"

def test_login_non_existent_user(auth_service):
    """존재하지 않는 사용자로 로그인 시도"""
    assert auth_service.login("unknown", "password") == "로그인 실패"
