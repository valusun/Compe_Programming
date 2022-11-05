def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    dp = [[False] * (M + 1) for i in range(N + 1)]  # i番目まで見たときにjが成り立つか
    dp[0][0] = True
    for i in range(N):
        for j in range(M):
            if not dp[i][j]:
                continue
            dp[i + 1][j] |= dp[i][j]
            if j + W[i] <= M:
                dp[i + 1][j + W[i]] |= dp[i][j]
    print("Yes" if dp[N][M] else "No")


if __name__ == "__main__":
    main()
