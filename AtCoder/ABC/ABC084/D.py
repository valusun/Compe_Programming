from itertools import accumulate


def GeneratePrimes(n: int) -> list[int]:
    """インデックス番号が素数の箇所を1としたリストを生成する"""

    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(n**0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes


def main():
    N = 10**5 + 1
    Q = int(input())
    primes = GeneratePrimes(N)
    similar_flag = [0] * N
    for i in range(N - 1):
        if primes[i] and primes[(i + 1) // 2]:
            similar_flag[i] += 1
    cusum = list(accumulate(similar_flag))
    for _ in range(Q):
        l, r = map(int, input().split())
        print(cusum[r] - cusum[l - 1])


if __name__ == "__main__":
    main()
