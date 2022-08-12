def main():
    X, Y = map(int, input().split())
    now = X
    ans = 1
    while (now := now * 2) <= Y:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
