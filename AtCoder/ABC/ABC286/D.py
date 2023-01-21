def main():
    N, X = map(int, input().split())
    Coins = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X + 1):
            if not dp[i][j]:
                continue
            dp[i + 1][j] = dp[i][j]
            for k in range(Coins[i][1]):
                if j + Coins[i][0] * (k + 1) <= X:
                    dp[i + 1][j + Coins[i][0] * (k + 1)] = True
    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
