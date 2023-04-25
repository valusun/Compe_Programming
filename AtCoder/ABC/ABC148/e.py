def main():
    N = int(input())
    if N % 2:
        print(0)
        exit()
    n_div = N // 2
    base = 5
    ans = 0
    while base <= n_div:
        ans += n_div // base
        base *= 5
    print(ans)


if __name__ == "__main__":
    main()
