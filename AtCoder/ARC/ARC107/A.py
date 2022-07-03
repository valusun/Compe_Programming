def CalcSum(N):
    return N * (N + 1) // 2


def main():
    a, b, c = map(int, input().split())
    MOD = 998244353
    print(CalcSum(a) * CalcSum(b) * CalcSum(c) % MOD)


if __name__ == "__main__":
    main()
