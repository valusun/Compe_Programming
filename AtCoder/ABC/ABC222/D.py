def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    LIMIT = 3001
    MOD = 998244353
    dp = [[0] * LIMIT for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N + 1):
        for j in range(LIMIT - 1):
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= MOD
        if i != N:
            for j in range(A[i], B[i] + 1):
                dp[i + 1][j] += dp[i][j]
    print(dp[N][LIMIT - 1])


if __name__ == "__main__":
    main()
