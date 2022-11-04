def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    dp[0] = A
    for i in range(1, N):
        for j in range(N):
            dp[i][j] = dp[i - 1][j]
            if j:
                dp[i][j] += dp[i - 1][j - 1]
            if j < N - 1:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= 100
    print(dp[N - 1][N - 1])


if __name__ == "__main__":
    main()
