def main():
    # Pythonはオーバーフローがないので単純計算でいける(桁が増えると処理時間がかかる)
    a, b, c, d, e, f = map(int, input().split())
    print((a * b * c - d * e * f) % 998244353)

    # 他言語のオーバーフロー考慮版
    MOD = 998244353
    x = ((a % MOD) * (b % MOD)) % MOD
    x = (x * (c % MOD)) % MOD
    y = ((d % MOD) * (e % MOD)) % MOD
    y = (y * (f % MOD)) % MOD
    print((x + MOD - y) % MOD)


if __name__ == "__main__":
    main()
