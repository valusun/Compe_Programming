def main():
    N = int(input())
    fields = [list(input()) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if i + 1 < N and fields[i + 1][j] == ".":
                dp[i + 1][j] += dp[i][j]
            if j + 1 < N and fields[i][j + 1] == ".":
                dp[i][j + 1] += dp[i][j]
    print(dp[N - 1][N - 1])


if __name__ == "__main__":
    main()
