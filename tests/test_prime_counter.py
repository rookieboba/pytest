# tests/test_prime_counter.py

import pytest
from src.prime_counter import solution

@pytest.mark.parametrize("n, expected", [
    (10, 4),   # [2, 3, 5, 7]
    (5, 3),    # [2, 3, 5]
    (2, 1),    # [2]
    (1, 0),    # 소수 없음
    (20, 8),   # [2, 3, 5, 7, 11, 13, 17, 19]
    (100, 25),
], ids=["10까지", "5까지", "2까지", "1까지", "20까지", "100까지"])
def test_solution(n, expected):
    assert solution(n) == expected
