# src/prime_counter.py

def solution(n: int) -> int:
    """1부터 n까지 범위에서 소수의 개수를 반환하는 함수"""
    if n < 2:
        return 0
#0부터 n까지의 숫자에 대해 전부 소수(True)라고 가정
    is_prime = [True] * (n + 1)

#0 과 1 은 소수가 아님
    is_prime[0] = is_prime[1] = False

# 2부터 √n 까지만 검사하면 충분함
# 시간 최적화를 위한 에라토스테네스의 체 원리
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return sum(is_prime)


# 실행용 테스트
if __name__ == "__main__":
    print("n=10 ➜", solution(10))  # 4
    print("n=5 ➜", solution(5))    # 3
