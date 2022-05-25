def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0] * 10 for _ in range(N)]
    dp[0][A[0]] = 1
    MOD = 998244353
    for i in range(N - 1):
        for j in range(10):
            if dp[i][j]:
                f = (j + A[i + 1]) % 10
                g = (j * A[i + 1]) % 10
                dp[i + 1][f] = (dp[i + 1][f] + dp[i][j]) % MOD
                dp[i + 1][g] = (dp[i + 1][g] + dp[i][j]) % MOD
    for i in dp[N - 1]:
        print(i)


if __name__ == "__main__":
    main()
