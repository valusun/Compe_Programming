def main():
    A = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(4)]
    dp[0] = A
    for i in range(1, 4):
        for j in range(4):
            dp[i][j] = dp[i - 1][j]
            if j:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 3:
                dp[i][j] += dp[i - 1][j + 1]
    print(dp[3][3])


if __name__ == "__main__":
    main()
