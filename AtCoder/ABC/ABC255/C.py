def main():
    X, A, D, N = map(int, input().split())
    first = A
    last = D * (N - 1) + A
    if D < 0:
        first, last = last, first
        D = -D
    if X < first:
        print(first - X)
    elif X > last:
        print(X - last)
    elif D == 0:
        print(abs(X - first))
    else:
        r = (X - first) % D
        print(min(r, D - r))


if __name__ == "__main__":
    main()
