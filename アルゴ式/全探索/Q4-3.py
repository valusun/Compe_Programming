def main():
    L, R = map(int, input().split())
    ans = 0
    for n in range(L, R + 1):
        if str(n) == str(n)[::-1]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
