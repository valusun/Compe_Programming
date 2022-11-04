def main():
    N = int(input())
    fields = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = fields[0][0]
    for i in range(N):
        for j in range(N):
            if i + 1 < N:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + fields[i + 1][j])
            if j + 1 < N:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + fields[i][j + 1])
    print(dp[N - 1][N - 1])


if __name__ == "__main__":
    main()
