import pytest
from src.password import is_valid_password

@pytest.mark.parametrize( # 테스트 함수에 여러 입력값을 전달해, 자동으로 반복 실행할 수 있게 해주는 기능
    "password, expected", #expected는 예상되는 결과값
    [
        ("ABCDEFGH", False),
        ("Ab1!efgh", False),
        ("PASSWORD123", False),
        ("Pass 123!", False),
        ("P@ssword", True),
        ("Ab1!", False)
    ]
)

def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected