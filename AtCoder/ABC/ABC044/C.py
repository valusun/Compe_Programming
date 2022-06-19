def main():
    N, A = map(int, input().split())
    X = list(map(int, input().split()))
    N_MAX = X_MAX = 51
    dp = [[[0] * (N_MAX * X_MAX) for _ in range(N_MAX)] for _ in range(N_MAX)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            for k in range(N_MAX * X_MAX):
                if dp[i][j][k]:
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j + 1][k + X[i]] += dp[i][j][k]
    ans = 0
    for i in range(1, N + 1):
        ans += dp[N][i][i * A]
    print(ans)


if __name__ == "__main__":
    main()
