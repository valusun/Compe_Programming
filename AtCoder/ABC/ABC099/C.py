def main():
    N = int(input())
    dp = [N] * (N + 1)
    dp[0] = 0

    for n in range(N):
        for p in (6, 9):
            x = 1
            while n + x <= N:
                dp[n + x] = min(dp[n + x], dp[n] + 1)
                x *= p
    print(dp[N])


if __name__ == "__main__":
    main()
