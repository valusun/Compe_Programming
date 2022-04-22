def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K):
            for k in range(1, M + 1):
                if j + k > K:
                    continue
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= MOD
    ans = 0
    for i in dp[N]:
        ans = (ans + i) % MOD
    print(ans)


if __name__ == "__main__":
    main()
