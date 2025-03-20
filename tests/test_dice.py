import random
import pytest
from src.dice import Dice

@pytest.fixture
def dice():
    return Dice()

def test_roll(dice):
    """주사위 굴리기 테스트"""
    result = dice.roll()
    assert 1 <= result <= 6

def test_roll_multiple(dice):
    """여러 개의 주사위 굴리기 테스트"""
    results = dice.roll_multiple(3)
    assert len(results) == 3
    for result in results:
        assert 1 <= result <= 6
