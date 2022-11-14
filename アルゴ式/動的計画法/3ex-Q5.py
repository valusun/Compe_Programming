def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    INF = 10**9
    dp = [[INF] * 4 for _ in range(N + 1)]
    dp[0][3] = 0
    for i in range(1, N + 1):
        dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + A[0][i - 1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][3]) + A[1][i - 1]
        dp[i][3] = min(dp[i - 1][1:4]) + A[0][i - 1] + A[1][i - 1]
    print(min(dp[N]))


if __name__ == "__main__":
    main()
