def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[[-1] * (D) for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        # K個選び終わっても選ばない処理を行うため
        for j in range(K + 1):
            for k in range(D):
                if dp[i][j][k] == -1:
                    continue
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                nxt = dp[i][j][k] + A[i]
                # 既にK個選んだならば行わない
                if j == K:
                    continue
                dp[i + 1][j + 1][(k + A[i]) % D] = max(
                    dp[i + 1][j + 1][(k + A[i]) % D], nxt
                )
    print(dp[N][K][0])


if __name__ == "__main__":
    main()
