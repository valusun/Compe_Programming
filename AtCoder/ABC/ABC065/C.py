from math import factorial


def main():
    N, M = map(int, input().split())
    MOD = 10**9 + 7
    if abs(N - M) > 1:
        print(0)
        exit()
    if N == M:
        print(factorial(N) * factorial(M) * 2 % MOD)
    else:
        print(factorial(N) * factorial(M) % MOD)


if __name__ == "__main__":
    main()
