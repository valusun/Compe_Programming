def main():
    N, M, K = map(int, input().split())
    ng_edges = [list(map(int, input().split())) for _ in range(M)]
    MOD = 998244353
    dp = [[0] * N for _ in range(K + 1)]
    dp[0][0] = 1
    for i in range(K):
        s = sum(dp[i]) % MOD
        for j in range(N):
            dp[i + 1][j] = (s - dp[i][j]) % MOD
        for u, v in ng_edges:
            dp[i + 1][v - 1] -= dp[i][u - 1]
            dp[i + 1][u - 1] -= dp[i][v - 1]
            dp[i + 1][v - 1] %= MOD
            dp[i + 1][u - 1] %= MOD
    print(dp[K][0])


if __name__ == "__main__":
    main()
