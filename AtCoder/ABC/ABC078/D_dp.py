def main():
    N, Z, W = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0] * 2 for _ in range(N + 1)]

    for i in range(N - 1, -1, -1):

        # 先手
        Y = A[i - 1] if i else W
        dp[i][0] = abs(Y - A[-1])
        for j in range(i + 1, N):
            dp[i][0] = max(dp[i][0], dp[j][1])

        # 後手
        X = A[i - 1] if i else Z
        dp[i][1] = abs(X - A[-1])
        for j in range(i + 1, N):
            dp[i][1] = min(dp[i][1], dp[j][0])

    print(dp[0][0])


if __name__ == "__main__":
    main()
