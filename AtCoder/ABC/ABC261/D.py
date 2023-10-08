from collections import Counter


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonuses = Counter()
    for _ in range(M):
        c, y = map(int, input().split())
        bonuses[c] = y
    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
            point = dp[i][j] + bonuses[j + 1] + X[i]
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], point)
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
