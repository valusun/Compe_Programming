def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        l, r = map(int, input().split())
        ans += r - l + 1
    print(ans)


if __name__ == "__main__":
    main()
