def main():
    N, M, K = map(int, input().split())
    MOD = 998244353

    # Kが0のときは制限がないためM^N
    if K == 0:
        print(pow(M, N, MOD))
        exit()

    # 数列の最初は 1<=M 間であれば何でもいい
    dp = [1] * M

    for _ in range(N - 1):
        next_dp = [0] * M
        for i in range(M):
            next_dp[0] += dp[i]
            next_dp[max(0, i - K + 1)] -= dp[i]
            if i + K < M:
                next_dp[i + K] += dp[i]
        now = 0
        for i in range(M):
            now += next_dp[i]
            now %= MOD
            dp[i] = now
    ans = 0
    for i in range(M):
        ans = (ans + dp[i]) % MOD
    print(ans)


if __name__ == "__main__":
    main()
