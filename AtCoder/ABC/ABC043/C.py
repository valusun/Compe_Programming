def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    for y in range(-100, 101):
        res = 0
        for x in A:
            res += (x - y) ** 2
        ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
