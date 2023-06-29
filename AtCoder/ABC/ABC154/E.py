def main():
    N = input()
    N_len = len(N)
    K = int(input())

    dp = [[[0] * (K + 2) for _ in range(2)] for _ in range(N_len + 1)]
    dp[0][0][0] = 1

    for i in range(N_len):
        for k in range(K + 1):
            # i桁目まででNより小さいならば、i+1桁目は何を選んでもよい
            dp[i + 1][1][k + 1] += dp[i][1][k] * 9  # 1~9を選んだ
            dp[i + 1][1][k] += dp[i][1][k]  # 0を選んだ

            ni = int(N[i])

            # i桁目まではNと同じ、i+1桁目でN以下になる
            if ni > 0:
                dp[i + 1][1][k] += dp[i][0][k]  # 0を選んだ
                dp[i + 1][1][k + 1] += dp[i][0][k] * (ni - 1)  # 1~N[i]-1までの数を選んだ

            # i桁目まではNと同じ、i+1桁目もNと同じ
            if ni > 0:
                dp[i + 1][0][k + 1] += dp[i][0][k]  # N[i+1]が0以外
            else:
                dp[i + 1][0][k] += dp[i][0][k]
    print(dp[N_len][0][K] + dp[N_len][1][K])


if __name__ == "__main__":
    main()
