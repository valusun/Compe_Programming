def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0] * N
    dp[1] = A[1]
    for i in range(2, N):
        dp[i] = min(dp[i - 2] + A[i] * 2, dp[i - 1] + A[i])
    print(dp[N - 1])


if __name__ == "__main__":
    main()
