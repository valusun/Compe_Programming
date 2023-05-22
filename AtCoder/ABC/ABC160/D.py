def main():
    N, X, Y = map(int, input().split())
    ans = [0] * (N - 1)
    X, Y = X - 1, Y - 1
    for i in range(N):
        for j in range(i + 1, N):
            k = abs(i - j)
            mn = min(k, abs(i - X) + abs(Y - j) + 1)
            ans[mn - 1] += 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
