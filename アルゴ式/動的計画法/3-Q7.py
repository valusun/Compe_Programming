def main():
    N = int(input())
    W = list(map(int, input().split()))
    M = sum(W) + 1
    dp = [[False] * M for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(M):
            if not dp[i][j]:
                continue
            dp[i + 1][j + W[i]] = True
            dp[i + 1][abs(j - W[i])] = True
    print(dp[N].index(True))


if __name__ == "__main__":
    main()
