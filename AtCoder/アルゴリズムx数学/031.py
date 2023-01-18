def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    dp[1] = A[0]
    dp[2] = A[1]
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
    print(dp[N])


if __name__ == "__main__":
    main()
