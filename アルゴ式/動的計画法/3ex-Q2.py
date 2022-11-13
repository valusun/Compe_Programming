def main():
    N, A, B = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))
    PQR = [[P[i], R[i], Q[i]] for i in range(N)]
    INF = 10**9
    dp = [[[INF for _ in range(4)] for _ in range(3)] for _ in range(N)]
    for j in range(3):
        dp[0][j][1] = PQR[0][j]
    for i in range(1, N):
        for j in range(3):
            for pj in range(3):
                if pj == j:
                    continue
                for k in range(1, 4):
                    dp[i][j][1] = min(dp[i][j][1], dp[i - 1][pj][k] + PQR[i][j])
            dp[i][j][2] = dp[i - 1][j][1] + (PQR[i][j] - A)
            dp[i][j][3] = min(dp[i - 1][j][3], dp[i - 1][j][2]) + PQR[i][j] - B
    ans = INF
    for j in range(3):
        ans = min(ans, min(dp[N - 1][j]))
    print(ans)


if __name__ == "__main__":
    main()
