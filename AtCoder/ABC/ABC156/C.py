def main():
    _ = int(input())
    X = list(map(int, input().split()))
    ans = 10**10
    for i in range(min(X), max(X) + 1):
        tmp = 0
        for x in X:
            tmp += (x - i) ** 2
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
