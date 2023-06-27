def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] -= 1
    MOD = 998244353
    for i in range(N):
        for l, r in LR:
            if i + l < N:
                dp[i + l] += dp[i]
            if i + r + 1 < N:
                dp[i + r + 1] -= dp[i]
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
    print(dp[N - 1] % MOD)


if __name__ == "__main__":
    main()
