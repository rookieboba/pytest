import random

class Dice:
    """주사위를 굴리는 클래스"""

    def __init__(self, sides=6):
        """기본적으로 6면체 주사위"""
        if sides < 2:
            raise ValueError("주사위는 최소 2면 이상이어야 합니다.")
        self.sides = sides

    def roll(self):
        """주사위를 굴려서 1~sides 사이의 난수를 반환"""
        return random.randint(1, self.sides)

    def roll_multiple(self, num):
        """여러 개의 주사위를 굴려서 결과 리스트 반환"""
        if num < 1:
            raise ValueError("1개 이상의 주사위를 굴려야 합니다.")
        return [self.roll() for _ in range(num)]
