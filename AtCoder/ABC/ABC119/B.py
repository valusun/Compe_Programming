def main():
    N = int(input())
    RATE = 380000
    ans = 0
    for _ in range(N):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x) * RATE
    print(ans)


if __name__ == "__main__":
    main()
