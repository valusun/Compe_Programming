def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    C = list(map(int, input().split()))
    color_cnt = 256
    CW = [[] for _ in range(color_cnt)]
    for c, w in zip(C, W):
        CW[c].append(w)
    dp = [[False] * (M + 1) for _ in range(color_cnt + 1)]
    dp[0][0] = True
    for i in range(color_cnt):
        for j in range(M + 1):
            if not dp[i][j]:
                continue
            dp[i + 1][j] = True
            for w in CW[i]:
                if j + w <= M:
                    dp[i + 1][j + w] = True
    print("Yes" if dp[color_cnt][M] else "No")


if __name__ == "__main__":
    main()
