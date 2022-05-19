from math import sqrt


def PrimeFactorSplit(num):
    """受け取った引数の素因数を返す

    Args:
        num (int): 数値

    Returns:
        list[int]: 引数の素因数
    """

    prime_factors = []
    for i in range(2, int(sqrt(num)) + 1):
        while num % i == 0:
            prime_factors.append(i)
            num //= i
    if num != 1:
        prime_factors.append(num)
    return prime_factors


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    prime_factors = set()
    for i in A:
        prime_factors |= set(PrimeFactorSplit(i))

    not_used = set()
    for p in prime_factors:
        for q in range(p, M + 1, p):
            not_used.add(q)

    ans = set(list(i for i in range(1, M + 1))) - not_used
    print(len(ans), *sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
