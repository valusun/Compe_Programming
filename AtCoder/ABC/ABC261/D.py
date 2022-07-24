from collections import Counter

ans = 0


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    dic = Counter()
    for _ in range(M):
        c, y = map(int, input().split())
        dic[c] = y

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1] + dic[j]
        for j in range(i):
            dp[i][0] = max(dp[i][0], dp[i - 1][j])

    ans = 0
    for i in range(N + 1):
        ans = max(ans, dp[N][i])
    print(ans)


if __name__ == "__main__":
    main()
