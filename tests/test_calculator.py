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


def test_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0
    with pytest.raises(ValueError):  #raises 는 특정 예외(Exception) 발생 검증 기능
        calc.divide(5, 0)