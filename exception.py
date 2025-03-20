import pytest

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None  # 테스트할 값

def test_divide():
    """ZeroDivisionError 예외 발생 여부 테스트"""
    assert divide(10, 2) == 5  # 정상 동작 확인
    assert divide(10, 0) is None  # 0으로 나눌 경우 None 반환 확인
