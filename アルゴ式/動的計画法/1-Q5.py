def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [10**18] * N
    dp[0] = 0
    for i in range(1, N):
        for j in range(1, min(i + 1, M + 1)):
            dp[i] = min(dp[i], dp[i - j] + A[i] * j)
    print(dp[N - 1])


if __name__ == "__main__":
    main()
