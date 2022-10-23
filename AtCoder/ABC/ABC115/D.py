def main():
    N, X = map(int, input().split())
    size, patty = [1], [1]
    for i in range(N):
        size.append(size[i] * 2 + 3)
        patty.append(patty[i] * 2 + 1)

    def rec(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        median = (size[n] + 1) // 2
        if x < median:
            return rec(n - 1, x - 1)
        elif x == median:
            return patty[n - 1] + 1
        else:
            return patty[n - 1] + 1 + rec(n - 1, x - median)

    print(rec(N, X))


if __name__ == "__main__":
    main()
