def GeneratePrimeNumbers(n: int):
    """エラトステネスの篩を用いて素数のリストを生成する

    Args:
        n (int): 上限

    Returns:
        list[int]: 引数までの素数
    """
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
    N = int(input())
    ans = 0
    primes = GeneratePrimeNumbers(10**6)
    for q in range(2, 10**6 + 1):
        if not primes[q]:
            continue
        for p in range(2, q):
            if not primes[p]:
                continue
            if p * q**3 > N:
                break
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
