def main():
    _ = int(input())
    A = list(map(int, input().split()))
    _ = int(input())
    B = list(map(int, input().split()))
    X = int(input())
    dp = [False] * (X + 1)
    for b in B:
        dp[b] = None

    dp[0] = True
    for i in range(X + 1):
        if not dp[i] or dp[i] is None:
            continue
        for a in A:
            if i + a > X or dp[i + a] is None:
                continue
            dp[i + a] = True

    print("Yes" if dp[X] else "No")


if __name__ == "__main__":
    main()
