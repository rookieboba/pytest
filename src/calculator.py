class Calculator:
    """간단한 사칙연산 계산기"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return a / b
