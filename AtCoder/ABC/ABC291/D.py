def main():
    N = int(input())
    cards = [list(map(int, input().split())) for _ in range(N)]
    MOD = 998244353
    dp = [[0, 0] for _ in range(N)]
    dp[0] = [1, 1]
    for i in range(1, N):
        for j in range(2):
            for k in range(2):
                if cards[i - 1][j] == cards[i][k]:
                    continue
                dp[i][k] += dp[i - 1][j]
        dp[i][0] %= MOD
        dp[i][1] %= MOD

    print((dp[N - 1][0] + dp[N - 1][1]) % MOD)


if __name__ == "__main__":
    main()
