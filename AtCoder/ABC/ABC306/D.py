def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 2 for _ in range(N + 1)]
    for i in range(N):
        X, Y = XY[i]
        for j in range(2):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])  # 食べない
            if X == 0:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + Y)
            else:
                if j == 1:
                    continue  # 死ぬため考えない
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][j] + Y)
    print(max(dp[N]))


if __name__ == "__main__":
    main()
