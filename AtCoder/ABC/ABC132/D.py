from math import comb


def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    for i in range(1, K + 1):
        r = comb(N - K + 1, i)
        b = comb(K - 1, i - 1)
        print(r * b % MOD)


if __name__ == "__main__":
    main()
