def main():
    N = int(input())
    INPUT_SIZE = 10**5
    X = [0] * (INPUT_SIZE + 1)
    A = [0] * (INPUT_SIZE + 1)
    for _ in range(N):
        t, x, a = map(int, input().split())
        X[t] = x
        A[t] = a

    dp = [[-(10**18)] * 5 for _ in range(INPUT_SIZE + 1)]
    dp[0][0] = 0
    for t in range(1, INPUT_SIZE + 1):
        for i in range(5):
            dp[t][i] = dp[t - 1][i]
            if i != 0:
                dp[t][i] = max(dp[t][i], dp[t - 1][i - 1])
            if i != 4:
                dp[t][i] = max(dp[t][i], dp[t - 1][i + 1])
        dp[t][X[t]] += A[t]
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
