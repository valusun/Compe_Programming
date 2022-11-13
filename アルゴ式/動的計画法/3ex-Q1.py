def main():
    N, A = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))
    PQR = [[P[i], Q[i], R[i]] for i in range(N)]
    INF = 10**9
    dp = [[INF] * 3 for _ in range(N)]
    dp[0] = PQR[0]
    for i in range(N - 1):
        for j in range(3):
            for k in range(3):
                if j == k:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + PQR[i + 1][j] - A)
                else:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + PQR[i + 1][j])
    print(min(dp[N - 1]))


if __name__ == "__main__":
    main()
