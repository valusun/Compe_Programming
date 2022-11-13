def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    dp = [[[False for _ in range(2)] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(M + 1):
            for k in range(2):
                if not dp[i][j][k]:
                    continue
                dp[i + 1][j][k] = True
                if j + W[i] <= M:
                    dp[i + 1][j + W[i]][(k + 1) % 2] = True
    print("Yes" if dp[N][M][1] else "No")


if __name__ == "__main__":
    main()
