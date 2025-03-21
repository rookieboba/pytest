import pytest
import logging
from src.calculator import Calculator

# pytest fixture: 각 테스트 함수 실행 전 Calculator생성해서 자동으로 주입
@pytest.fixture
def calc():
    """각 테스트마다 새로운 Calculator 를 제공하고 테스트 후 정리"""
    calculator = Calculator()
    yield calculator  # ✅ 여기까지 실행되면 테스트 함수로 객체가 전달됨
    logging.info("🔹 Calculator 테스트 완료!")  # ✅ logging 사용

@pytest.mark.parametrize(
    "a, b, expected",  # 변수 이름 순서대로 unpack
    [
        (3, 5, 8),       # 3 + 5 → 예상 결과 8
        (0, 0, 0),       # 0 + 0 → 0
        (-1, -2, -3),    # -1 + (-2) → -3
        (10, -5, 5)      # 10 + (-5) → 5
    ]
)
def test_add(calc, a, b, expected):
    # expected 는 기대한 결과값 (예상값)
    assert calc.add(a, b) == expected

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6

def test_divide(calc):
    assert calc.divide(10, 2) == 5.0
    with pytest.raises(ValueError):  
        calc.divide(5, 0)
