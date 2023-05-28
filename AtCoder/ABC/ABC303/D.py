def main():
    X, Y, Z = map(int, input().split())
    S = input()
    N = len(S)
    dp = [[10**18] * 2 for _ in range(N + 1)]
    dp[0][0] = 0
    for i, s in enumerate(S):
        p = 0 if s.islower() else 1
        for j in range(2):
            for k in range(2):
                add = 0
                if j != k:
                    add += Z
                add += X if j == p else Y
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + add)
    print(min(dp[N]))


if __name__ == "__main__":
    main()
