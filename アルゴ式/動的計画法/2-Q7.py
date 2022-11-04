def main():
    N = int(input())
    fields = [list(map(int, input().split())) for _ in range(N)]
    dp = [[10**10] * N for _ in range(N)]
    dp[0][N - 1] = fields[0][N - 1]
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if i + 1 < N:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + fields[i + 1][j])
            if j:
                dp[i][j - 1] = min(dp[i][j - 1], dp[i][j] + fields[i][j - 1])
    print(dp[N - 1][0])


if __name__ == "__main__":
    main()
