def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    INF = 10**10
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M + 1):
            if dp[i][j] == INF:
                continue
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            if j + W[i] <= M:
                dp[i + 1][j + W[i]] = min(dp[i + 1][j + W[i]], dp[i][j] + 1)
    print(-1 if dp[N][M] == INF else dp[N][M])


if __name__ == "__main__":
    main()
