def main():
    N = int(input())
    A = list(map(int, input().split()))
    INF = 10**9
    dp = [INF] * (N + 1)
    dp[0] = 0
    dp[1] = 0
    for i in range(1, N):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(A[i - 1] - A[i]))
        if i + 2 <= N:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(A[i - 1] - A[i + 1]))
    print(dp[N])


if __name__ == "__main__":
    main()
