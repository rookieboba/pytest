# [문제]
# N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다. 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.

# 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
# 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
# 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
# 지붕의 가장자리는 땅에 닿아야 한다.
# 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
# 그림 1은 창고를 옆에서 본 모습을 그린 것이다. 이 그림에서 굵은 선으로 표시된 부분이 지붕에 해당되고, 지붕과 땅으로 둘러싸인 다각형이 창고를 옆에서 본 모습이다. 이 다각형을 창고 다각형이라고 하자.

# 창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다. 그림 1에서 창고 다각형의 면적은 98 ㎡이고, 이 경우가 가장 작은 창고 다각형이다.

# 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.

# [입력]
# 첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. N은 1 이상 1,000 이하이다. 그 다음 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다. L과 H는 둘 다 1 이상 1,000 이하이다.

# [출력]
# 첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력한다.


# Link: https://www.acmicpc.net/problem/2304

# src/warehouse_area.py

def calculate_warehouse_area(pillars):
    pillars.sort()

    warehouse = [0] * 1001
    for l, h in pillars:
        warehouse[l] = h

    max_h = max(warehouse)
    max_idx = warehouse.index(max_h)

    area = 0

    # 왼쪽 → max_idx
    left_max = 0
    for i in range(0, max_idx + 1):
        if warehouse[i] > left_max:
            left_max = warehouse[i]
        area += left_max

    # 오른쪽 → max_idx
    right_max = 0
    for i in range(1000, max_idx, -1):
        if warehouse[i] > right_max:
            right_max = warehouse[i]
        area += right_max

    return area


# 초기 동작 확인용 (테스트 없이 단독 실행 시)
if __name__ == "__main__":
    example_input = [
        (2, 4), (11, 4), (15, 8),
        (4, 6), (5, 3), (8, 10), (13, 6)
    ]
    result = calculate_warehouse_area(example_input)
    print(f"면적: {result}")  # 출력: 면적: 98
