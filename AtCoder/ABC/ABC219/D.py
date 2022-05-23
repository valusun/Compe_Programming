def main():
    N = int(input())
    X, Y = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    INF = 10**9
    dp = [[[INF] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    def chmin(i, j, k, x):
        if x < dp[i][j][k]:
            dp[i][j][k] = x

    for i in range(N):
        for j in range(X + 1):
            min_tako = min(j + A[i], X)
            for k in range(Y + 1):
                min_tai = min(k + B[i], Y)
                if dp[i][j][k] < INF:
                    # 弁当を食べない
                    chmin(i + 1, j, k, dp[i][j][k])
                    chmin(i + 1, min_tako, min_tai, dp[i][j][k] + 1)
    print(dp[N][X][Y] if dp[N][X][Y] != INF else -1)


if __name__ == "__main__":
    main()
