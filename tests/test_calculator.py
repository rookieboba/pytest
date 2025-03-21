'''
✅ 요구 사항
📌 test_calculator.py에서 다음 사항을 검증하는 pytest 테스트 코드를 작성하라.

add(3, 5)의 결과가 8인지 검증
subtract(10, 4)의 결과가 6인지 검증
multiply(2, 3)의 결과가 6인지 검증
divide(10, 2)의 결과가 5.0인지 검증
divide(5, 0)을 실행하면 ValueError가 발생하는지 검증'
'''

import pytest
from src.calculator import Calculator

# pytest fixture: 각 테스트 함수 실행 전 Calculator생성해서 자동으로 주입
@pytest.calculator.fixture
def calc():
    """각 테스트마다 새로운 Calculator 를 제공하고 테스트 후 정리"""
    calculator = Calculator()
    yield calculator  # ✅ 여기까지 실행되면 테스트 함수로 객체가 전달됨
    print("\n🔹 Calculator 테스트 완료!")  # ✅ cleanup 코드 (테스트 후 실행)

def test_add(calc):
    assert calc.add(3, 5) == 8

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6

def test_divide(calc):
    assert calc.divide(10, 2) == 5.0
    with pytest.raises(ValueError):  
        calc.divide(5, 0)
