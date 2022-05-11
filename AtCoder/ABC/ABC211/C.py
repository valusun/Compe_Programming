def main():
    S = input()
    T = "chokudai"
    MOD = 10**9 + 7
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    for i in range(len(S) + 1):
        dp[i][0] = 1
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
    print(dp[len(S)][len(T)])


if __name__ == "__main__":
    main()
