def main():
    N, _ = map(int, input().split())
    D = list(map(int, input().split()))
    dp = [False] * (N + 1)
    dp[0] = True
    for i in range(N):
        if not dp[i]:
            continue
        for d in D:
            if i + d > N:
                continue
            dp[i + d] = True
    print("Yes" if dp[N] else "No")


if __name__ == "__main__":
    main()
