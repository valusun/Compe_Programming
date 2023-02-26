def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    BASE = 10**4
    MAX_NUMS = 2 * BASE
    x_dp = [[False] * (MAX_NUMS + 1) for _ in range(N)]
    y_dp = [[False] * (MAX_NUMS + 1) for _ in range(N)]
    x_dp[0][BASE] = True
    y_dp[0][BASE] = True
    for i in range(N - 1):
        for j in range(MAX_NUMS):
            if x_dp[i][j]:
                if i % 2 == 0:
                    x_dp[i + 1][j] |= x_dp[i][j]
                else:
                    x_dp[i + 1][j + A[i + 1]] = True
                    x_dp[i + 1][j - A[i + 1]] = True
            if y_dp[i][j]:
                if i % 2 == 0:
                    y_dp[i + 1][j + A[i + 1]] = True
                    y_dp[i + 1][j - A[i + 1]] = True
                else:
                    y_dp[i + 1][j] |= y_dp[i][j]
    if x_dp[N - 1][x + BASE - A[0]] and y_dp[N - 1][y + BASE]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
