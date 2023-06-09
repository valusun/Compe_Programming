def main():
    X, N = map(int, input().split())
    p = set(map(int, input().split()))
    mn, ans = 100, 100
    for x in range(102):
        if x in p:
            continue
        if abs(X - x) < mn:
            mn = abs(X - x)
            ans = x
    print(ans)


if __name__ == "__main__":
    main()
