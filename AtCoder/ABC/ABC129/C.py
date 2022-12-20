def main():
    N, M = map(int, input().split())
    dp = [0] * (N + 2)
    for _ in range(M):
        dp[int(input())] = -1
    MOD = 10**9 + 7
    dp[0] = 1
    for i in range(N):
        if dp[i] == -1:
            continue
        if dp[i + 1] != -1:
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
        if dp[i + 2] != -1:
            dp[i + 2] = (dp[i + 2] + dp[i]) % MOD
    print(dp[N])


if __name__ == "__main__":
    main()
